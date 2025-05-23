from alerts import send_sms_alert

# Simulate an intentional error
try:
    raise Exception("🔥 Simulated failure in Sci-Tech thread pipeline")
except Exception as e:
    send_sms_alert("🚨 Test Alert", str(e))
