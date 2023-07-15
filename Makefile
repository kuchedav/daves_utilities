configure_poetry:
	# https://python-poetry.org/docs/repositories/
	# poetry config pypi-token.pypi <my-token>
	# poetry config http-basic.pypi <username> <password>

deploy:
	poetry publish --build
