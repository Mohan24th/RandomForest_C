#  Income Prediction Using Random Forest Classifier

##  Project Overview

This project predicts whether a person's annual income exceeds $50K using Machine Learning.

The model is built using the Random Forest Classifier algorithm and deployed with Streamlit for an interactive user experience.

---

#  Features

- Data preprocessing and cleaning
- Exploratory Data Analysis (EDA)
- Feature engineering
- One-hot encoding
- Correlation heatmap visualization
- Random Forest Classification
- Hyperparameter tuning using GridSearchCV
- Feature importance analysis
- Decision tree visualization
- Streamlit frontend deployment

---

#  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

#  Dataset

Dataset used:
Adult Income Dataset

The dataset contains:
- Age
- Education
- Occupation
- Workclass
- Gender
- Marital Status
- Hours per Week
- Income Category

---

#  Machine Learning Model

Algorithm Used:
## Random Forest Classifier

Why Random Forest?
- Handles large datasets effectively
- Works well with categorical data
- Reduces overfitting
- Provides feature importance

---

#  Model Evaluation

Metrics Used:
- Accuracy Score
- Confusion Matrix
- Classification Report

---

#  Tree Visualization

The project includes visualization of individual trees inside the Random Forest model using:

```python
tree.plot_tree()
```

---

#  Streamlit Application

The Streamlit app allows users to:
- Enter personal details
- Predict income category
- View prediction confidence
- Get user-friendly insights

---

#  Run the Project

## Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
```

## Run Streamlit App

```bash
streamlit run app.py
```

---

#  Project Structure

```text
project/
│
├── app.py
├── adult.csv
├── income_model.pkl
├── model_columns.pkl
├── RandomForestClassifier.ipynb
├── random_forest_tree.png
├── README.md
```

---

#  Future Improvements

- Add SHAP explanations
- Improve frontend UI
- Add prediction history
- Deploy on Render or Streamlit Cloud
- Add user authentication

---

# 👨‍💻 Author

Developed as a Machine Learning project using Random Forest Classification and Streamlit deployment.
