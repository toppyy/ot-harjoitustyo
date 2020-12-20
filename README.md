# Statistical analysis application

The application provides an access to simple statistical analysis for text files.

## Releases

* [Final](https://github.com/toppyy/ot-harjoitustyo/releases/tag/final)
* [Week 6](https://github.com/toppyy/ot-harjoitustyo/releases/tag/week6)
* [Week 5](https://github.com/toppyy/ot-harjoitustyo/releases/tag/viikko5)

## Documentation

* [Requirements](./documentation/Requirements.md)
* [Timesheet](./documentation/Timesheet.md)
* [Architecture](./documentation/Architecture.md)
* [User guide](./documentation/UserGuide.md)
* [Testing](./documentation/Testing.md)

## Setup and running the application

1. Install dependencies

```bash
python3 -m pipenv install
```
2. Build the app

```bash
python3 -m pipenv run build
```

3. To run the application
```bash
python3 -m pipenv run start
```
At the moment it's only possible to analyze plain text files that separate columns with ";".  

Alternatively you can run `python3 -m pipenv run dev` which loads the example data on start-up.

## Tests and linting

To run tests
```bash
python3 -m pipenv run test
```
To create coverage-report. Gather coverage data and create the report by:
```bash
python3 -m pipenv run coverage && python3 -m pipenv run coverage-report
```
And you'll find the report in /htmlcov

To run the linter:
```bash
python3 -m pipenv run lint
```
