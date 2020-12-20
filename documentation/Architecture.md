# Architecture

## Structure

Project structure:

- **/src**
    - main classes (StatAnalyzer, Dataset, FileAccess)
    - **/analyses**
        - Contains logic for analysis tasks
    - **/gui**
        * main classes for gui
        - **/analysis_setup**
            - Contains setup-vies for specific analysis jobs (extending the class Setup)
        - **/output_elements**
            - Classes for different type elements "outputs" are made of (header/text/table etc.)
    - **/math_helper**
        - Functions implementing some simple math
    - **/misc**
        - Miscellanious helper functions
    - **/tests**
        - Tests for main classes
        - **/analysis_tests**
            - Tests for analysis-related functions
        - **/misc_tests**
            - Tests for misc functions
    - **/test_helpers**
        - Helpers for tests

        
##  User interface

The application has one main view that lists the possible analysis tasks for a dataset. 

Each of the analysis tasks have a distinct view for the setup (choose variable(s) for analysis etc.). 

The output of the analysis tasks are displayed in a separate window so that the can control which of the outputs to display permanently. 

## Application logic

Available analysis tasks are defined in [analyses_config.py](../src/analyses_config.py). It defines a function which returns a dictionary in which each element is a dictionary represents an analysis tasks. The dictionaries bind together the actual function for the analysis and the setup view for the analysis.

The main class responsible for executing application logic (statistical analysis) is StatAnalyzer. The GUI knows of only one StatAnalyzer. 

The data is accessed through Dataset which provides getters for the actual data and metadata on columns (type of data).

Each "analysis task" (e.g. summary statistics or frequency table) has it's own implementation of the class "Setup". The class is responsible for calling StatAnalyzer for the specific analysis and construct the output of the analysis results.


![Architecture](logical_structure.png)


## Functionality

### Loading a dataset

![dataset_load](sequence_data_load.png)

### Summary statistics

![summary](sequence_summary.png)