install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --user dist/*.whl

force-install:
	python -m pip install --force-reinstall --user dist/*.whl

gendiff:
	poetry run gendiff

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff
