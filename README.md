# Python + Selenium base template

Create a virtual environment: `python3 -m venv virtualenv`

Activate the venv: `source virtualenv/bin/activate`

Install dependencies: `pip3 install -r requirements.txt`

Select venv in VSCode:

- CTRL (or Command if using a Mac) + Shift + P.
- Search for `"Python: Select Interpreter"`
- Select the `virtualenv` virtual environment.

# Project Structure

- `pages` folder: there should be one `page file` for each page that your application has.
  There is a `BasePage` file which contains common methods for each individual page.
- `tests` folder: there should be one file (prefixed with `test_`) for each page file created in the `pages` folder.
- `locators` folder: there should be one file for each page file created in the `pages` folder.

A `page file` should contain:

- one method for each locator (e.g. getting a button element).
- methods to interact with page elements (e.g. clicking a button element).

# Run tests

- `export SIMPLE_SETTINGS=settings.development` - this loads development settings located in `settings/development.py`.
- `pytest -v -s tests/<file_to_test.py>::<ClassToTest>::<function_to_test>`.

### TODO

- Add linter/formatter in pre-commit hook.
