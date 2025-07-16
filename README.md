# Machine-Learning-Model-for-Predicting-the-Impact-of-Drug-Abuse-on-Students'-Academic-Performance
A machine learning web app that predicts the impact of drug abuse on students' academic performance. I built it using Flask, HTML, CSS, and JavaScript, using a Random Forest model for accurate predictions.
## Overview.  
This project presents a machine learning-based predictive system designed to assess the impact of drug abuse on students’ academic performance. By analyzing a structured dataset comprising academic records (e.g., GPA, attendance), behavioral data, and substance use patterns, the model identifies at-risk students and predicts academic outcomes. It considers key factors such as alcohol and drug use, peer influence, family support, socioeconomic status, and reasons for substance use. The goal is to provide early warning insights for educators, counselors, and policymakers to support timely interventions and promote academic success.  
# Data Visualization.  

<img width="805" height="432" alt="image" src="https://github.com/user-attachments/assets/9e70731c-5124-48bb-8fda-b2d7b3ab8a7f" />   

- Students who use Alcohol, Marijuana, and Cocaine tend to have a higher impact on academics.  
- Students who don’t use drugs ("None") have better academic performance.  

## Implementation Architecture.  
The implementation architecture of this project is structured into five core layers: the data layer, the machine learning model layer, backend layer, frontend layer, and deployment layer. I began by preparing the data layer, where I collected the dataset used to train the model directly from students in higher institutions using Google Forms. The dataset contains features such as age, gender, drug type, frequency of use, GPA, and academic impact. I performed preprocessing steps, including handling missing values, encoding categorical variables, and scaling numerical features. I then split the dataset into 80% for training and 20% for testing.  
In the machine learning model layer, I evaluated multiple algorithms Logistic Regression, Random Forest, SVM, KNN, and Linear Regression to determine the best-performing model. Random Forest produced the highest accuracy and stability, so I selected it as the final model. I also performed hyperparameter tuning to further optimize its performance and saved the trained model using joblib for deployment.  
Next, I developed the backend using Flask to manage API endpoints, handle user input, and return prediction results. For the frontend, I built a clean and user-friendly interface using HTML, CSS, and JavaScript that allows users to input student information and instantly view academic risk predictions. Finally, I brought all components together in a web-based deployment that enables practical use of the model for early intervention and academic performance monitoring.  

## Model Performance Evaluation.  

To determine the most effective algorithm for predicting the impact of drug abuse on academic performance, I evaluated multiple machine learning models. The Random Forest classifier outperformed all other models, achieving 100% accuracy, making it the most suitable for this task. It was followed by Logistic Regression, which achieved 92% accuracy. In comparison, Support Vector Machine (SVM) and K-Nearest Neighbors (KNN) recorded lower accuracies of 80% and 76%, respectively. The Linear Regression model, being regression-based, was found unsuitable for this classification problem and was not considered further for deployment.  

<img width="456" height="356" alt="image" src="https://github.com/user-attachments/assets/296c62f6-9544-4b20-95bf-81d8b301babc" />  

## Presentation of Results.  

<img width="636" height="638" alt="image" src="https://github.com/user-attachments/assets/bc6ee007-5fd3-4a50-ae35-67b81fa07312" />  

## Contribution
In this research, I introduced a machine learning-based predictive system that helps identify students at risk of academic decline due to drug abuse. By analyzing various factors such as drug frequency, socioeconomic status, and family support, the model offers a comprehensive and automated way to assess the impact of substance use on academic performance. It enables early intervention by educators, counselors, and policymakers. The project also contributes a structured dataset derived from primary data (collected via Google Forms), enhancing the reliability of the analysis. Also, the implementation as a web-based application using Flask, HTML, CSS, and JavaScript ensures usability and accessibility for educational institutions. This work supports further research in behavioral analytics, rehabilitation strategies, and predictive academic monitoring, offering practical insights for evidence-based decision-making.

## Future Research
Future studies can explore advanced models like deep learning and ensemble learning to enhance the model’s robustness and interpretability. Expanding the dataset to include students from diverse backgrounds and institutions will improve generalizability. Integrating additional factors such as mental health, social influence, and extracurricular activities can provide deeper insights.
## How to Run the Flask App.

- Clone the Repository.
- Install dependencies. Make sure you have Python installed (Python 3.7+ is recommended), then install all required packages.
- Run the Flask app using python app.py in your terminal.
- Open a browser, and type this address http://127.0.0.1:5000/ to interact with the system.
