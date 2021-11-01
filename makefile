.PHONY: test
test:
	FLAKS_ENV=testing ward

	
.PHONY: format
format:
	@black . -l 79


.PHONY: check
check:
	@black . -l 79 --check

