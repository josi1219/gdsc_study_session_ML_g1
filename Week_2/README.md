# Housing Price Prediction

## Overview
This project implements a clean and efficient **Machine Learning pipeline** for predicting housing prices based on property features such as area, bedrooms, bathrooms, and available amenities. It highlights practical skills in **data preprocessing, feature engineering, model training, evaluation, and visualization** using Python.

The project uses **pandas**, **scikit-learn**, and **matplotlib** to build and analyze the model.

---

## Features
The pipeline includes:

- **Dataset preprocessing** and handling of mixed categorical/numerical features.
- **Feature engineering**, including:
  - Converting "yes"/"no" values into numeric format.
  - Creating `total_rooms` and `area_per_story` for better feature representation.
  - Applying **one-hot encoding** to categorical attributes.
- **Train–test splitting** for model validation.
- **Linear Regression model training** using scikit-learn.
- **Model evaluation** with:
  - Mean Absolute Error (MAE)  
  - Mean Squared Error (MSE)
- **Visualization** showing actual vs. predicted housing prices.

---

## Technologies Used
- **Python 3**
- **pandas**
- **scikit-learn**
- **matplotlib**

---

## How to Run
1. Clone the repository:
```
  git clone https://github.com/josi1219/gdsc_study_session_ML_g1.git
```
2. Navigate to the `Week_2` folder:
```
  cd gdsc_study_session_ML_g1/Week_2
```
3. Install required packages if not already installed:

```
  pip install pandas scikit-learn matplotlib
```
4. Run the Python script:

```
python housing_price_prediction.py
```
## Output

When you run the script, it generates both **text-based results** and a **visual plot**:

### **1. Console Output**
The program prints the **first 10 predicted prices** alongside their corresponding **actual prices** from the test set.  
This allows quick inspection of how closely the model is performing on unseen data.


### **2. Performance Metrics**
The model evaluation includes:

- **Mean Absolute Error (MAE)**  
- **Mean Squared Error (MSE)**  

These metrics provide insight into how accurate the predictions are and help compare future model improvements.

### **3. Visualization**
A **scatter plot** is displayed showing:

- **Actual prices** on the x-axis  
- **Predicted prices** on the y-axis  
- A **diagonal reference line** (perfect prediction line)

This visualization helps you understand:

- How close predictions are to actual values  
- Whether the model systematically overestimates or underestimates prices  
- The overall spread and accuracy of the model  

This makes it useful for quickly diagnosing performance and identifying potential areas for feature improvement or model tuning.



