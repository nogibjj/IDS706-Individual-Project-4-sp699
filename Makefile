install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=library test_*.py

format:	
	black *.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_*.py *.py

deploy:
	#deploy goes here

all: install test format lint