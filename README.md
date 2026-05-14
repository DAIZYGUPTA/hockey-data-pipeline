Hockey Teams Scraping Pipeline
Overview

This project is a modular end-to-end web scraping and data processing pipeline built using Python.

The pipeline scrapes hockey team data from:

https://www.scrapethissite.com/pages/forms/

and transforms raw HTML into:

structured datasets
cleaned analytical data
engineered ML-ready features
visual reports

The project was built step-by-step following real-world software engineering and data engineering practices.

Project Features
Web Scraping
Pagination handling
Query-based scraping
Session-based requests
Request retry handling
Safe HTML parsing
Modular scraper architecture
Data Engineering
Validation layer
Cleaning layer
Feature engineering layer
EDA (Exploratory Data Analysis)
Visualization layer
Storage
Raw HTML saving
CSV export
Parquet export
Organized data directories
Engineering Practices
Modular project structure
Logging system
Environment variable support (.env)
CLI support using argparse
Config separation
Reusable architecture
Project Structure
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
Technologies Used
Python
Requests
BeautifulSoup4
Pandas
Matplotlib
PyArrow
python-dotenv
argparse
Pipeline Flow
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
Features Engineered

The pipeline creates additional analytical features such as:

Total Games
Goal Difference Ratio
Goals Per Game
Team Category

These features help prepare the dataset for:

analytics
dashboards
machine learning workflows
Generated Outputs
Raw Data
/data/raw/

Contains saved HTML pages.

Processed Data
/data/processed/

Contains:

CSV datasets
Parquet datasets
Reports
/data/reports/

Contains generated visualizations:

Top Teams Plot
Yearly Win Trends
Correlation Matrix
Installation
Clone Repository
git clone <your-repo-url>
cd hockey-scraping-pipeline
Create Virtual Environment
python -m venv venv
Activate Environment
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
Install Requirements
pip install -r requirements.txt
Environment Variables

Create:

.env

Example:

SCRAPER_DELAY=1

USER_AGENT=Mozilla/5.0

RAW_DATA_PATH=data/raw

PROCESSED_DATA_PATH=data/processed

REPORTS_PATH=data/reports
Running The Pipeline
Scrape All Teams
python main.py
Scrape Specific Teams

Example:

python main.py --query Boston

You can replace:

Boston
Chicago
Detroit
etc.
Example Pipeline Output
Pipeline started
Total pages detected: 24
Processing page 1
Collected 25 records from page 1
...
Pipeline completed successfully
Learning Outcomes

This project helped me learn:

Modular Python architecture
Data pipeline design
Web scraping best practices
Pagination handling
Data validation
Data cleaning
Feature engineering
Exploratory data analysis
Visualization workflows
Environment variable management
CLI development
Logging systems
Future Improvements

Planned improvements:

YAML configuration
Pytest testing framework
Docker support
CI/CD pipelines
Scheduling automation
Database integration
API integration
Selenium/Playwright support
Author

Built as part of my Learning in Public journey into:

Data Engineering
Machine Learning Engineering
AI Engineering