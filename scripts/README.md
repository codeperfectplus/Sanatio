# Scripts

1. test_changes.sh - Test if the changes are valid and can be released. flake8/pytest are run and the version is checked.
2. code_coverage.sh - Run the tests and generate a code coverage report.
3. test_release.sh - Test the release on test.pypi.org.
4. release.sh - Release the package to PyPI if both tests are successful.


reference links:

- https://packaging.python.org/en/latest/guides/using-testpypi/
