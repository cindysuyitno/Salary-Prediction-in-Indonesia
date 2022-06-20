# Data Science Project: Salary Prediction in Indonesia
This is the salary prediction model based on Indonesia. The salary predicted is fitted with machine learning model with job, province, and years of experience as predictors. 

Data Collection:
  - Web scrapped Karir.com and Glints jobsite with more than 9000 data
  - Contains job title, city, salary range, and years of experience range
Data Cleaning:
  - Assigning data to suitable columns
  - Removing null value
Data Modelling:
  - Exploratory Data Analysis: including data visualization to determine which value will be used
  - Regression model fitted: Gradient Boosting Regressor, K Neighbors Regressor, Extra Trees Regressor, Random Forest Regressor, Decision Tree Regressor, Linear  Regression, Lasso, Ridge
  - Three best models will be tuned with the estimator hyperparameters
Web app with Streamlit:
  - The salary prediction will be put in a web app with streamlit
  - Data visualization by matplotlib and geopandas is also shown
