from health.models import EmployeeDevice,HealthReport
from django.conf import settings
from django.core.mail import send_mail
def predict_temp_n_send_email(temperature,user):
    if temperature < 95:
        msg =  "hello {}, your are suffering from  hypothermia.".format(user.username)
    elif 95 < temperature < 99:
        msg =  "hello {}, your health report is normal based on your body temperature.".format(user.username)
    else:
        msg = "hello {}, your health report is fever.".format(user.username)
    subject = "Health report based on temperature level"
    send_mail(subject,msg,settings.EMAIL_HOST_USER,[user.email])
def predict_glucose_n_send_email(glucose,user):
    if glucose < 140:
        msg = "hello {}, your health report is normal based on your glucose level.".format(user.username)
    elif 140 < glucose < 199:
        msg = "hello {}, your health report is prediabetice.".format(user.username)
    else :
        msg = "hello {}, your health report is diabetics.".format(user.username)
    subject = "Health report based on glucose level"
    send_mail(subject, msg, settings.EMAIL_HOST_USER, [user.email])
def predict_health():
    devices = EmployeeDevice.objects.all()
    for device_obj in devices:
        health_data=HealthReport.objects.filter(device=device_obj)
        counter=0
        avg_temp = 0
        avg_glucose = 0
        avg_pulse = 0
        for health_data in health_data :
            counter+=1
            avg_temp+=health_data.temprature
            avg_glucose+=health_data.glucose
            avg_pulse+=health_data.pulse

        if counter > 0:
            avg_temp=avg_temp/counter
            avg_pulse = avg_pulse /counter
            avg_glucose = avg_glucose /counter

            print(avg_glucose,avg_temp)
            predict_glucose_n_send_email(avg_glucose,device_obj.user)
            predict_temp_n_send_email(avg_temp, device_obj.user)

