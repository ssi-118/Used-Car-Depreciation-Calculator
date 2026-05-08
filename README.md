# Used-Car-Depreciation-Calculator
A machine learning regression web application that predicts the resale price of a used car and shows estimated depreciation based on user-provided car details. It considers showroom price, vehicle age, mileage, fuel type, seller type, transmission, and ownership history, then visualizes estimated depreciation and resale value.

## Dataset

The dataset used is the CarDekho car price prediction dataset from Kaggle.
```
https://www.kaggle.com/datasets/bhavikjikadara/car-price-prediction-dataset
```

Dataset file used:

```text
car data.csv
```

Main columns:

```text
Car_Name
Year
Selling_Price
Present_Price
Kms_Driven
Fuel_Type
Seller_Type
Transmission
Owner
```

Target variable:

```text
Selling_Price
```

Input features:

```text
Present_Price
Kms_Driven
Fuel_Type
Seller_Type
Transmission
Owner
Vehicle_Age
```

`Vehicle_Age` is created from:

```text
Vehicle_Age = Current_Year - Year
```

## Algorithms Used

The following regression algorithms were trained and compared:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

## Best Algorithm

The best-performing model was selected based on the highest R2 Score and lowest error metrics.

Best model used:

```text
Random Forest Regressor
```

The final trained model is saved as:

```text
src/best_car_price_model.pkl
```

## Evaluation Metrics

The models were evaluated using:

- MAE: Mean Absolute Error
- RMSE: Root Mean Squared Error
- R2 Score

Example metrics format:

```text
Model                  MAE        RMSE       R2 Score
Linear Regression     1.216226	 1.865155	 0.848981
Decision Tree         0.733770	 1.130603	 0.944509
Random Forest         0.606525	 0.927681	 0.962641
```

Add your actual values from the notebook output here.

## Tech Stack

Machine Learning:

- Python
- Pandas
- NumPy
- Scikit-learn

Visualization:

- Matplotlib
- Seaborn
- Chart.js

Web Framework:

- Flask

Deployment:

- Render
- Gunicorn

Version Control:

- Git
- GitHub

## Project Structure

```text
Used-Car-Depreciation-Calculator/
│
├── src/
│   ├── app.py
│   ├── predict.py
│   ├── train_model.py
│   ├── best_car_price_model.pkl
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   └── static/
│       └── style.css
│
├── assets/
│   ├── data/
│   │   └── car data.csv
│   │
│   └── notebooks/
│       └── The_Used_Car_Depreciation_Calculator.ipynb
│
├── tests/
│   └── test_data.csv
│
├── requirements.txt
├── Procfile
├── README.md
└── .gitignore
```

## How to Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Used-Car-Depreciation-Calculator.git
```

Move into the project folder:

```bash
cd Used-Car-Depreciation-Calculator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Flask app:

```bash
python src/app.py
```

Open in browser:

```text
http://127.0.0.1:5000
```

## Deployment on Render

Render start command:

```bash
gunicorn src.app:app
```

Build command:

```bash
pip install -r requirements.txt
```

The `Procfile` contains:

```text
web: gunicorn src.app:app
```

## Output

The web app displays:

- Predicted resale price
- Current showroom price
- Depreciation amount
- Depreciation percentage
- Vehicle age
- Bar chart comparing showroom price and predicted resale price

## Live Demo

```
https://used-car-depreciation-calculator.onrender.com/
```
