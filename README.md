# 🎯 Job Acceptance Prediction System

A Machine Learning-based HR Analytics application that predicts whether a candidate is likely to accept a job offer based on academic performance, technical skills, interview scores, work experience, and recruitment-related factors.

---

## 📌 Project Overview

Recruitment teams often struggle with offer dropouts and unpredictable hiring outcomes. This project analyzes candidate data and builds a predictive machine learning model to estimate job offer acceptance while identifying the key factors influencing candidate decisions.

---

## 🚀 Key Features

- Predict job offer acceptance using Machine Learning
- Comprehensive Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Interactive Streamlit Dashboard
- HR Analytics & KPI Visualization
- Model Performance Comparison
- Correlation & Feature Analysis

---

# 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Dashboard | Streamlit |
| Database (Optional) | MySQL |
| IDE | VS Code, Jupyter Notebook |

---

# 📂 Dataset

- **Records:** 50,000 Candidates
- Real-world HR recruitment dataset
- Includes:
  - Academic Performance
  - Technical Skills
  - Certifications
  - Interview Scores
  - Work Experience
  - Company Tier
  - Placement Status

The dataset intentionally contains:

- Missing Values
- Inconsistent Categories
- Duplicate-like Records
- Noisy Data

to simulate real-world recruitment scenarios.

---

# 📊 Project Workflow

```
Data Collection
        │
        ▼
Data Understanding
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Exploratory Data Analysis (EDA)
        │
        ▼
Feature Engineering
        │
        ▼
Machine Learning Modeling
        │
        ▼
Model Evaluation
        │
        ▼
Streamlit Dashboard
```

---

# 🧹 Data Preprocessing

- Missing Value Handling
- Duplicate Removal
- Label Encoding
- One-Hot Encoding
- Feature Scaling
- Data Validation
- Data Normalization
- SMOTE for Class Balancing

---

# 📈 Exploratory Data Analysis

Performed detailed EDA to understand recruitment trends:

- Acceptance Rate by Company Tier
- Experience vs Placement
- Competition Level Analysis
- Skills Match vs Interview Score
- Correlation Heatmap
- Candidate Performance Analysis

---

# ⚙️ Feature Engineering

Created meaningful business features such as:

- Experience Category
- Academic Performance Band
- Skills Match Level
- Interview Performance Category
- Placement Probability Indicators

---

# 🤖 Machine Learning Models

The project uses supervised machine learning classification models.

| Model | Purpose |
|--------|----------|
| Logistic Regression | Baseline Classification |
| Decision Tree | Rule-Based Prediction |
| Random Forest | Ensemble Learning (Best Model) |

---

## 📊 Model Performance

Three supervised machine learning classification models were trained and evaluated to predict whether a candidate would accept or reject a job offer.

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------:|----------:|--------:|---------:|---------:|
| Logistic Regression | **85.69%** | 72.12% | **85.93%** | 78.42% | 85.76% |
| Decision Tree | 83.74% | 71.81% | 76.21% | 73.95% | 81.61% |
| Random Forest ⭐ | **89.39%** | **82.80%** | 81.98% | **82.38%** | **87.29%** |

### 📈 Model Accuracy Comparison

| Model | Training Accuracy | Testing Accuracy |
|-------|------------------:|-----------------:|
| Logistic Regression | 87.55% | 85.69% |
| Decision Tree | 100.00% | 83.74% |
| Random Forest | 100.00% | **89.39%** |

> **Observation:**  
> - Logistic Regression shows good generalization with similar training and testing accuracy.
> - Decision Tree achieved **100% training accuracy**, indicating **overfitting**, as its testing accuracy dropped to **83.74%**.
> - Random Forest also achieved **100% training accuracy**, but significantly improved generalization with the highest testing accuracy of **89.39%**.

---

## 🏆 Best Performing Model

**Random Forest Classifier** achieved the best overall performance across all evaluation metrics.

- ✅ **Accuracy:** 89.39%
- ✅ **Precision:** 82.80%
- ✅ **Recall:** 81.98%
- ✅ **F1-Score:** 82.38%
- ✅ **ROC-AUC:** 87.29%

The **Random Forest** model was selected as the final model because it achieved the highest testing accuracy while maintaining the best balance between precision, recall, F1-score, and ROC-AUC, making it the most reliable model for job offer acceptance prediction.
---

## 📈 Key Insights

- Interview performance has a strong influence on job acceptance.
- Higher skills match percentage increases the likelihood of placement.
- Candidates with more relevant experience have better acceptance rates.
- Company tier has only a minor impact compared to candidate skills and interview performance.
- Feature engineering significantly improved model performance.
- Random Forest outperformed Logistic Regression and Decision Tree on overall evaluation metrics.

---

# 📈 Dashboard KPIs

The Streamlit dashboard displays:

- Total Candidates
- Placement Rate
- Job Acceptance Rate
- Average Interview Score
- Average Skills Match
- Offer Dropout Rate
- High-Risk Candidate Percentage

---

# 💼 Business Use Cases

- Predict job offer acceptance probability
- Reduce hiring cycle time
- Identify high-risk candidates
- Improve recruitment strategy
- Support HR decision-making
- Analyze placement trends

---

# 📁 Project Structure

```
Job-Application-Prediction/
│
├── Data/
├── Models/
├── Notebook/
├── screenshots/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Dhanyaa-shree/Job-Application-Prediction.git
```

Navigate to the project

```bash
cd Job-Application-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# 🎯 Results

- Cleaned and preprocessed HR dataset
- Engineered meaningful recruitment features
- Built multiple classification models
- Random Forest achieved the best performance
- Generated actionable HR insights through analytics dashboards

---

# 👩‍💻 Author

**Dhanyaa Shree**

GitHub: https://github.com/Dhanyaa-shree

---

## ⭐ If you found this project useful, consider giving it a star!
