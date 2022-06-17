This project made by Arshan Aslam (bc180202497).

# Requirements 
1. Redis
2. Django 4.0.4
3. Python 3.10


# Step
1. Install redis
2. Make Virtual Environment

    ```python -m venv venv```
    
    ```venv Scripts\activate```


3. Before run this project Setup mail server for reset password. (only use gmail address for set backend mail server)
Open file:

   setting.py
   Email server setup for gmail

   ```EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'```
   
   ```EMAIL_HOST = 'smtp.gmail.com'```
   
   ```EMAIL_PORT = '587'```
   
   ```EMAIL_USE_TLS = True```
   
   ```EMAIL_HOST_USER = 'xxxxxxxxx@gmail.com'```
   
   ```EMAIL_HOST_PASSWORD = 'xxxxxx'```


4. run these commands

    ```pip install -r requirements.txt```

    ```python manage.py migrate```

    ```python manage.py runserver```
    
    ```celery --app=config worker -l INFO --pool=solo```
    
