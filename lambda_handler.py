    #import the twilio module
    from twilio.rest import Client

    #define your lambda function
    def lambda_handler(event, context):

        #enter your account details here
        account_sid = "paste your twilio account SID here"
        auth_token = "paste your twilio auth token here"

        client = Client(account_sid, auth_token)
        
        message = client.messages.create(
            to="+The phone number you want to send the message to here",
            from_="+The twilio phone number you bought earlier here",
            body="Mrs. Kauffman, I need some help.")
