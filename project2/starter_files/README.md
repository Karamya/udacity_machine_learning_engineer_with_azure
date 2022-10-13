*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.


# End-to-End Machine Learning Pipeline with AzureML 
In the second part of the project assigment, we are building an end-to-end machine learning pipeline using Microsoft Azure on a sample bank marketing dataset. 
We start with registering the dataset on Azure blob storage and using AutoML functionalities provided by Microsoft Azure, we train an automl model using a predefined compute cluster of choice. Once the AutoML model is trained, we register the best performing model and deploy it by creating an http endpoint and consuming from it. Swagger UI is used to visually render documentation for the API endpoint, which can then be used to test the endpoint for prediction as well as for benchmarking. 
Again, we repeat the whole process of automating the pipeline using python SDK in a jupyter notebook. AutoML was used to train the pipeline and the best performing model is registered and deployed on Microsoft Azure by creating a rest endpoint from the AutoML pipeline. 


## Architectural Diagram
Here is the architecture diagram of the whole process
![architecture](screenshots/azure_ml_pipeline.png)

## Key Steps
### Authentication
Login using Azure CLI and create a service principal
![login](screenshots/Screenshot%202022-10-12%20at%2014.13.52.png)
Associating the workspace with service principal is successful without any errors
![login](screenshots/Screenshot%202022-10-12%20at%2014.15.04.png)
![successful](screenshots/Screenshot%202022-10-12%20at%2016.57.34.png)
### Dataset
Create a data asset by uploading the data on a blob storage
![data](screenshots/Screenshot%202022-10-12%20at%2017.34.44.png)
### AutoML
create and run AutoML on the uploaded dataset successfully
![AutoML successful](screenshots/Screenshot%202022-10-13%20at%2011.03.21.png)
Choose the best performing model from the AutoML runs
![best performing model](screenshots/Screenshot%202022-10-13%20at%2011.03.48.png)
Deploy the best performing model and make sure the rest endpoint is present and application insights are enabled
![deploy and application insights](screenshots/Screenshot%202022-10-13%20at%2013.19.30.png)
Download the swagger.json file and consume the deployed model using swagger
![swagger1](screenshots/Screenshot%202022-10-13%20at%2013.20.09.png)
Swagger runs on the localhost showing the documentation for HTTP API methods 
![swagger1](screenshots/Screenshot%202022-10-13%20at%2013.38.33.png)
Modify the scoring_uri and key to execute the endpoint and get the predictions
![endpoint predictions](screenshots/Screenshot%202022-10-13%20at%2013.54.04.png)
Benchmark the model for load tests using the benchmark.sh script
![benchmark load test](screenshots/Screenshot%202022-10-13%20at%2013.56.55.png)
## Screen Recording
https://youtu.be/mNW8kbp2-6I

[![youtube_video](screenshots/azure_ml_pipeline.png)](https://youtu.be/mNW8kbp2-6I)