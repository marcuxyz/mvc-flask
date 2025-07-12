.PHONY: test
test:
	poetry run pytest --cov=flask_mvc --cov-report=xml --cov-report=term-missing -vvv

.PHONY: format
format:
	poetry run black -l 89 tests flask_mvc

.PHONY: check
check:
	poetry run black -l 89 --check flask_mvc tests
