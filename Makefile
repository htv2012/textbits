.PHONY: \
	all \
	clean \
	install \
	lab \
	lint \
	py \
	rename \
	serve \
	test \

### Default target(s)
all: test serve

### Clean up generated files
clean:
	uv clean
	rm -fr .ruff_cache .venv

### Install this tool locally
install:
	uv tool install --upgrade .

### Run Jupyter lab
lab:
	JUPYTER_CONFIG_DIR=etc uv run jupyter lab --notebook-dir=etc/notebooks

### Perform static analysis
lint:
	uv run ruff check --select I --fix .
	uv run ruff format .
	uv run ruff check . --fix

### Open a Python shell
py:
	PYTHONSTARTUP= uv run ipython --profile-dir=./etc/ipython

### Rename the project
rename:
	uv run etc/set_project_name.py

### Run the project
serve: lint
	uv run textbits serve

### Run unit tests
test: lint
	PYTHONBREAKPOINT="pudb.set_trace" uv run pytest -vv

