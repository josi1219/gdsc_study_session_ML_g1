# Breast Cancer Detection

## Overview
This project implements a clean and efficient **Machine Learning pipeline** for detecting breast cancer based on patient cytology features. It highlights practical skills in **data preprocessing, cleaning, feature scaling, model training, evaluation, and interpretation** using Python.

The project uses **pandas**, **scikit-learn**, and **NumPy** to build and analyze the model.

---

## Features
The pipeline includes:

- **Dataset preprocessing** and handling of missing or non-numeric values (e.g., replacing "?" and filling missing values).  
- **Feature preparation**, including:
  - Removing unnecessary columns (`Sample code number`).  
  - Scaling features with **StandardScaler** for better model performance.  
- **Train–test splitting** for model validation.  
- **Logistic Regression model training** using scikit-learn.  
- **Model evaluation** with:
  - Accuracy score  
  - Confusion Matrix  
  - Classification Report (Precision, Recall, F1-score)  
- **Prediction interpretation**, showing the first 10 test predictions with their:
  - Predicted type (Benign or Malignant)  
  - Actual type  
  - Correctness of the prediction

---

## Technologies Used
- **Python 3**  
- **pandas**  
- **NumPy**  
- **scikit-learn**  

---

## How to Run
1. Clone the repository:
```commandline
git clone https://github.com/josi1219/gdsc_study_session_ML_g1.git
```
2. Navigate to the `Week_3` folder:
```commandline
cd gdsc_study_session_ML_g1/Week_3
```
3. Install required packages if not already installed:
```
pip install pandas numpy scikit-learn
```
4. Run the Python script:
```
python Cancer_Detection.py
```
Or open the Google Colab notebook `Cancer_Detection.ipynb` and run each cell sequentially.

---

## Output

When you run the script/notebook, it generates both **text-based results** and **evaluation metrics**:

### **1. Console Output**
The program prints the **first 10 test predictions** with:

- Predicted type (Benign or Malignant)  
- Actual type  
- Whether the prediction is correct  

This allows quick inspection of the model’s performance on unseen data.

### **2. Performance Metrics**
The evaluation includes:

- **Accuracy Score** – overall correctness of predictions  
- **Confusion Matrix** – breakdown of true positives, true negatives, false positives, and false negatives  
- **Classification Report** – includes Precision, Recall, F1-score, and Support for each class  

These metrics provide insight into how accurate the model is and where it may make errors.

---
.
