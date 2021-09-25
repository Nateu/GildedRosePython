serv:
	nohup python -m http.server 8000 -d htmlcov &

test:
	pytest && coverage run --branch --source gilded_rose gilded_rose_test.py && coverage report -m && coverage html
	