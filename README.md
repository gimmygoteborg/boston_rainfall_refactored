# Boston Rainfall Analysis

This project contains refactored Python code for analyzing historical rainfall data in Boston. It includes data loading, preprocessing, and visualization routines to explore rainfall patterns over time.

## 📁 Repository Structure

```
boston_rainfall_refactored/
├── data/
│   └── boston_rainfall.csv         # Rainfall data CSV file
├── src/
│   ├── data_loader.py              # Functions for loading and preprocessing data
│   ├── visualizations.py           # Plotting and visualization utilities
│   └── main.py                     # Main script to run the analysis
└── README.md                       # Project description and usage instructions
```

## 📦 Requirements

Ensure you have Python 3.7+ installed. Install dependencies using:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not provided, the core dependencies are:

- `pandas`
- `matplotlib`
- `seaborn`

Install them via:

```bash
pip install pandas matplotlib seaborn
```

## ▶️ Usage

Run the main script:

```bash
python src/main.py
```

This will load the rainfall data, perform basic preprocessing, and generate summary plots of rainfall trends in Boston.

## 📊 Features

- Daily/Monthly rainfall aggregation
- Visualization of rainfall trends over years
- Clean, modular, and refactored codebase

## 📈 Example Output

Generated plots include:

- Monthly average rainfall
- Year-over-year rainfall variation
- Rainfall histogram

## 📬 Contact

For questions or suggestions, feel free to open an issue or submit a pull request.
