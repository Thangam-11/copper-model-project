

# Industrial Copper Modeling

**Introduction**

Enhance your proficiency in data analysis and machine learning with our "Industrial Copper Modeling" project. In the copper industry, dealing with complex sales and pricing data can be challenging. Our solution employs advanced machine learning techniques to address these challenges, offering regression models for precise pricing predictions and lead classification for better customer targeting. You'll also gain experience in data preprocessing, feature engineering, and web application development using Streamlit, equipping you to solve real-world problems in manufacturing.


**Key Technologies and Skills**
- Python
- Numpy
- Pandas
- Scikit-Learn
- Matplotlib
- Seaborn
- Pickle
- Streamlit

**Features**

**Data Preprocessing:**

- **Data Understanding**: Data Understanding: Identify the types of variables (continuous, categorical) and their distributions. Some rubbish values are present in ‘Material_Reference’ which starts with ‘00000’ value which should be converted into null. Treat reference columns as categorical variables. INDEX may not be useful..

- **Handling Null Values**: The dataset may contain missing values that need to be addressed. The choice of handling these null values, whether through mean, median, or mode imputation, depends on the nature of the data and the specific feature.

- **Encoding and Data **:
  
Encode categorical variables using suitable techniques, such as , label encoding, , based on their nature and relationship with the target variable.
- **Skewness - Feature Scaling**: Skewness is a common challenge in datasets. Identifying skewness in the data is essential, and appropriate data transformations must be applied to mitigate it. One widely-used method is the log transformation, which is particularly effective in addressing high skewness in continuous variables. This transformation helps achieve a more balanced and normally-distributed dataset, which is often a prerequisite for many machine learning algorithms.

- **Outliers Handling**: Outliers can significantly impact model performance. We tackle outliers in our data by using the Interquartile Range (IQR) method. This method involves identifying data points that fall outside the IQR boundaries and then converting them to values that are more in line with the rest of the data. This step aids in producing a more robust and accurate model.

**Exploratory Data Analysis (EDA) and Feature Engineering:**

- **Skewness Visualization**: ToIdentify Skewness in the dataset and treat skewness with appropriate data transformations, such as log transformation(which is best suited to transform target variable-train, predict and then reverse transform it back to original scale eg:dollars), boxcox transformation, or other techniques, to handle high skewness in continuous variables

- **Outlier Visualization**: We identify and rectify outliers by leveraging `Seaborn's Boxplot`. This straightforward visualization aids in pinpointing outlier-rich features. Our chosen remedy is the Interquartile Range (IQR) method, which brings outlier data points into alignment with the rest of the dataset, bolstering its resilience.

**Classification:**

- **Success and Failure Classification**: In our predictive journey, we utilize the 'status' variable, defining 'Won' as Success and 'Lost' as Failure. Data points with status values other than 'Won' and 'Lost' are excluded from our dataset to focus on the core classification task.
  
- **Algorithm Selection**: After thorough evaluation, two contenders,  and Random Forest Classifier, commendable testing accuracy. Upon checking for any overfitting issues in both training and testing, both models exhibit strong performance without overfitting concerns. I choose the Random Forest Classifier for its ability to strike a balance between interpretability and accuracy, ensuring robust performance on unseen data.

- **Hyperparameter Tuning with GridSearchCV and Cross-Validation**: To fine-tune our model and mitigate overfitting, we employ GridSearchCV with cross-validation for hyperparameter tuning. This function allows us to systematically explore multiple parameter values and return the optimal set of parameters. 
`{max_depth=20, max_features='sqrt', min_samples_leaf=1, min_samples_split=2}`

**Regression:**

- **Algorithm Selection**: After thorough evaluation, Random Forest Regressor, demonstrate commendable testing accuracy. Upon checking for any overfitting issues in both training and testing, both models exhibit strong performance without overfitting concerns. I choose the Random Forest Regressor for its ability to strike a balance between interpretability and accuracy, ensuring robust performance on unseen data.

- **Hyperparameter Tuning with GridSearchCV and Cross-Validation**: To fine-tune our model and mitigate overfitting, we employ GridSearchCV with cross-validation for hyperparameter tuning. This function allows us to systematically explore multiple parameter values and return the optimal set of parameters.
`{'max_depth': 20, 'max_features': None, 'min_samples_leaf': 1, 'min_samples_split': 2}`.

- 
**Contributing**

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request.

**Contact**

📧 Email: thangamani1128@gmail.com 

For any further questions or inquiries, feel free to reach out. We are happy to assist you with any queries.
