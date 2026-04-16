from pathlib import Path

folders = [
    "data/raw",
    "data/processed",
    "data/synthetic",
    "notebooks",
    "src/data",
    "src/models",
    "src/evaluation",
    "src/utils",
    "experiments/exp_noise_levels",
    "experiments/exp_seasonality",
    "experiments/exp_nonlinearity",
    "reports/figures"
]

files = [
    "README.md",
    "requirements.txt",
    "config.yaml",
    ".gitignore",
    "notebooks/01_data_exploration.ipynb",
    "notebooks/02_baseline_arima.ipynb",
    "notebooks/03_lstm.ipynb",
    "notebooks/04_xgboost.ipynb",
    "notebooks/05_results_analysis.ipynb",
    "src/data/load_data.py",
    "src/data/preprocess.py",
    "src/data/generate_synthetic.py",
    "src/models/arima_model.py",
    "src/models/lstm_model.py",
    "src/models/xgboost_model.py",
    "src/models/base_model.py",
    "src/evaluation/metrics.py",
    "src/evaluation/backtest.py",
    "src/utils/plotting.py",
    "src/utils/helpers.py",
    "experiments/results.csv",
    "reports/final_report.md"
]

for folder in folders:
    Path(folder).mkdir(parents=True, exist_ok=True)

for file in files:
    Path(file).parent.mkdir(parents=True, exist_ok=True)
    Path(file).touch(exist_ok=True)

print("Struktura gotowa")
