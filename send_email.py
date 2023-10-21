import smtplib, ssl, os


def sendemail(message):
    port = 465  # For SSL

    smtp_server = "smtp.gmail.com"
    sender_email = 'devopsesi2022@gmail.com'
    receiver_email = 'devopsesi2022@gmail.com'
    password = 'unkj vlla dtat dxkd'  # os.getenv

    # Message = f""" \
    # Subject: Hi
    #
    #
    #
    #{message} . """
    # Create a secure SSL context
    context = ssl.create_default_context()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if __name__ == '__main__':
    message = "Hi"
    sendemail(message)