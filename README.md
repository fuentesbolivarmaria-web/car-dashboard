# 🚗 Car Dashboard

An interactive **data visualization dashboard** built with **Streamlit**, **Plotly**, and **Pandas** to explore and analyze vehicle sales data.  
This project demonstrates skills in data manipulation, visualization, and web app deployment.

---

## 🧭 Project Overview

The goal of this project is to create a simple yet functional **web dashboard** for exploring vehicle listings.  
Users can interactively generate histograms and scatter plots to uncover patterns and trends in the dataset.

The app was developed as part of the **TripleTen Data Science Bootcamp (Sprint 7)** to practice:
- Building and managing virtual environments.
- Developing and deploying a Streamlit web app.
- Creating interactive data visualizations with Plotly.

---

## 🧰 Tech Stack

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)]()  
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)]()  
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)]()  
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)]()  
[![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=black)]()

---

## ⚙️ Features

- 📊 Interactive **histograms** and **scatter plots** built with Plotly.
- 🧮 Data exploration with Pandas.
- 🧱 Clean modular structure with `app.py`, `requirements.txt`, and Jupyter notebook for EDA.
- ☁️ Deployed using **Render** for live web access.

---

## 🚀 How to Run Locally

To run this project on your local machine:

```bash
# Clone this repository
git clone https://github.com/fuentesbolivarmaria-web/car-dashboard.git

# Navigate to the project folder
cd car-dashboard

# Create and activate a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate     # On Mac/Linux
venv\Scripts\activate        # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

