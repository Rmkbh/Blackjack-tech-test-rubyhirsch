#################################################################################
#
# Makefile for Blackjack Game Project
#
#################################################################################

PROJECT_NAME = blackjack-rubyhirsch
PYTHON_INTERPRETER = python3
WD=$(shell pwd)
PYTHONPATH=${WD}:${WD}/src
SHELL := /bin/bash
PROFILE = default
PIP := pip

## Create a virtual environment
venv:
	$(PYTHON_INTERPRETER) -m venv venv
	@echo "Virtual environment created."

## Activate the virtual environment 
activate:
	@echo "Run: source venv/bin/activate"

## Install dependencies (black, coverage, bandit)
install-deps: venv
	./venv/bin/$(PIP) install --upgrade pip
	./venv/bin/$(PIP) install coverage bandit
	@echo "Dependencies installed."

## Install coverage
coverage:
	./venv/bin/$(PIP) install coverage

## Install bandit
bandit:
	./venv/bin/$(PIP) install bandit

## Set up dev requirements
dev-setup: coverage bandit

# Build / Run

## Run the security tests (now with venv activation)
security-test:
	source ./venv/bin/activate && bandit -lll src/*.py test/*.py

## Run the unit tests using unittest (with venv activation)
unit-test:
	source ./venv/bin/activate && PYTHONPATH=${PYTHONPATH} python3 -m unittest discover -s test -p 'test_*.py' -v

## Run the coverage check (with venv activation)
check-coverage:
	source ./venv/bin/activate && PYTHONPATH=${PYTHONPATH} coverage run -m unittest discover -s test
	source ./venv/bin/activate && PYTHONPATH=${PYTHONPATH} coverage report

## Run the Blackjack script (with venv activation)
run-blackjack:
	source ./venv/bin/activate && python3 blackjack.py

## Run all checks (including setup and security checks)
run-checks: activate security-test unit-test check-coverage

## Set up venv and run all checks
venv-run-checks: install-deps dev-setup run-checks

.DEFAULT_GOAL := venv-run-checks
