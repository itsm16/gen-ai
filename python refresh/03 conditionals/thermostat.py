device_status = "active"
temperature = 30

if device_status == "active" and temperature > 35:
    print("High temp.")
elif device_status == "active" and temperature < 35:
    print("Its ok")
else:
    print("Device is offline")