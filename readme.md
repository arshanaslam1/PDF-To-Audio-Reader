This project made by Arshan Aslam (bc180202497).


before run this project Setup mail server for reset password. (only use gmail address for set backend mail server)
Open file:
file:///Test_phase_django/Test_phase_django/setting.py
# Email server setup for gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_USE_TLS = True
# BY USEING SET ENVIRMENT VARIBALE
EMAIL_HOST_USER = 'xxxxxxxxx@gmail.com'
EMAIL_HOST_PASSWORD = 'xxxxxx'
# EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')


SuperUser:
username: root
email: contact@arshanaslam.me
password: root



User:
username: arshanaslam1
email: arshan.aslam94@gmail.com
password: Dell786.

You can also create new user and reset password of these users.