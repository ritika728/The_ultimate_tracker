import pandas as pd
import json
import urllib
import urllib.request
import smtplib
from email.message import EmailMessage
def funcalert():
    url = "https://eonet.sci.gsfc.nasa.gov/api/v2.1/events"
    response = urllib.request.urlopen(url)
    text = response.read()
    json_data = json.loads(text)
    df = pd.json_normalize(json_data['events'])
    file = open('city.txt','r')
    contents = file.readlines()
    for i in contents:
        for j in range(0,len(df)):
            if(i==(df.title[j]+"\n")):
                print("hello")
                gmail_user = ''
                gmail_password = ''

                sent_from = gmail_user
                to = ['']
                subject = 'Lorem ipsum dolor sit amet'
                body = 'consectetur adipiscing elit'

                email_text = """\
                From: %s
                To: %s
                Subject: %s

                %s
                """ % (sent_from, ", ".join(to), subject, body)

                try:
                    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    smtp_server.ehlo()
                    smtp_server.login(gmail_user, gmail_password)
                    smtp_server.sendmail(sent_from, to, email_text)
                    smtp_server.close()
                    print ("Email sent successfully!")
                except Exception as ex:
                    print ("Something went wrong….",ex)
                break
funcalert()
