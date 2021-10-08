#!/bin/bash
poetry run pytest && \
	poetry run coverage erase && \
	poetry run coverage run --branch --source gilded_rose gilded_rose_test.py && \
	poetry run coverage report -m && \
	poetry run coverage html
