sync:
	poetry run sync

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/*.whl

make lint:
	poetry run flake8