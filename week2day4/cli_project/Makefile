.PHONY: format lint test clean

format:
	black .
	isort .

lint:
	pylint yourpkg/**/*.py

test:
	pytest tests/

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +