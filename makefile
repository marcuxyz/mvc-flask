.PHONY: test
test:
	@ward

	
.PHONY: format
format:
	@black . -l 79


.PHONY: check
check:
	@black . -l 79 --check

