*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# Hear failure prediction

For the capstone project, I went with the default option of predicting heart failures. It is 

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.

## Dataset
Cardiovascular diseases (CVDs) are the number 1 cause of death globally, taking an estimated 17.9 million lives each year, which accounts for 31% of all deaths worlwide.
Heart failure is a common event caused by CVDs and this dataset contains 12 features that can be used to predict mortality by heart failure.

Most cardiovascular diseases can be prevented by addressing behavioural risk factors such as tobacco use, unhealthy diet and obesity, physical inactivity and harmful use of alcohol using population-wide strategies.

People with cardiovascular disease or who are at high cardiovascular risk (due to the presence of one or more risk factors such as hypertension, diabetes, hyperlipidaemia or already established disease) need early detection and management wherein a machine learning model can be of great help.

### Overview
The data that I am using is a kaggle dataset of clinical records of heart failures and the objective is to predict whether the given data leads to the event of death. 
Some of the features of the dataset are,
- **age** - age of te patient
- **anaemina** - Decrease of red blood cells or hemoglobin (boolean)
- **creatinin_phosphokinase** - Level of the CPK enzyme in the blood (mcg/L)
- **diabetes** - is the patient diabetic (boolean)
- **ejection_fraction** - percentage of blood leaving the heart at each contraction (percentage)
- **high_blood_pressure** - if the patient has hypertension (boolean)
- **platelets** - platelets in the blood (kiloplatelets/mL)
- **serum_creatinine** - level of serum creatinine in the blood (mg/dL)
- **serum_sodium** - Level of serum sodium in the blood (mEq/L)
- **sex** - male of female (binary)

Target - "DEATH_EVENT" 


### Task
Some of the features of the dataset are,
- **age** - age of te patient
- **anaemina** - Decrease of red blood cells or hemoglobin (boolean)
- **creatinin_phosphokinase** - Level of the CPK enzyme in the blood (mcg/L)
- **diabetes** - is the patient diabetic (boolean)
- **ejection_fraction** - percentage of blood leaving the heart at each contraction (percentage)
- **high_blood_pressure** - if the patient has hypertension (boolean)
- **platelets** - platelets in the blood (kiloplatelets/mL)
- **serum_creatinine** - level of serum creatinine in the blood (mg/dL)
- **serum_sodium** - Level of serum sodium in the blood (mEq/L)
- **sex** - male of female (binary)

The task or objective of the problem is to find if the patient will die or not based on the available features
Target - "DEATH_EVENT" 

### Access
The data was uploaded to our workspace as Azure blobstorage of tabular datatype. 

## Automated ML

Here is an overview of AutoML settings, 
- **experiment_timeout_minutes**: set to 20 minutes. The experiment will timeout after after this period of time to avoid incurring additional expense.
- **max_concurrent_iterations**: set to 4. The max number of concurrent iterations that can be run on the nodes in the compute cluster.
- **primary_metric** : set to 'AUC_weighted' because this is an imbalanced dataset
- **n_cross_validations**: set to 4 fold cross validation.


Here is an overview of AutoML Configuration
- **compute_target**: set to CPU compute cluster name defined above.
- **task**: set to 'classification' because our target is to predict how many upvotes a comment will get.
- **training_data**: reddit upvotes dataset.
- **label_column_name**: set to 'DEATH_EVENT' which is our target.
- **enable_early_stopping**: enabled to terminate the experiment if the accuracy score does not improveme over time, thus avoiding unnecessary costs.
- **featurization** = set to 'auto' so Azure ML will automatically handle featurization and clean the dataset.
- **debug_log**: errors will be logged into 'automl_errors.log'.


### Results
![Screenshot 2022-11-11 at 00 26 09](https://user-images.githubusercontent.com/19229613/201227063-1e53c3a4-e792-46b4-b3d8-524665eff151.png)
## Run Details

- Tree based models (both Random Forest and gradient boosted trees) performed quite well. In almost all the models we have either StandardScaling or MinMaxScaling on the dataset
- Ensembling using a simple voting performs much better than stacking ensemble. 

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.
![Screenshot 2022-11-11 at 00 27 53](https://user-images.githubusercontent.com/19229613/201227281-31a96f60-578c-449c-a4ea-29fe8731cdb5.png)

The best model is a voting ensemble model with an AUC weighted score of 0.92110
![Screenshot 2022-11-11 at 00 29 47](https://user-images.githubusercontent.com/19229613/201227488-d04c40aa-2edc-449b-9d53-472690094971.png)

The parameters of the best model are
![Screenshot 2022-11-11 at 00 31 31](https://user-images.githubusercontent.com/19229613/201227681-f11e3087-6afd-45b1-95f5-79fa55ad5dff.png)


## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search
For this experiment, I went with a simple Logistic Regression model from scikit-learn on a dataset preprocessed using a StandardScaler. I chose this model as it is a bit easier to experiment. Since the data is imbalanced, I set the class_weight to 'balanced' which will automatically weight different categories based on the occurences. 

For parameter sampling, I choose random parameter sampling and sample two hyperparameters C (regularization strength) and max_iter (maximum number of iterations) in the ranges of -0.01 to 1.0 and 50 to 150 respectively.


### Results
The best performing model had a ROC_AUC_score of around 0.72 with C of around 0.00419 and max_iter to 100 
![Screenshot 2022-11-11 at 00 36 09](https://user-images.githubusercontent.com/19229613/201228237-bfa21fa9-0d33-4a63-aebb-8f651aac5668.png)

The performance can be improved by going through a bigger searchspace and using gradient boosted trees.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.
The best performing model was a voting ensemble from AutoML and this was deployed. 
<img width="2535" alt="Screenshot 2022-11-10 at 18 55 23" src="https://user-images.githubusercontent.com/19229613/201228747-fb530de8-89df-4fad-b1e9-584b2d21e158.png">


## Screen Recording

![](https://youtu.be/uhN5C-WRTbQ)

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
