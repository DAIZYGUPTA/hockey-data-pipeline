#  Hockey Teams Scraping Pipeline

##  Overview

This project is a modular **end-to-end web scraping and data processing pipeline** built using Python.

The pipeline scrapes hockey team data from:

 https://www.scrapethissite.com/pages/forms/

and transforms raw HTML into:

- Structured datasets
- Cleaned analytical data
- Engineered ML-ready features
- Visual reports

The project was built step-by-step following real-world:

- Data Engineering practices
- Software Engineering principles
- ML pipeline structuring approaches

---

#  Features

##  Web Scraping

- Pagination handling
- Query-based scraping
- Session-based requests
- Request retry handling
- Safe HTML parsing
- Modular scraper architecture

---

##  Data Engineering

- Validation layer
- Cleaning layer
- Feature engineering
- Exploratory Data Analysis (EDA)
- Visualization layer

---

##  Storage

- Raw HTML saving
- CSV export
- Parquet export
- Organized data directories

---

##  Engineering Practices

- Modular project structure
- Logging system
- Environment variable support (`.env`)
- CLI support using `argparse`
- Config separation
- Reusable architecture

---

#  Project Structure

```bash
hockey-scraping-pipeline/
│
├── config/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── reports/
│
├── logs/
│
├── src/
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── eda.py
│   │
│   ├── config/
│   │   ├── settings.py
│   │   └── __init__.py
│   │
│   ├── constants/
│   │   ├── constants.py
│   │   └── __init__.py
│   │
│   ├── processing/
│   │   ├── __init__.py
│   │   ├── cleaning.py
│   │   ├── feature_engineering.py
│   │   └── validation.py
│   │
│   ├── scraper/
│   │   ├── __init__.py
│   │   ├── fetcher.py
│   │   ├── paginator.py
│   │   ├── parser.py
│   │   └── storage.py
│   │
│   ├── utils/
│   │   ├── helpers.py
│   │   ├── logger.py
│   │   └── __init__.py
│   │
│   └── visualization/
│       ├── __init__.py
│       └── plots.py
│
├── .env
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── venv/
```

---

#  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Requests | HTTP requests |
| BeautifulSoup4 | HTML parsing |
| Pandas | Data processing |
| Matplotlib | Visualization |
| PyArrow | Parquet support |
| python-dotenv | Environment variables |
| argparse | CLI support |

---

#  Pipeline Flow

```text
Fetch Data
    ↓
Parse HTML
    ↓
Validate Dataset
    ↓
Clean Dataset
    ↓
Feature Engineering
    ↓
EDA
    ↓
Visualization
    ↓
Save Outputs
```

---

#  Feature Engineering

The pipeline creates additional analytical features such as:

- Total Games
- Goal Difference Ratio
- Goals Per Game
- Team Category

These features help prepare the dataset for:

- Analytics
- Dashboards
- Machine Learning workflows

---

#  Generated Outputs

##  Raw Data

```bash
/data/raw/
```

Contains saved HTML pages.

---

##  Processed Data

```bash
/data/processed/
```

Contains:

- CSV datasets
- Parquet datasets

---

##  Reports

```bash
/data/reports/
```

Contains generated visualizations:

- Top Teams Plot
- Yearly Win Trends
- Correlation Matrix

---

#  Installation

## 1️ Clone Repository

```bash
git clone <your-repo-url>
cd hockey-scraping-pipeline
```

---

## 2️ Create Virtual Environment

```bash
python -m venv venv
```

---

## 3️ Activate Environment

### Windows

```bash
venv\Scripts\activate
```


## 4️ Install Requirements

```bash
pip install -r requirements.txt
```

---

#  Environment Variables

Create:

```bash
.env
```

Example:

```env
SCRAPER_DELAY=1

USER_AGENT=Mozilla/5.0

RAW_DATA_PATH=data/raw

PROCESSED_DATA_PATH=data/processed

REPORTS_PATH=data/reports
```

---

# Running The Pipeline

## Scrape All Teams

```bash
python main.py
```

---

## Scrape Specific Teams

Example:

```bash
python main.py --query Boston
```

You can replace:

- Boston
- Chicago
- Detroit
- etc.

---

#  Example Pipeline Output

```text
Pipeline started
Total pages detected: 24
Processing page 1
Collected 25 records from page 1
...
Pipeline completed successfully
```

---

#  Learning Outcomes

This project helped me learn:

- Modular Python architecture
- Data pipeline design
- Web scraping best practices
- Pagination handling
- Data validation
- Data cleaning
- Feature engineering
- Exploratory data analysis
- Visualization workflows
- Environment variable management
- CLI development
- Logging systems

---

#  Future Improvements

Planned improvements:

- YAML configuration
- Pytest testing framework
- Docker support
- CI/CD pipelines
- Scheduling automation
- Database integration
- API integration
- Selenium/Playwright support

---

#  Author

Built as part of my **Learning in Public** journey into:

- Data Engineering
- Machine Learning Engineering
- AI Engineering

---

#  Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🧠 Share feedback
- 🤝 Connect on LinkedIn

---
