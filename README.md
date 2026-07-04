# 💸 AI-Powered Mobile Money Fraud Detection

An end-to-end Machine Learning project that detects fraudulent mobile money transactions using advanced classification techniques. This project includes data preprocessing, exploratory data analysis, model training, evaluation, and a Streamlit web application for real-time fraud prediction.

---

## 🚀 Features

* 📊 Exploratory Data Analysis (EDA)
* 🧹 Data Cleaning & Preprocessing
* 🤖 Machine Learning-Based Fraud Detection
* 📈 Model Performance Evaluation
* ⚡ Real-Time Fraud Prediction
* 🌐 Interactive Streamlit Web Application
* 💾 Model & Scaler Serialization using Pickle

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn
* **Visualization:** Matplotlib, Seaborn
* **Web Framework:** Streamlit
* **Model Saving:** Pickle
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
AI-Powered-Mobile-Money-Fraud-Detection/
│── app.py
│── fraud_model.pkl
│── scaler.pkl
│── requirements.txt
│── README.md
│── notebook.ipynb
│── dataset.csv
```

---

## 📊 Dataset

The dataset contains mobile money transaction records with features such as transaction type, amount, balances before and after the transaction, and a target variable indicating whether a transaction is fraudulent.

---

## 🔄 Workflow

1. Load the dataset.
2. Perform data cleaning and preprocessing.
3. Conduct exploratory data analysis (EDA).
4. Split the dataset into training and testing sets.
5. Train the Machine Learning model.
6. Evaluate model performance.
7. Save the trained model and scaler.
8. Deploy the model using Streamlit.

---

## 📈 Model Performance

| Metric                | Score      |
| --------------------- | ---------- |
| **Accuracy**          | **99.94%** |
| **Precision (Fraud)** | **75%**    |
| **Recall (Fraud)**    | **68%**    |
| **F1-Score (Fraud)**  | **72%**    |

### Highlights

* ✅ Achieved **99.94%** overall accuracy.
* ✅ Successfully detects fraudulent mobile money transactions.
* ✅ Evaluated using Accuracy, Precision, Recall, and F1-Score.
* ✅ Built for handling highly imbalanced fraud detection datasets.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 💻 Application

The Streamlit application allows users to:

* Enter transaction details.
* Predict whether a transaction is **Fraud** or **Not Fraud**.
* Receive instant prediction results.
* Experience a clean and interactive user interface.

---

## 👨‍💻 Author

**Prem Chougule**

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub. Your support helps motivate further improvements and future AI/ML projects.
