# Statistical analysis application

The application provides an access to simple statistical analysis for text files.

## Documentation

* [Requirements](https://github.com/toppyy/ot-harjoitustyo/blob/master/documentation/Requirements.md)
* [Timesheet](https://github.com/toppyy/ot-harjoitustyo/blob/master/documentation/Timesheet.md)
* [Architecture](https://github.com/toppyy/ot-harjoitustyo/blob/master/documentation/Architecture.md)

## Setup and running the application

1. Install dependencies

```bash
python3 -m pipenv install
```

2. To run the application
```bash
python3 -m pipenv run start
```
At the moment it's only possible to analyze an example dataset. To analyse a different dataset, manipulate the index.py-file. 

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
