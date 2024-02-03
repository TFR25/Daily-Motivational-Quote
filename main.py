import random
import smtplib
import json

my_email = "my email"
my_pwd = "my email password"

try:
    with open("data.json", "r") as data_file:
        data = json.load(data_file)

except FileNotFoundError:
    print("Error, file not located.")
except json.decoder.JSONDecodeError:
    print("Error, file empty.")
else:
    my_email = data["outlook"]["email"]
    my_pwd = data["outlook"]["password"]
    email_recipient = []
    for recipient in data['recipients']:
        email_recipient.append(recipient['email'])

with open(file="quotes.txt") as file:
    quote = random.choice(file.readlines())


def send_quote():
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pwd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email_recipient,
            msg=f"Subject:Motivational quote \n\n{quote}")


send_quote()
