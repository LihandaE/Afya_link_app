import africastalking

# Initialize SDK
africastalking.initialize(
    username="sandbox",  # replace with your app username in production
    api_key="YOUR_API_KEY"
)

sms = africastalking.SMS


def send_sms(phone, message):

    try:
        response = sms.send(message, [phone])
        return response

    except Exception as e:
        print("SMS Error:", str(e))