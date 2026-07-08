.PHONY: format lint run

format:
	black energy_insights/
	isort energy_insights/

lint:
	pylint energy_insights/

run:
	python -m energy_insights --help