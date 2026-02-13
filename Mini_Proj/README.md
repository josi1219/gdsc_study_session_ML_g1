# Ride Price Estimation System

## Project Overview
This project builds a machine learning system to estimate ride prices based on trip and contextual factors. The focus is on designing a dataset, cleaning it, training both regression and classification models, and evaluating model performance.

## Dataset Description
- **Source:** Synthetic dataset generated to mimic real-world ride patterns.
- **Rows:** 250 rides
- **Features:** Numerical and categorical
- **Target:** `ride_price` (continuous variable)

The dataset includes missing values, outliers, and variations in traffic, weather, and time of day to simulate realistic conditions.

## Features Used and Justification
- **distance_km:** Longer trips cost more.
- **duration_min:** Captures travel time; affected by traffic.
- **base_fare:** Minimum starting price for rides.
- **demand_level:** Higher demand increases price (surge pricing).
- **traffic_level:** Congestion increases cost.
- **weather_condition:** Rain or storms increase price.
- **time_of_day:** Evening and night rides often have higher prices.
- **high_cost:** Binary target for classification; derived from `ride_price`.

**Feature Considered but Excluded:**  
- Driver rating – excluded because it does not directly determine price and may introduce bias.

## How to Run the Notebook
1. Open `ride_price_model.ipynb` in Google Colab.
2. Ensure all required packages are installed:  
3. Run each cell in order. The notebook will:
- Generate or load the dataset
- Explore and preprocess data
- Train Linear Regression and Logistic Regression models
- Evaluate models and visualize results

## Key Findings
- **Regression:** Linear Regression predicted ride prices with a mean absolute error of ~3.57 dollars.
- **Classification:** Logistic Regression classified rides as high-cost or low-cost with 96% accuracy.
- **Most Influential Features:** Distance and duration had the largest impact on price.
- **Data Quality Impact:** Outliers and missing values were handled; they improve realism but require careful preprocessing.
- **Ethical Consideration:** Surge pricing during emergencies may create unfairly high prices.
- **Limitation:** Dataset is synthetic and simplified; real-world data may include additional complexities.

## Repository Structure
```
Mini_Proj/
├── data/
│   ├── rides.csv
│   └── Data_generator.ipynb
├── ride_price_model.ipynb
└── README.md
```
