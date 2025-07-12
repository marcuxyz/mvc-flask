.PHONY: test
test:
	poetry run pytest --cov=flask_mvc --cov-report=xml --cov-report=term-missing -vvv


.PHONY: format
format:
	@black . -l 89


.PHONY: check
check:
	poetry run black -l 89 --check .
