from django.contrib.auth.models import User
import json,requests
from health.models import EmployeeDevice,HealthReport

def load_data():
    devices = EmployeeDevice.objects.all()
    api_url = "https://api.thingspeak.com/channels/{}/feeds.json?api_key=9W11ZVQ6QGOZU5B0&results=15"
    for device_obj in devices:
        HealthReport.objects.filter(device=device_obj).delete()
        health_url = api_url.format(device_obj.device)
        r = requests.get(health_url, allow_redirects=True)
        x = json.loads(r.content)
        for i in range(len(x["feeds"])):
            health_record_obj = HealthReport()
            health_record_obj.device = device_obj
            health_record_obj.temprature = x["feeds"][i]["field1"]
            health_record_obj.glucose = x["feeds"][i]["field2"]
            health_record_obj.pulse = x["feeds"][i]["field3"]
            health_record_obj.created_time = x["feeds"][i]["created_at"]
            health_record_obj.save()

