#!/bin/bash

# Change to the specified directory
cd /home/serverw3/vhost/bot-support.com/pinkpanthercapital.bot-support.com/ppcTelegramHalvingBot

# Activate the virtual environment
source ./env/bin/activate

# Run the Python script and redirect output to log.file
/usr/bin/python3 ./ppchalving_countdown.py >> ./ppchalving_countdown.log
