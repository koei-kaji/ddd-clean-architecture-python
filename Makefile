VERSION=$$(rye version)
DOCKER_TAG_BASE=$$(rye show | awk 'NR==1 {print $$2}')
DOCKER_TAG_REST=${DOCKER_TAG_BASE}-rest:${VERSION}
DOCKER_TAG_GRPC=${DOCKER_TAG_BASE}-grpc:${VERSION}
DOCKLE_LATEST=$$( \
  curl --silent "https://api.github.com/repos/goodwithtech/dockle/releases/latest" | \
  grep '"tag_name":' | \
  sed -E 's/.*"v([^"]+)".*/\1/' \
)
TRIVY_LATEST=$$( \
  curl --silent "https://api.github.com/repos/aquasecurity/trivy/releases/latest" | \
  grep '"tag_name":' | \
  sed -E 's/.*"v([^"]+)".*/\1/' \
)
DOCKERFILE_REST=Dockerfile.rest
DOCKERFILE_GRPC=Dockerfile.grpc
export DOCKER_BUILDKIT=1

.PHONY: format
format:
	@rye run isort --extend-skip src/_grpc/ .
	@rye run black --extend-exclude src/_grpc/ .

.PHONY: format-check
format-check:
	@rye run isort --check --extend-skip src/_grpc/ .
	@rye run black --check --extend-exclude src/_grpc/ .

.PHONY: lint
lint:
	@rye run pylint -d C,R,fixme --ignore-paths=src/_grpc/ src/
	@rye run mypy --show-error-codes --exclude src/_grpc/ src/

.PHONY: test
test:
	@rye run pytest src/tests
	@rye run coverage-badge -f -o docs/img/coverage.svg

.PHONY: lint-docker
lint-docker:
	@hadolint ./$(DOCKERFILE_REST)
	@hadolint ./$(DOCKERFILE_GRPC)

.PHONY: build-docker
build-docker:
	@docker build --no-cache -t $(DOCKER_TAG_REST) -f $(DOCKERFILE_REST) .
	@docker build --no-cache -t $(DOCKER_TAG_GRPC) -f $(DOCKERFILE_GRPC) .

.PHONY: scan-docker
scan-docker:
	@docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
       goodwithtech/dockle:v$(DOCKLE_LATEST) --no-color $(DOCKER_TAG_REST)
	@docker run -v /var/run/docker.sock:/var/run/docker.sock \
		-v $${HOME}/Library/Caches:/root/.cache/ \
		aquasec/trivy:$(TRIVY_LATEST) image --ignore-unfixed $(DOCKER_TAG_REST)

	@docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
       goodwithtech/dockle:v$(DOCKLE_LATEST) --no-color $(DOCKER_TAG_GRPC)
	@docker run -v /var/run/docker.sock:/var/run/docker.sock \
		-v $${HOME}/Library/Caches:/root/.cache/ \
		aquasec/trivy:$(TRIVY_LATEST) image --ignore-unfixed $(DOCKER_TAG_GRPC)

.PHONY: docker
docker: lint-docker build-docker scan-docker

.PHONY: pre-commit
pre-commit: generate-grpc format lint test docker

.PHONY: run
run:
	@cd src && rye run uvicorn rest_api.main:app --reload --port=8000

.PHONY: run-gunicorn
run-gunicorn:
	@cd src && rye run gunicorn --log-level debug rest_api.main:app

.PHONY: run-docker-rest
run-docker-rest:
	@docker run --rm -p 8000:8000 $(DOCKER_TAG_REST)

.PHONY: run-docker-grpc
run-docker-grpc:
	@docker run --rm -p 50051:50051 $(DOCKER_TAG_GRPC)

generate-grpc:
	@rye run python -m grpc_tools.protoc \
		-I ./src/grpc_protos/ \
		--python_out=./src/_grpc/ \
		--grpc_python_out=./src/_grpc/ \
		--mypy_out=./src/_grpc/ \
		--mypy_grpc_out=./src/_grpc/ \
		./src/grpc_protos/*.proto
	@rye run python -m grpc_tools.protoc \
		--include_imports \
		--descriptor_set_out=descriptor.temp \
		--proto_path=./src/grpc_protos/ \
		./src/grpc_protos/*.proto \
	&& rye run protol \
		--create-package \
		--in-place \
		--python-out=./src/_grpc/ \
		raw descriptor.temp \
	&& rm descriptor.temp
