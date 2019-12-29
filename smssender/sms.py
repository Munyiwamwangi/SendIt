# Import the AfricasTalking SDK into your app
import africastalking

# Create your credentials
username = "testjoe"
apikey = "065ce0c2c30f8bc4a3b038a2935b59b6b1baac0e8fd4a5d3103f7fb6149773ea"

# Initialize the SDK
africastalking.initialize(username, apikey)

# Get the SMS service
sms = africastalking.SMS

# Define some options that we will use to send the SMS
recipients = ['+254719828205']
message = 'I\'m all cool at night and I work all day at day'
sender = '33334'

# Send the SMS
try:
    # Once this is done, that's it! We'll handle the rest
    response = sms.send(message, recipients, sender)
    print(response)
except Exception as e:
    print(f"yoh cute ass nigger, we have a problem {e}")
