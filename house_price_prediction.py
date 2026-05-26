import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
data = pd.read_csv("house_prices.csv")

print("Dataset Preview:")
print(data.head())

# Features (X) and Target (y)
X = data[["Size", "Bedrooms", "Age"]]
y = data["Price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("\nModel Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Predict custom input
print("\nCustom Prediction:")
size = int(input("Enter house size: "))
bedrooms = int(input("Enter number of bedrooms: "))
age = int(input("Enter house age: "))

prediction = model.predict([[size, bedrooms, age]])
print("Predicted Price:", prediction[0])