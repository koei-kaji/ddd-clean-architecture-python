DOCKER_TAG_REST=$$(poetry version | awk '{print $$1"-rest:"$$2}')
DOCKERFILE_REST=Dockerfile.rest
export DOCKER_BUILDKIT=1

.PHONY: format
format:
	@poetry run isort .
	@poetry run black .

.PHONY: format-check
format-check:
	@poetry run isort --check .
	@poetry run black --check .

.PHONY: lint
lint:
	@poetry run pylint -d C,R,fixme src/
	@poetry run mypy --show-error-codes src/

.PHONY: test
test:
	@poetry run pytest src/tests
	@poetry run coverage-badge -f -o docs/img/coverage.svg

.PHONY: lint-docker
lint-docker:
	@hadolint ./$(DOCKERFILE_REST)

.PHONY: build-docker
build-docker:
	@docker build --no-cache -t $(DOCKER_TAG_REST) -f $(DOCKERFILE_REST) .

.PHONY: scan-docker
scan-docker:
	@docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
       goodwithtech/dockle:latest --no-color $(DOCKER_TAG_REST)
	@trivy image --ignore-unfixed $(DOCKER_TAG_REST)

.PHONY: docker
docker: lint-docker build-docker scan-docker

.PHONY: pre-commit
pre-commit: format lint test docker

.PHONY: run
run:
	@cd src && poetry run uvicorn rest_api.main:app --reload --port=8000

.PHONY: run-gunicorn
run-gunicorn:
	@cd src && poetry run gunicorn --log-level debug rest_api.main:app

.PHONY: run-docker-rest
run-docker-rest:
	@docker run --rm -p 8000:8000 $(DOCKER_TAG_REST)