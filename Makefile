PYTHON = python3
LINTER = ruff
FORMATTER = black
TYPECHECKER = mypy
TESTER = pytest
NAME = proxiflow
DOC = docs
VERSION = 0.1.0

help:
	@echo "---------------HELP-----------------"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "------------------------------------"

format:
	${FORMATTER} ${NAME}

lint:
	$(LINTER) check ${NAME}

typecheck:
	mypy ${NAME}

test:
	${PYTHON} -m ${TESTER} -v

