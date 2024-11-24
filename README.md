# HumanEmotionDetection
A final year group project that detects human emotions using facial expressions with a website to interact with the model.

## Project Description
This project demonstrates a connection between a deep learning model with a website created via Django.
The model predicts human emotions via facial expressions. The model is trained on over 10000+ images which can be found on kaggle. ([LINK](https://www.kaggle.com/datasets/msambare/fer2013))
The approach used for training the model is Transfer learning. A PPT link is attached to understand the whole project in simple terms. 

## Project Explanation
-The repository contains few folders the main one being DKRZ. 
-DKRZ is the main source through which our users will interact with the website. 
![image](https://github.com/user-attachments/assets/0380ff64-33a6-4dd6-8b87-6feb26a4b87d)

-From DKRZ we have an API folder which connects to the backend i.e our model. 
![image](https://github.com/user-attachments/assets/394fcfcb-0c8f-4c5b-b58c-e0671839e5b4)

-We trained the model and saved it in h5 .format.
-We have stored static files like HTML, CSS , JS and few images in the static folder. 
-The connection folder holds the logic to predict our emotion and give the output to our API folder which then passes it on to our DKRZ folder. 

## Running the project. 
To get started clone the repository and open it in VS code or any code editor. You can also directly open the folder path in CMD and type 'python manage.py runserver' and you can interact with our project now.

## Results 
![image](https://github.com/user-attachments/assets/763601f8-86b0-4edb-bc6c-ce3f3c31198c)
![image](https://github.com/user-attachments/assets/55a6f1bc-7b71-4d87-8bf5-13e3df520f90)
![image](https://github.com/user-attachments/assets/3bc10174-fcb5-44ad-94b5-2aa7070f11ec)
