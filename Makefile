SHELL := /bin/bash

.PHONY: test
test:
	rm -Rf generated_project
	scaraplate rollup . generated_project --no-input \
		metadata_author=scaraplate-tests \
		metadata_author_email=um@rambler-co.ru \
		metadata_description=test
	{ \
		set -e; \
		cd generated_project; \
		make venv; \
		source ./venv/bin/activate; \
		set -x; \
		make develop; \
		make lint; \
		make test; \
		make format; \
	}
