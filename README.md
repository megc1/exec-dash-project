# Executive Dashboard
[![Build Status](https://travis-ci.org/megc1/exec-dash-project.svg?branch=master)](https://travis-ci.org/megc1/exec-dash-project)

## About
This project provides insights into monthly sales data via data visualization methods and summary information. Users may select one month at a time to view top sellers, as well as a graph of sales data over time if desired.

## Getting Started

### Prerequisites
* Anaconda 3.7
* Python 3.7
* Pip

### Installations

For this repository under your account, then clone or download it to your local computer. Then, navigate to the folder from your command line:
```sh
cd exec-dash-project
```
Create a new virtual environment using Anaconda, for example:
```sh
conda create dashboard-env
```
Then, use pip to install the necessary package dependencies for this project:
```sh
pip install pandas plotly
```
## To Use:
From within the app folder, run the script:
```sh
python monthly_sales.py
```

## To Test:

This program can be tested using pytest, which can be downloaded to the virtual environment to run tests from the command line with the pytest command.

To install in your virtual environment:
```sh
pip install pytest
```

To run tests:
```sh
pytest 
```
It is recommended to deploy the project to a continuous integration service, such as [Travis CI](https://travis-ci.org/) for continuous automated testing as further modifications are made to the code. 


## License

This program is licensed under the terms of the MIT License. For more detailed information see [LICENSE.md](LICENSE.md).