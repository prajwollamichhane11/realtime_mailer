# Realtime_Mailer

I want to remotely access my PC at home from work for the sake of ssh logins. The PC at home is on and connected to the internet. I would require my PC's external address before connecting to it. So, what I did was wrote this script and compiled it on my home PC. I also created a daemon process using crontab on linux that automatically sent my home PCs IP to my email on certain time gaps.


Language Used: Python3

Libraries Used: smtplib, time, subprocess


Creating The Daemon Process:

Use of Chrontab:


#min hr dom moy dow COMMAND

#0-59 0-23 1-30 1-12 0-6 python3 ~/Desktop/YourFileName

example: 0 7 20 1 0 python3 ~/Desktop/realtime_mailer.py



So, what this example did was ran the realtime-mailer.py in 20th of January Sunday at exactly 7:00 in the morning.

