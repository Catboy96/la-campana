#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import smtplib
import sys
import os
from email.mime.text import MIMEText
from email.header import Header

# SMTP configuration
smtp_host = "example.com"
smtp_port = 25
smtp_user = "user@domain.name"
smtp_pass = "P@ssw0rd"

# Email configuration
receiver = 'campana@notify.me'


if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("No command specified, exiting...")
        exit(0)

    args = sys.argv[1:]
    command = ""
    for arg in args:
        command = command + arg + ' '

    process = os.popen(command)
    content = process.read()

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("Campana Reminder", 'utf-8')
    message['To'] = Header(receiver, 'utf-8')

    subject = "🔔 Result of: " + command
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtp_client = smtplib.SMTP()
        print("Connecting to SMTP server... ", end='')
        smtp_client.connect(smtp_host, smtp_port)
        print("Done.")
        print("Login... ", end='')
        smtp_client.login(smtp_user, smtp_pass)
        print("Done.")
        print("Sending email... ", end='')
        smtp_client.sendmail(smtp_user, receiver, message.as_string())
        print("Done.")
    except smtplib.SMTPException:
        print("FAILED")
