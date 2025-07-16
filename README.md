# Machine-Learning-Model-for-Predicting-the-Impact-of-Drug-Abuse-on-Students'-Academic-Performance
A machine learning web app that predicts the impact of drug abuse on students' academic performance. I built it using Flask, HTML, CSS, and JavaScript, using a Random Forest model for accurate predictions.
## Overview.  
This project presents a machine learning-based predictive system designed to assess the impact of drug abuse on students’ academic performance. By analyzing a structured dataset containing academic records (e.g., GPA, attendance), behavioral data, and substance use patterns, the model identifies at-risk students and predicts academic outcomes.  
It considers key factors such as alcohol and drug use, peer influence, family support, socioeconomic status, and reasons for substance use. The goal is to provide early warning insights for educators, counselors, and policymakers to enable timely interventions and promote academic success.  

# Data Visualization.  

<img width="805" height="432" alt="image" src="https://github.com/user-attachments/assets/9e70731c-5124-48bb-8fda-b2d7b3ab8a7f" />   

  
- Students who use Alcohol, Marijuana, and Cocaine tend to have a higher impact on academics.  
- Students who don’t use drugs ("None") have better academic performance.  

## Implementation Architecture.  
The implementation architecture of this project is structured into five core layers: the data layer, machine learning model layer, backend layer, frontend layer, and deployment layer.
The process began with the data layer, where I collected the dataset directly from students in higher institutions using Google Forms. The dataset includes features such as age, gender, drug type, frequency of use, GPA, and academic impact. I performed preprocessing steps, including handling missing values, encoding categorical variables, and scaling numerical features. The dataset was then split into 80% for training and 20% for testing.
In the machine learning model layer, I evaluated multiple algorithms, including Logistic Regression, Random Forest, SVM, KNN, and Linear Regression, to identify the best-performing model. The Random Forest algorithm yielded the highest accuracy and stability, making it the optimal choice. I further fine-tuned its performance through hyperparameter tuning and saved the trained model using joblib for deployment.
For the backend layer, I used Flask to manage API endpoints, process user inputs, and return prediction results. In the frontend layer, I developed a clean and user-friendly interface using HTML, CSS, and JavaScript, allowing users to input student information and instantly receive academic risk predictions.
Finally, in the deployment layer, I integrated all components into a fully functional web-based system that enables practical use of the model for early intervention and academic performance monitoring.  
## Model Performance Evaluation.  

To determine the most effective algorithm for predicting the impact of drug abuse on academic performance, I evaluated multiple machine learning models. The Random Forest classifier outperformed all other models, achieving 100% accuracy, making it the most suitable for this task. It was followed by Logistic Regression, which achieved 92% accuracy. In comparison, Support Vector Machine (SVM) and K-Nearest Neighbors (KNN) recorded lower accuracies of 80% and 76%, respectively. The Linear Regression model, being regression-based, was found unsuitable for this classification problem and was not considered further for deployment.  

<img width="456" height="356" alt="image" src="https://github.com/user-attachments/assets/296c62f6-9544-4b20-95bf-81d8b301babc" />  

## Presentation of Results.  

<img width="636" height="638" alt="image" src="https://github.com/user-attachments/assets/bc6ee007-5fd3-4a50-ae35-67b81fa07312" />  

## Contribution
In this research, I introduced a machine learning-based predictive system designed to identify students at risk of academic decline due to drug abuse. By analyzing key factors such as drug use frequency, socioeconomic status, and family support, the model provides a comprehensive and automated approach to assessing the impact of substance use on academic performance. It facilitates early intervention by educators, counselors, and policymakers.
The project also contributes a structured dataset derived from primary data collected via Google Forms, enhancing the reliability and contextual relevance of the analysis. Furthermore, the system is implemented as a web-based application using Flask, HTML, CSS, and JavaScript, ensuring usability and accessibility for educational institutions.
This work supports further research in behavioral analytics, rehabilitation strategies, and predictive academic monitoring, offering practical insights for evidence-based decision-making.
## Future Research
Future studies can explore advanced models like deep learning and ensemble learning to enhance the model’s robustness and interpretability. Expanding the dataset to include students from diverse backgrounds and institutions will improve generalizability. Integrating additional factors such as mental health, social influence, and extracurricular activities can provide deeper insights.  
## How to Run the Flask App.

- Clone the Repository.
- Install dependencies. Make sure you have Python installed (Python 3.7+ is recommended), then install all required packages.
- Run the Flask app using python app.py in your terminal.
- Open a browser, and type this address http://127.0.0.1:5000/ to interact with the system.
