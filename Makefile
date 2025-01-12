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

## Run the security tests (using bandit from venv)
security-test:
	./venv/bin/bandit -lll src/*.py test/*.py

## Run the unit tests using unittest (using python from venv)
unit-test:
	PYTHONPATH=${PYTHONPATH} ./venv/bin/$(PYTHON_INTERPRETER) -m unittest discover -s test -p 'test_*.py' -v

## Run the coverage check (using coverage from venv)
check-coverage:
	PYTHONPATH=${PYTHONPATH} ./venv/bin/$(PYTHON_INTERPRETER) -m coverage run -m unittest discover -s test
	PYTHONPATH=${PYTHONPATH} ./venv/bin/$(PYTHON_INTERPRETER) -m coverage report

## Run the Blackjack script (using python from venv)
run-blackjack:
	./venv/bin/$(PYTHON_INTERPRETER) blackjack.py

## Run all checks (including setup and security checks)
run-checks: security-test unit-test check-coverage

##Set-up venv and run all checks
venv-run-checks: install-deps dev-setup run-checks

.DEFAULT_GOAL := venv-run-checks