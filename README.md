# ML Data Analysis Project - India Case Studies

This project contains a series of data analysis scripts focusing on various critical issues in India, utilizing machine learning and data visualization techniques to derive insights.

## Project Files

The project consists of four primary analysis scripts:

1. **`covid_19_india.py`**: 
   - **Purpose**: Analyzes COVID-19 pandemic data in India.
   - **Functionality**: Loads COVID-19 dataset, filters data for a specific date (July 14, 2020), and identifies the top 10 states with the highest number of confirmed and recovered cases.
   - **Visualizations**: Generates bar plots for confirmed and recovered cases across the top 10 states.

2. **`india_lpg_crisis.py`**: 
   - **Purpose**: Explores the LPG (Liquefied Petroleum Gas) crisis in India.
   - **Functionality**: analyzes supply deficit and the percentage of households affected by the crisis for the year 2026 across different states.
   - **Visualizations**: Creates bar charts showing the supply deficit percentage and household impact per state.

3. **`India_cancer_patients.py`**: 
   - **Purpose**: Analyzes cancer patient data from 2022 to 2025 in India.
   - **Functionality**: Examines patient status (e.g., Deceased, Recovered) across states and further investigates the cancer stage associated with deceased patients.
   - **Visualizations**: Provides bar plots representing state-wise patient status and the distribution of cancer stages among deceased patients.

4. **`India_traffic_violation.py`**: 
   - **Purpose**: Studies traffic violations and patterns across India.
   - **Functionality**: Processes traffic violation data to determine the total number of violations per state and categorizes these violations by type (reason).
   - **Visualizations**: Displays bar plots for total state-wise violations and a detailed breakdown of violation types per state.

## Datasets

The required datasets are located in the `datasets/` directory.

## Setup and Usage

Ensure you have the required Python libraries installed (e.g., pandas, matplotlib, seaborn, scikit-learn).

```bash
pip install pandas matplotlib seaborn scikit-learn
```

Run any of the scripts using:
```bash
python <filename>.py
```
