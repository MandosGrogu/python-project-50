#Makefile
install:
	uv sync
gendiff:
	uv run gendiff
build:
	uv build
package-install:
	uv tool install dist/*.whl
lint:
	uv run ruff check

check: 
	test lint

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml