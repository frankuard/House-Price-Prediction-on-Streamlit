# 🏠 House Price Prediction App

A machine learning web app that predicts house prices based on various features like area, number of bedrooms, bathrooms, and more. The app is built using **Streamlit** and powered by a trained **Machine Learning model**.

---

## 📊 Dataset

The dataset contains the following features:

- Area (sq ft)
- Bedrooms
- Bathrooms
- Stories
- Parking
- Main Road
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Preferred Area
- Furnishing Status

### 🎯 Target Variable

- **Price**

---

## 🧠 Models Used

The following regression models were trained and evaluated:

- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor  

### 📈 Best Model

- **Linear Regression**
- R² Score: ~0.65  
- RMSE: ~1.3M  

---

## ⚙️ Feature Engineering

New features were created to improve model performance:

- `area_per_bedroom = area / bedrooms`
- `area_per_bathroom = area / bathrooms`
- `total_rooms = bedrooms + bathrooms + stories`

---

## 🔄 Data Preprocessing

- One-hot encoding for categorical variables  
- Feature scaling using `StandardScaler`  
- Removed unnecessary columns  
- Train-test split (80/20)  


---

## 💻 How It Works

1. User enters house details via the Streamlit UI  
2. Input is converted into numerical format  
3. Feature engineering is applied  
4. The trained model predicts the house price  
5. Result is displayed on the screen  

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/house-price-prediction.git
cd house-price-prediction
```
---

### 2. Install the Required Libraries

```bash
pip install -r requirements.txt
```

---

## 📌 Key Learnings

- Data preprocessing and feature engineering  
- Handling categorical variables  
- Building ML pipelines  
- Model evaluation using RMSE and R²  
- Deploying ML models using Streamlit  

---

## 🔮 Future Improvements

- Will try advanced models (XGBoost, Gradient Boosting)  
- Hyperparameter tuning  
- Improving model accuracy  
- Add visualization and feature importance   

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Streamlit  

---

## 📜 License

This project is open-source and free to use.

---

## 👤 Author

**Roshan Karki**

