# Housing Price Prediction

## Overview
This project is a **Machine Learning pipeline** for predicting housing prices using a dataset containing features such as area, bedrooms, bathrooms, and amenities. It demonstrates **data preprocessing, feature engineering, linear regression modeling, and evaluation**, along with visualization of predictions versus actual prices.

The pipeline is implemented in Python using `pandas`, `scikit-learn`, and `matplotlib`.

---

## Features and Engineering
The following steps are applied to the dataset to improve prediction accuracy:

- **Guestroom Conversion:** Convert 'yes'/'no' values to numeric 1/0 for calculations.
- **Total Rooms:** Sum of bedrooms, bathrooms, and guestroom for a more representative feature.
- **Area per Story:** Compute `area / stories` to capture the space distribution per floor.
- **Categorical Encoding:** One-hot encoding applied to categorical features including `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `prefarea`, and `furnishingstatus`.

---

## Data Preprocessing
- Numerical features are kept as-is.
- Categorical features are transformed using `OneHotEncoder` with `drop='first'` to avoid multicollinearity.
- Train-test split: 80% training, 20% testing (`random_state=42` for reproducibility).

---

## Model
- **Algorithm:** Linear Regression (`sklearn.linear_model.LinearRegression`)
- **Training:** Model is trained on the preprocessed training data.
- **Evaluation Metrics:**
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  
---

## Visualization
- Scatter plot of actual vs. predicted prices.
- Diagonal reference line to visualize prediction accuracy.

---

## Usage
1. Ensure Python 3.x is installed.
2. Install required packages:
   ```bash
   pip install pandas scikit-learn matplotlib
3. Place the dataset `Housing.csv` in the same directory as the script.

4. Run the script:
```bash
    python housing_price_prediction.py

## Output

- The first 10 predictions vs. actual prices will be printed in the console.
- A scatter plot will be displayed showing predicted prices versus actual prices.

---

## Dependencies

- `pandas`
- `scikit-learn`
- `matplotlib`

