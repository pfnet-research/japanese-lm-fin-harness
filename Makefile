RUN := uv run
.PHONY: check
check: lint mypy
.PHONY: lint
lint: lint-black lint-isort lint-flake8
.PHONY: lint-black
lint-black:
	$(RUN) black --check --diff --quiet . 
.PHONY: lint-isort
lint-isort:
	$(RUN) isort --check --quiet . 
.PHONY: lint-flake8
lint-flake8:
	$(RUN) pflake8 . 
.PHONY: mypy
mypy:
	$(RUN) mypy . 
.PHONY: format
format: format-black format-isort
.PHONY: format-black
format-black:
	$(RUN) black --quiet . 
.PHONY: format-isort
format-isort:
	$(RUN) isort --quiet .
