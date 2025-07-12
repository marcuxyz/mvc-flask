.PHONY: test
test:
	FLAKS_ENV=testing pytest -vvv


.PHONY: format
format:
	@black . -l 89


.PHONY: check
check:
	poetry run black -l 89 --check .
