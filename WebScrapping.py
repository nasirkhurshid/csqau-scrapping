import requests
import re
from bs4 import BeautifulSoup

page = requests.get("http://cs.qau.edu.pk/faculty.php")
soup = BeautifulSoup(page.content, 'html.parser')

names = []
mails = []
phone = []

namePattern = "Dr\.[\S\s]+|Me[\S\s]+|If[\S\s]+"
mailPattern = "[a-z]*.[a-z]+ at qau dot edu dot pk$"
phonePattern = "\+92[ 0-9\-]{13}"

ind = i = 0

nameData = soup.select('strong')
for str in nameData:
    nList = re.findall(namePattern, str.text)
    for name in nList:
        name = re.sub("\s+", " ", name)
        names.append(name)
        if "Muazzam" in name:
            ind=i
        i+=1

phAndMail = soup.select('a')
for str in phAndMail:
    eList = re.findall(mailPattern, str.text)
    for email in eList:       
        email = re.sub(" at qau dot edu dot pk", "@qau.edu.pk", email)
        mails.append(email)

for str in phAndMail:
    pList = re.findall(phonePattern, str.text)
    for ph in pList:       
        phone.append(ph)
        if len(phone) == 5:
            phone.append("    ")

file = open("data.txt", "w")
str1, str2, str3 = "Name", "Phone", "Email\n"
file.write(str1.ljust(30, " "))
file.write(str2.ljust(30, " "))
file.write(str3)
for i in range(len(names)):
    file.write(names[i].ljust(30," "))
    file.write(phone[i].ljust(30," "))
    file.write(mails[i]+"\n")
file.close()

print("Data written to file!")