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

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

active:
	source $(PROJECT_DIR)/env/bin/activate

package:
	$(PYTHON_INTERPRETER) -m build

publish: package
	@echo 'THIS COMMAND ONLY DEPLOYS TO TEST_PYPI'
	@echo 'To deploy to PYPI use the command publish_prod'
	twine check dist/*
	twine upload -r testpypi dist/*

publish_prod: package
	twine check dist/*
	twine upload -r pypi dist/*
