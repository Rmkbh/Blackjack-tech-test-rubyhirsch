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

## Install dependencies from requirements.txt
install-deps: venv
	./venv/bin/$(PIP) install --upgrade pip
	./venv/bin/$(PIP) install -r requirements.txt
	@echo "Dependencies installed from requirements.txt."

# Build / Run

## Run the security tests (now with venv activation)
security-test:
	source ./venv/bin/activate && bandit -lll src/*.py test/*.py

## Run the unit tests using pytest (with venv activation and warnings disabled)
unit-test:
	source ./venv/bin/activate && PYTHONPATH=${PYTHONPATH} pytest -p no:warnings --tb=short

## Run the coverage check using pytest
check-coverage:
	source ./venv/bin/activate && PYTHONPATH=${PYTHONPATH} pytest --cov=src --cov-report=term-missing

## Run the Blackjack script (with venv activation)
run-blackjack:
	source ./venv/bin/activate && python3 blackjack.py

## Run all checks (including setup and security checks)
run-checks: activate security-test unit-test check-coverage

## Set up venv and run all checks
venv-run-checks: install-deps run-checks

.DEFAULT_GOAL := venv-run-checks