import smtplib
import datetime as Datetime
import random

my_email = "afeezbolajiola@gmail.com"
password = "raafiypvegedssxo"

def getDate():
    today = Datetime.datetime.today().weekday()
    return today


with open("quotes.txt", "r") as quotes:
    quote_list = [(quote.replace('"', "")).strip("\n") for quote in (quotes.readlines())]
    quote = quote_list[random.randint(0, len(quote_list) - 1)]

def mail_quote():
    print(getDate())
    if getDate() == 3:
        try:
            connection = smtplib.SMTP_SSL("smtp.gmail.com", port=465)
        except TimeoutError:
            print(TimeoutError.strerror)
        else:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="afeezmobolajiola@gmail.com",
                                msg=f"Subject: DAILY QUOTE \n\n{quote}")
            connection.close()


mail_quote()


