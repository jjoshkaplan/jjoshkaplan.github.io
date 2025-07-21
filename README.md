# Moneyball 2.0: Investigating the Relationship between Team Spend and Success

## Installation

This project is installable as a standard Python package. Dependencies and other project information are included in [`pyproject.toml`](pyproject.toml). You can use pip or get set up quickly using [uv](https://docs.astral.sh/uv/getting-started/installation/).

### pip

```text
pip install -e .
```

> [!TIP]
> pip support for installing from `[dependency-groups]` was just added and should be released soon. In the meantime, development dependencies must be manually installed.

### uv

```text
uv sync
```

## Usage

With the package installed, the project can be called with the `mads-capstone` command from the root of the repository. The tool supports skipping certain steps by passing optional arugments. Skipping data scraping (and thus using the existing provided data) with `--skip-scraping` is highly recommended to save time. Note: running the project may cause file changes due to how some visualizations contain nondeterministic/timestamp dependent metadata.

```text
mads-capstone --skip-scraping
```

```text
mads-capstone -h
usage: mads-capstone [-h] [--skip-scraping] [--skip-modeling] [--skip-viz]

options:
  -h, --help       show this help message and exit
  --skip-scraping  skip data scaping and cleaning
  --skip-modeling  skip running predictive models
  --skip-viz       skip generating visualizations
```

## Data

The data used for our analysis is included in this repository under the [`data`](data) folder. We collected and included the data we used in this repository for the purposes of our analysis, but these should not be redistributed in a manner that violates the terms of the data sources.

### Sports Reference

The majority of sports statistics comes from [Sports Reference](https://www.sports-reference.com/). This website includes detailed information for [MLB](https://www.baseball-reference.com/), [NBA](https://www.basketball-reference.com/), and [NFL](https://www.pro-football-reference.com/).

Sports Reference has [policies](https://www.sports-reference.com/data_use.html) restricting the use of redistributing their data as a competitive database and of using their data to train generative artificial intelligence models. They also have restrictions on abusively scraping their data.

### Over The Cap

Data was collected from [Over The Cap](https://overthecap.com/) for NFL positional spending. Their [terms](https://overthecap.com/terms-and-conditions) prohibit collecting and scraping their pages for competitive commercial purposes.

### HoopsHype

NBA team salaries were collected from [HoopsHype](https://hoopshype.com/). Their [terms](https://cm.usatoday.com/terms/) prohibit commercial use of their materials.

### Spotrac

[Spotrac](https://www.spotrac.com/) was used to collect salary information for MLB teams. Their [terms](https://www.spotrac.com/service/) outline prohibited uses such as republishing their data in a database or compilation.
