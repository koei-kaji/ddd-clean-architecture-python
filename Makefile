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
	@poetry run pylint -d C,R,fixme \
		src/custom_pydantic \
		src/rest_api \
		src/todo \
		tests
	@poetry run mypy --show-error-codes \
		src/custom_pydantic \
		src/rest_api \
		src/todo \
		tests

.PHONY: test
test:
	@poetry run pytest tests
	@poetry run coverage-badge -f -o docs/img/coverage.svg

.PHONY: pre-commit
pre-commit: format lint test

.PHONY: run
run:
	@cd src && poetry run uvicorn rest_api.main:app --reload --port=8000

.PHONY: run-gunicorn
run-gunicorn:
	@cd src && poetry run gunicorn --log-level debug rest_api.main:app