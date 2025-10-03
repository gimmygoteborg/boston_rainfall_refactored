# Boston Rainfall Analysis

Analyzes historical rainfall data from the Boston Water and Sewer Commission (BWSC).

## Quick Start

```bash
# Run analysis for 2025 (default)
python run.py

# Run for different years
python run.py 2024
python run.py 2026
```

## Setup

```bash
pip install pandas matplotlib seaborn
```

## Project Structure

```
├── input/          # Raw CSV data files
├── output/         # Generated analysis outputs (organized by year)
├── src/           # Python source code
└── run.py         # Entry point
```

## Features

- Year-based analysis with organized outputs
- Holiday vs. working day rainfall comparison
- Weekend vs. weekday patterns
- Calendar heatmaps and statistical analysis

## Data Source

[Boston Water and Sewer Commission](https://www.bwsc.org/environment-education/rainfall-garden)
