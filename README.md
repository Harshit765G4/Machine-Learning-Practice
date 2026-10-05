# Machine Learning Practice

A hands-on learning repository covering the foundations that lead into **Machine Learning and Data Science**: Python programming, data structures, NumPy, Pandas, statistics, visualization, data preprocessing, and end-to-end machine-learning practice.

The repository is notebook-heavy and experiment-driven. It contains small concept exercises alongside larger projects using real datasets such as Heart Disease, Insurance, IPL, country statistics, and student analytics.

## Learning Path

```text
Python
  │
  ├── Control Flow / Functions / Exceptions
  ├── File Handling
  ├── Data Structures
  └── Object-Oriented Programming
          │
          ▼
       NumPy
          │
          ▼
       Pandas
          │
          ▼
 Statistics ──────► Data Visualization
          │
          ▼
   Data Preprocessing
          │
          ▼
   Machine Learning
```

## Repository Highlights

| Area | What is included |
|---|---|
| Python | Functions, loops, exceptions, file handling, data structures, OOP |
| NumPy | Arrays, vectorization, array creation and numerical operations |
| Pandas | Series, DataFrames, joins, concatenation, GroupBy, pivot tables, missing data |
| Statistics | Outliers, ANOVA, Chi-square, linear algebra-style exercises and transformations |
| Visualization | Matplotlib, Seaborn categorical/distribution/regression plots, Plotly/Cufflinks, matrix-style plots |
| Data Preprocessing | Encoding, feature preparation, exploratory analysis, structured ML workflows |
| Machine Learning | End-to-end Heart Disease and Insurance practice notebooks |
| Projects | IPL analysis, country-data analysis, anime feature extraction, student analytics, banking/OOP practice |
| Supporting stack | SciPy, Statsmodels, scikit-learn, XGBoost, LightGBM, CatBoost, SHAP, LIME, PyTorch, and more |

## Directory Structure

```text
Machine-Learning-Practice/
│
├── DataPreprocessing/
│   ├── Heart_Disease_ML_Well_Structured.ipynb
│   ├── heartProject.ipynb
│   ├── heart.csv
│   ├── insuranceProjectPractice.ipynb
│   └── insurance.csv
│
├── dataVisualization/
│   ├── Categorialplot/
│   ├── Distributionplot/
│   ├── IPLCapstoneProject/
│   ├── Matplotlib/
│   ├── Matrixplot/
│   ├── PlotlyandCufflinks/
│   └── Regressionplot/
│
├── numpy/
│   ├── notebook.ipynb
│   └── numpyProjects/
│       ├── practice.ipynb
│       └── numpy_student_analytics_dataset.csv
│
├── pandas/
│   ├── Concepts/
│   └── Projects/
│       ├── AnimeFeatureExtractionProject.ipynb
│       ├── DataCapstoneCountriesProject.ipynb
│       ├── anime.csv
│       └── Countries.csv
│
├── python/
│   ├── ExceptionHandling/
│   ├── FileHandling/
│   ├── Practice_Assignments/
│   ├── data_structures/
│   ├── for_loop/
│   ├── function/
│   ├── objectOrientedProgramming/
│   └── while_loop/
│
├── statistics/
│   └── outliers/
│
└── requirements.txt
```

The repository currently contains **140 tracked paths** across the main learning areas.

## Python Foundations

The `python/` directory builds the programming base required for data science.

### Control Flow

Examples include:

- `for` loops
- `while` loops
- Palindrome checks
- Digit separation
- Number reversal
- Random-number guessing
- String counting

### Functions

The function exercises demonstrate reusable program structure with examples such as:

- Hello-world functions
- String palindrome functions
- Sum-of-two-numbers functions

### Exception Handling

The repository includes standalone exception-handling exercises for learning how Python programs behave when invalid input or runtime errors occur.

### File Handling

The file-handling section demonstrates reading and writing text files and includes a small CRUD-style project.

### Built-in Data Structures

Practice is organized around:

- Lists
- Tuples
- Sets
- Dictionaries

Examples cover operations such as sorting, finding the largest/second-largest element, calculating means, combining dictionaries, frequency counting, and aggregating dictionary values.

### Object-Oriented Programming

The OOP section includes:

- Basic classes and objects
- More advanced OOP concepts
- A bank-management project
- JSON-backed data
- Modular Python packages

It also contains a small banking application split into modules such as `app.py` and `bank.py`.

## NumPy

The `numpy/` directory introduces vectorized numerical computing with NumPy.

The main notebook covers:

- Creating arrays
- Converting lists to arrays
- Multi-dimensional arrays
- `arange`
- `zeros`
- `ones`
- Array generation
- Numerical operations

The `numpyProjects/` directory contains a student-analytics dataset and a practice notebook for applying these operations to a more realistic dataset.

## Pandas

The `pandas/` directory focuses on structured data analysis.

### Concepts

The notebooks cover:

- Series
- DataFrames
- Operations
- GroupBy and aggregation
- Missing data
- Pivot tables
- Merging, joining, and concatenation

### Projects

Two larger analysis projects are included:

#### Country Data Analysis

`DataCapstoneCountriesProject.ipynb` works with a country-level dataset containing fields such as:

- Country and capital
- Currency
- Region / continent
- Latitude / longitude
- Population
- Urban and rural population
- Agricultural land
- Democracy-related fields
- Demographic information

#### Anime Feature Extraction

`AnimeFeatureExtractionProject.ipynb` uses the included `anime.csv` dataset for Pandas-based feature extraction and manipulation practice.

## Data Visualization

The `dataVisualization/` directory contains notebooks focused on visual analysis.

### Matplotlib

The Matplotlib section includes a dedicated notebook and a sample plot image.

### Categorical and Distribution Plots

The repository contains separate notebooks for:

- Categorical plots
- Distribution plots
- Regression plots
- Matrix-style plots

These exercises are useful for learning how to select visualizations based on variable types and analytical questions.

### Plotly and Cufflinks

The repository also includes interactive plotting practice using Plotly/Cufflinks.

### IPL Capstone Project

`dataVisualization/IPLCapstoneProject/` contains an IPL 2022 analysis notebook and dataset.

The project explores match-level attributes such as:

- Date and venue
- Teams
- Toss winner and decision
- First and second innings scores
- Match winner
- Winning margin
- Player of the Match
- Top scorer
- Bowling figures

This project is primarily an exploratory/data-visualization exercise.

## Statistics

The `statistics/outliers/` directory contains notebooks for statistical and mathematical foundations.

Current examples include:

- Outlier analysis
- ANOVA testing
- Chi-square testing
- Dot products
- Gaussian elimination
- Linear transformations
- Determinant calculations

These topics provide mathematical context for later machine-learning work.

## Data Preprocessing and Machine Learning

The strongest ML-focused section is `DataPreprocessing/`.

### Heart Disease Project

The repository contains the Heart Disease dataset with **918 rows and 12 columns**, including:

- Age
- Sex
- ChestPainType
- RestingBP
- Cholesterol
- FastingBS
- RestingECG
- MaxHR
- ExerciseAngina
- Oldpeak
- ST_Slope
- HeartDisease

There are two notebooks:

- `heartProject.ipynb` — exploratory and preprocessing practice
- `Heart_Disease_ML_Well_Structured.ipynb` — a more systematic end-to-end ML workflow

The structured notebook explicitly follows:

```text
Raw data
   ↓
Data understanding
   ↓
Data quality checks
   ↓
EDA + hypotheses
   ↓
Feature engineering
   ↓
Train/test split
   ↓
Preprocessing pipeline
   ↓
Baseline model
   ↓
Cross-validation / model comparison
   ↓
Feature importance / information value
   ↓
Original vs engineered-feature experiment
   ↓
Final test evaluation
   ↓
Interpretation
```

The project emphasizes leakage prevention, hypothesis-driven EDA, feature engineering, feature selection, cross-validation, final test evaluation, and model interpretation.

> **Medical disclaimer:** The Heart Disease notebook is an educational machine-learning exercise and is not a medical diagnostic system.

### Insurance Project

`insuranceProjectPractice.ipynb` works with the included Insurance dataset.

The data contains:

- Age
- Sex
- BMI
- Children
- Smoker
- Region
- Charges

The notebook starts with EDA and data inspection and serves as practice for preparing a tabular dataset for regression-style machine-learning work.

## Machine-Learning Stack

The root `requirements.txt` shows that the environment is designed to support a broad data/ML workflow.

### Core data stack

- NumPy
- Pandas
- SciPy
- Polars
- PyArrow

### Statistics and modeling

- Statsmodels
- scikit-learn

### Visualization

- Matplotlib
- Seaborn
- Plotly
- Dash
- Jupyter/nbformat

### Machine learning

- scikit-learn
- XGBoost
- LightGBM
- CatBoost
- mlxtend
- factor-analyzer

### Interpretability

- SHAP
- LIME

### Deep learning

- PyTorch
- Torchvision
- Pillow

### Large-scale / data processing

- PySpark
- Dask
- Distributed
- DuckDB

### Optimization / simulation

- PuLP
- CVXPY
- SimPy

### Other tooling

- joblib
- memory-profiler
- openpyxl
- PyYAML
- ipykernel

Not every dependency is used by every notebook; the root requirements file is intentionally broad for the overall learning environment.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Harshit765G4/Machine-Learning-Practice.git
cd Machine-Learning-Practice
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\\Scripts\\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the repository dependencies

```bash
pip install -r requirements.txt
```

### 4. Start Jupyter

```jupyter notebook```

or:

```bash
jupyter lab
```

Open the notebook you want to study and run cells from top to bottom unless the notebook itself specifies another order.

## Running Individual Python Exercises

Many files in `python/` are standalone scripts.

For example:

```bash
python python/for_loop/stringPalindrome.py
```

Another example:

```bash
python python/while_loop/randomNumGuessingGame.py
```

For projects with their own data files, run the script from the project directory when relative paths are used.

## Recommended Study Order

A practical way to use this repository is:

```text
01. Python fundamentals
        ↓
02. Functions + exception handling
        ↓
03. Built-in data structures
        ↓
04. OOP
        ↓
05. NumPy
        ↓
06. Pandas
        ↓
07. Statistics
        ↓
08. Data visualization
        ↓
09. Data preprocessing
        ↓
10. End-to-end ML projects
```

For machine-learning preparation, the **Heart Disease structured notebook** is a good central project because it connects EDA, preprocessing, feature engineering, model comparison, evaluation, and interpretation.

## Data Science Workflow Practiced Here

Across the notebooks, the repository develops the following workflow:

```text
Load Data
   ↓
Understand Schema
   ↓
Clean / Validate
   ↓
EDA
   ↓
Visualize
   ↓
Transform / Encode
   ↓
Engineer Features
   ↓
Select Features
   ↓
Train Models
   ↓
Cross-Validate
   ↓
Evaluate
   ↓
Interpret
```

This is the foundation needed before moving into more advanced areas such as deep learning, NLP, computer vision, and MLOps.

## Important Repository Notes

This is a **practice and learning repository**, not a single production-ready machine-learning application.

The code intentionally contains:

- Small concept demonstrations
- Multiple versions of similar exercises
- Experimental notebooks
- Educational datasets
- Course/practice projects
- Broad dependencies covering different phases of learning

Some older or experimental files may not follow modern project-structuring conventions.

The repository also contains generated Python bytecode directories such as `__pycache__` under some folders. These should generally be excluded from source control in future cleanup passes.

## Future Improvements

Potential improvements for turning this archive into a stronger ML portfolio include:

- Add a consistent README to each major project
- Add reusable preprocessing pipelines with scikit-learn
- Add train/validation/test evaluation templates
- Add model comparison tables and experiment tracking
- Add more regression and classification algorithms
- Add hyperparameter tuning examples
- Add explainability examples using SHAP/LIME
- Add reproducible environment locking
- Remove generated `__pycache__` artifacts
- Add automated notebook execution or CI checks
- Separate educational exercises from portfolio-ready projects

## Author

**Harshit Garg**

GitHub: https://github.com/Harshit765G4

## Disclaimer

This repository is intended for educational and experimentation purposes. Models and analyses should be independently validated before being used in real-world decisions, especially in high-stakes domains such as healthcare.
