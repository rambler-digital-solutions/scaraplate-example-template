PN := {{ cookiecutter.python_package }}
LINT_TARGET := setup.py src/ tests/
MYPY_TARGET := src/${PN} tests/

# Additional make targets and overrides of the variables defined above
# should go to the following file:
include Makefile.inc


.PHONY: develop
develop:
	@python -m pip install --upgrade pip setuptools wheel
	@python -m pip install -e .[develop]


.PHONY: format
format: format-black format-isort


.PHONY: format-black
format-black:
	@black ${LINT_TARGET}


.PHONY: format-isort
format-isort:
	@isort -rc ${LINT_TARGET}


.PHONY: lint
lint: lint-isort lint-black lint-flake8{% if cookiecutter.mypy_enabled == "1" %} lint-mypy{% endif %}


.PHONY: lint-black
lint-black:
	@python -m black --check --diff ${LINT_TARGET}


.PHONY: lint-flake8
lint-flake8:
	@python -m flake8 --statistics ${LINT_TARGET}


.PHONY: lint-isort
lint-isort:
	@python -m isort.main -df -c -rc ${LINT_TARGET}
{%- if cookiecutter.mypy_enabled == "1" %}


.PHONY: lint-mypy
lint-mypy:
	@python -m mypy ${MYPY_TARGET}
{%- endif %}


.PHONY: test
test:
	@python -m coverage run -m py.test
	@python -m coverage report

venv:
	@python3 -m venv venv
