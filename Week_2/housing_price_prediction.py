import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt


# Load the data
data = pd.read_csv("Housing.csv")

# Separate features and target
X = data.drop("price", axis=1)  # features
y = data["price"]               # target

# Feature Engineering for more accurate prediction
# Convert 'yes'/'no' to 1/0 for arithmetic
X['guestroom_num'] = X['guestroom'].map({'yes':1, 'no':0})

# Total rooms: bedrooms + bathrooms + guestroom
X['total_rooms'] = X['bedrooms'] + X['bathrooms'] + X['guestroom_num']

# Area per story
X['area_per_story'] = X['area'] / X['stories']

# Drop the temporary column because we don't need it
X = X.drop('guestroom_num', axis=1)

# Identify categorical features
categorical_features = ['mainroad', 'guestroom', 'basement', 'hotwaterheating',
                        'airconditioning', 'prefarea', 'furnishingstatus']

# Encode categorical features
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(drop='first'), categorical_features)
    ],
    remainder='passthrough'  # numeric columns stay as-is
)

# Transform features
X_transformed = preprocessor.fit_transform(X)

# Split the dataset: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X_transformed,  # all features after encoding
    y,              # target (price)
    test_size=0.2,  # 20% of data for testing, 80% for training
    random_state=42 # ensures the split is the same every time
)

# Create the Linear Regression model
model = LinearRegression()

# Train the model on the training set
model.fit(X_train, y_train)

# Predict prices for the test set
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# printing first 10 predictions vs actual prices
print("First 10 predictions vs actual prices:")
for actual, pred in zip(y_test[:10], y_pred[:10]):
    print(f"Actual: {actual:,.0f}, Predicted: {pred:,.0f}")

# Visualize predictions
plt.scatter(y_test, y_pred, color='red')
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Prices")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'b--')
plt.show()
