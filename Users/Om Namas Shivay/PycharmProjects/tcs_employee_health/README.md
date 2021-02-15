# How to install and use application

# Step1
    Clone  code in your system
# Step2
    Create virual environment and install dependency by running below command
    
    pip install -r requirements.txt
# Step3
    Create a Database and update database datails in tcs_employee_health/setting.py
    Also update email server settings in tcs_employee_health/setting.py
    by providing your  EMAIL_HOST_USER and EMAIL_HOST_PASSWORD 
# Step4
    Run below commands to migrate data and runsrver
    
    python manage.py migrate
    python manage.py runserver

    Now check http://127.0.0.1:8000/ is running

# Step5
    Create superuser and login to admin(http://127.0.0.1:8000/admin)
    
    python manage.py createsuperuser
# Step6 
    Ask employees to register(http://127.0.0.1:8000/register)
# Step7
     Valid device list [1294209]
     Assign employee device from above list
#Step8
    Load health records in database by using Below command 
    
    python manage.py shell
    import json,requests
    from health.models import EmployeeDevice,HealthReport
    load_data()

#Step9 
    To predict and send email run below commands
    
    python manage.py shell
    #import these modules 
    from health.models import EmployeeDevice,HealthReport
    from django.conf import settings
    from django.core.mail import send_mail
    predict_n_send mail 

For any query :
You can contact  me on yogendrayadav0199@gmail.com