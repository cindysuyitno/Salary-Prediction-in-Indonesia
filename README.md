# Data Science Project: Salary Prediction in Indonesia
This is the salary prediction model based in Indonesia, with the predictor of job name, province, and years of experience. This project aims to make businesses able to determine the salary of their employees based on common salaries provided by other businesses in Indonesia. The alternative aim is for employees-to-be to determine their desired salary before going into their career.

# Technologies used
Python (Pandas, Numpy, BeautifulSoup, Matplotlib, Seaborn, Pickle, Streamlit, Geopandas), Google Colab, Chrome Driver

## Table of Content:
### Data Collection:
  - Sources: Karir.com and Glints Jobsites 
  - Web scrapping with more than 9000 data
  - Contains job title, city, salary range, and years of experience range
### Data Cleaning:
  - Assigning data to suitable columns
  - Removing null value
### Data Modelling:
  - Exploratory Data Analysis: including data visualization to determine which value will be used
  - Regression model fitted: Gradient Boosting Regressor, K Neighbors Regressor, Extra Trees Regressor, Random Forest Regressor, Decision Tree Regressor, Linear Regression, Lasso, Ridge
  - The three best models will be tuned with the estimator hyperparameters
### Web app with Streamlit:
  - The salary prediction will be put in a web app with streamlit
  - Data visualization by matplotlib and geopandas is also shown

# Ilustration of Web App:
![alt text](https://github.com/cindysuyitno/Salary-Prediction-in-Indonesia/blob/main/screenshoot1.jpg)
![alt text](https://github.com/cindysuyitno/Salary-Prediction-in-Indonesia/blob/main/screenshoot2.jpg)
![alt text](https://github.com/cindysuyitno/Salary-Prediction-in-Indonesia/blob/main/screenshoot3.jpg)
![alt text](https://github.com/cindysuyitno/Salary-Prediction-in-Indonesia/blob/main/screenshoot4.jpg)

# Comments and Suggestion from Author
From the salary data scrapped from job vacancy websites, the predictor job categories, province categories, and years of experience have been used to predict salary. The model used was Gradient Boosting Regressor with parameter of alpha= 1e-08, learning_rate= 1, max_depth= 1, and n_estimators= 5. The model had achieved a square root mean absolute error of 1527.1, explained variance of 0.52, and R2 score of 0.52. However, it seems that the model hardly took predictors other than years of experience as a significant predictor. This might happen as job and province categories have irregular values (most job and province data lies in the same mean). As the machine learning model needs more data, the model's performance should be examined over time with more data inputted.
