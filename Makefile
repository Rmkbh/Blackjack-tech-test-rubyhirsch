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

## Install black
black:
	$(PIP) install black

## Install coverage
coverage:
	$(PIP) install coverage

## Install bandit
bandit:
	$(PIP) install bandit

## Set up dev requirements
dev-setup: black coverage bandit

# Build / Run

## Run the security tests
security-test:
	bandit -lll src/*.py test/*.py

## Run the black code check
run-black:
	black ./src/*.py ./test/*.py

## Run the unit tests using unittest
unit-test:
	PYTHONPATH=${PYTHONPATH} $(PYTHON_INTERPRETER) -m unittest discover -s test -p '*_test.py' -v

## Run the coverage check
check-coverage:
	PYTHONPATH=${PYTHONPATH} $(PYTHON_INTERPRETER) -m coverage run -m unittest discover -s test
	PYTHONPATH=${PYTHONPATH} $(PYTHON_INTERPRETER) -m coverage report

## Run the Blackjack script
run-blackjack:
	$(PYTHON_INTERPRETER) blackjack.py

## Run all checks
run-checks: security-test run-black unit-test check-coverage
