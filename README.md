# Machine-Learning-Model-for-Predicting-the-Impact-of-Drug-Abuse-on-Students'-Academic-Performance
A machine learning web app that predicts the impact of drug abuse on students' academic performance. I built with Flask, HTML, CSS, and JavaScript using a Random Forest model for accurate predictions.
## Overview.  
This project presents a machine learning-based predictive system designed to assess the impact of drug abuse on students’ academic performance. By analyzing a structured dataset comprising academic records (e.g., GPA, attendance), behavioral data, and substance use patterns, the model identifies at-risk students and predicts academic outcomes. It considers key factors such as alcohol and drug use, peer influence, family support, socioeconomic status, and reasons for substance use. The goal is to provide early warning insights for educators, counselors, and policymakers to support timely interventions and promote academic success.  
# Data Visualization.  

<img width="805" height="432" alt="image" src="https://github.com/user-attachments/assets/9e70731c-5124-48bb-8fda-b2d7b3ab8a7f" />   

- Students who use Alcohol, Marijuana, and Cocaine tend to have a higher impact on academics.  
- Students who don’t use drugs ("None") have better academic performance.  
<img width="696" height="400" alt="image" src="https://github.com/user-attachments/assets/7fc80b09-9ff4-432b-9863-375a42426f77" />  
 
### Insight on Gender vs. Drug Use.  
- More males use hard drugs (Cocaine, Marijuana, Heroin) compared to females.    
- Females are more represented in the Alcohol and Tobacco categories.  
 
## Implementation Architecture.  
The implementation architecture of this project is structured into five core layers: the data layer, the machine learning model layer, backend layer, frontend layer, and deployment layer. I began by preparing the data layer, where I collected the dataset used to train the model directly from students in higher institutions using Google Forms. The dataset contains features such as age, gender, drug type, frequency of use, GPA, and academic impact. I performed preprocessing steps, including handling missing values, encoding categorical variables, and scaling numerical features. I then split the dataset into 80% for training and 20% for testing.  
In the machine learning model layer, I evaluated multiple algorithms Logistic Regression, Random Forest, SVM, KNN, and Linear Regression to determine the best-performing model. Random Forest produced the highest accuracy and stability, so I selected it as the final model. I also performed hyperparameter tuning to further optimize its performance and saved the trained model using joblib for deployment.  
Next, I developed the backend using Flask to manage API endpoints, handle user input, and return prediction results. For the frontend, I built a clean and user-friendly interface using HTML, CSS, and JavaScript that allows users to input student information and instantly view academic risk predictions. Finally, I brought all components together in a web-based deployment that enables practical use of the model for early intervention and academic performance monitoring.  
## Performance Evaluation.  
Performance evaluation showed that the Random Forest model was the most suitable, achieving 100% accuracy, followed by Logistic Regression (92%), while SVM (80%) and KNN (76%) performed lower. The Linear Regression model was unsuitable for classification tasks.  

<img width="456" height="356" alt="image" src="https://github.com/user-attachments/assets/296c62f6-9544-4b20-95bf-81d8b301babc" />  

