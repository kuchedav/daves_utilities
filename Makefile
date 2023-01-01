#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = test
PYTHON_INTERPRETER = $(PROJECT_DIR)/env/bin/python

globals:
	@echo '=============================================='
	@echo '=    displaying all global variables         ='
	@echo '=============================================='
	@echo 'PROJECT_DIR: ' $(PROJECT_DIR)
	@echo 'PROJECT_NAME: ' $(PROJECT_NAME)
	@echo 'PYTHON_INTERPRETER: ' $(PYTHON_INTERPRETER)

functions:
	@echo '=============================================='
	@echo '=    displaying all functions available      ='
	@echo '=============================================='
	@echo 'test: run tox to fully test package'
	@echo 'publish: publish package to pypi_test server'
	@echo 'publish_prod: publish package to pypi server'

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

package:
	rm -rf dist/*
	$(PYTHON_INTERPRETER) -m build

check_credentials_exist:
	[ -f ~/.pypi ] && echo 'pypi credentials found' || echo '~/.pypi file not found!'

publish: package check_credentials_exist
	twine check dist/*
	twine upload --repository testpypi --config-file ~/.pypi dist/*
	@echo '==============================================='
	@echo 'THIS COMMAND ONLY DEPLOYS TO TEST_PYPI'
	@echo 'To deploy to PYPI use the command publish_prod'

publish_prod: check_credentials_exist test
	twine check dist/*
	twine upload --repository pypi --config-file ~/.pypi dist/*

test:
	tox
