# News Articles Share Prediction using Machine Learning

---


## Project Overview

### Business Overview

Our project aims to predict the number of shares news articles will receive on various online platforms. News agencies, bloggers, and content creators are always interested in understanding how popular their articles will be. Predicting the number of shares can help them tailor their content and promotional strategies.

### Aim

To predict the number of shares news articles will receive using machine learning algorithms based on various article attributes.

### Data Description

The dataset comprises news articles and their associated attributes, such as title, text, publication date, keywords, and more. These attributes can be used to predict the article's shareability.

## Tech Stack

- **Language**: Python
- **Libraries**: pandas, numpy, scikit-learn, nltk, matplotlib, seaborn

## Approach

1. **Data Collection**
   - Gathered a dataset of news articles with attributes.
2. **Data Preprocessing**
   - Text cleaning
   - Feature extraction
   - Handling missing data
   - Categorical Data Cleaning
   - Using Regex Library
   - Univariate Data Analysis
   - Multivariate Data Analysis
   - Outlier Treatment
   - Feature Extraction
   - Text Data Processing
   - Parts of Speech Tagging
   - Count Vectorization and N-grams
3. **Exploratory Data Analysis (EDA)**
   - Understand data distributions
   - Identify correlations
4. **Feature Engineering**
   - Create new features from existing data
5. **Machine Learning Models**
   - Build and train machine learning models to predict shares.
   - Random Forest Regressor
6. **Model Evaluation**
   - Evaluate model performance using metrics such as Mean Absolute Error (MAE), R2 Squared and Root Mean Squared Error (RMSE).
7. **Model Deployment**
   - APIs
   - Web Application Development using FastAPI
   - Render Deployment
   
Once you unzip the modular_code.zip file, you can find the following folders within it.



1. The input folder contains the raw data that we have for analysis. In our case, it
   contains Pune Real Estate Data.xlsx
2. The ML_pipeline is a folder that contains all the functions put into different python
   files, which are appropriately named. The engine.py script then calls these
   python functions to run the steps in one go. It can be used to train the model or
   use the web application as mentioned in the readme.md file.
3. The output folder contains the models and training data python objects saved for
   inference while training the model through engine.py.
4. The lib folder is a reference folder, and it contains the original ipython notebooks
   we saw in the lectures, it has its own system with data and models as used in the
   videos.
5. The FastAPI for the model can be accessed by running the app.py script and
   Procfile along with app.py, saved voting regressor model, propertyvariables.py
   and requirements.txt will be used to deploy the application on Heroku.
6. The requirements.txt file has all the required libraries with respective versions.
   Kindly install the file by using the command pip install -r requirements.txt
7. All the instructions for running the code are present in readme.md file
