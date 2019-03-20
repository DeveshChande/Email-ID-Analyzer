"""
Email-ID-Analyzer, by Devesh Chande
This is a simple email-id checker which attempts to notify the user whether
his/her email-id has been disclosed via the haveibeenpwned API.
It will notify the user of the following information, in the event that a
breach has occurred :

1. Company Name
2. Domain
3. Compromised information
4. Date of Breach

In the event that the email is not leaked (as far as verification through public
resources go, the user will be notified that no data leaks have been associated
with that email-id.)

"""

import requests
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_data(self, data):
        print(data)


print("Welcome to your personal Email-ID-Analyzer!")
print("-------------------------------------------")

print("Please enter the email-id you wish to check.")
user_email_id = str(input())

print(f'Check whether the email-id : {user_email_id} has been comprised...')
headers = {'User-Agent' : 'Email-ID-Analyzer-DC'}
r = requests.get(f'https://haveibeenpwned.com/api/breachedaccount/{user_email_id}', headers = headers)



if r.status_code == 404:
    print("Horray! The email-id has not been compromised!")
else:
    print("Pwned! The email-id has been leaked. Change your passwords immediately!")
    print("--------------------------------")
    company_list = r.json()
    i = 0
    while i < len(company_list):
        print(f'Name : {company_list[i]}')
        r1 = requests.get(f'https://haveibeenpwned.com/api/v2/breach/{company_list[i]}', headers = headers)
        temp_list = r1.json()
        print(f'Website: {temp_list["Domain"]}')
        print(f'What was leaked : {temp_list["DataClasses"]}')
        print(f'Date of breach : {temp_list["BreachDate"]}')
        print('---------------------------------------------------------------')
        i+=1
