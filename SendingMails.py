import os
import sys
import random
import smtplib



class applicant:
    __name = ""
    __mail = ""


    def __init__(self,name,mail): #assuming first line is name and second is mail
        self.__name=name
        self.__mail=mail


    def set_name(self, name):
        self.__name = name

    def set_mail(self, mail):
        self.__mail = mail


    def get_name(self):
        return self.__name

    def get_mail(self):
        return self.__mail




text_file = open('read.txt', 'r')
lines = text_file.readlines()
n = len(lines) / 2  # number of students
text_file.close()

students = []

text_file = open('read.txt', 'r')

for i in range(n):
    students.append(applicant(text_file.readline(),text_file.readline()))

text_file.close()


mail =smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()

mail.login('ASURTIT@gmail.com','MAILTEST')

for j in range(n):
    subject = "RacingTeam Results."
    name= students[j].get_name()
    content = "Congratulations, " + name + " you have been accepted with us!"
    message = 'subject: %s\n\n%s' % (subject, content)
    mail.sendmail('ASURTIT@gmail.com',students[j].get_mail(),message)


mail.close()

raw_input()


#IT ROCKS~!