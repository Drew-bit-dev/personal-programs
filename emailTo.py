import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "SenderEmail"  # Enter your address
receiver_email = "recieverAddress"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
    Subject: Hi there

    This message is sent from Python."""
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


#Code written to send an email from a gmail account. Can be scaled up using a forloop and an array
#of recipients