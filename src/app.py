from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "best_car_price_model.pkl")

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

CURRENT_YEAR = 2026

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    present_price = None
    depreciation = None
    depreciation_percentage = None
    vehicle_age = None
    insight_message = None

    if request.method == "POST":
        year = int(request.form["year"])
        present_price = float(request.form["present_price"])
        kms_driven = int(request.form["kms_driven"])
        fuel_type = request.form["fuel_type"]
        seller_type = request.form["seller_type"]
        transmission = request.form["transmission"]
        owner = int(request.form["owner"])

        vehicle_age = CURRENT_YEAR - year

        input_data = pd.DataFrame({
            "Present_Price": [present_price],
            "Kms_Driven": [kms_driven],
            "Fuel_Type": [fuel_type],
            "Seller_Type": [seller_type],
            "Transmission": [transmission],
            "Owner": [owner],
            "Vehicle_Age": [vehicle_age]
        })

        predicted_price = model.predict(input_data)[0]
        prediction = round(predicted_price, 2)

        depreciation = round(present_price - prediction, 2)
        depreciation_percentage = round((depreciation / present_price) * 100, 2)

        if depreciation_percentage < 25:
            insight_message = "Great resale value. This car has held its price well."
        elif depreciation_percentage < 50:
            insight_message = "Moderate depreciation. This is common for many used cars."
        else:
            insight_message = "High depreciation. Age, mileage, or market segment may be affecting value."

    return render_template(
        "index.html",
        prediction=prediction,
        present_price=present_price,
        depreciation=depreciation,
        depreciation_percentage=depreciation_percentage,
        vehicle_age=vehicle_age,
        insight_message=insight_message
    )

if __name__ == "__main__":
    app.run(debug=True)
