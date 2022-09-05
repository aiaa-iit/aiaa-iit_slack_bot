#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 13:38:06 2022

@author: eyob
"""
import slack
import os
from pathlib import Path
from dotenv import load_dotenv
# from flask import Flask, request, Response
# from slackeventsapi import SlackEventAdapter
# import string
# from datetime import datetime, timedelta
# import time

env_path =  Path('.') / '.env'
load_dotenv(dotenv_path=(env_path))
client=slack.WebClient(token=os.environ['SLACK_TOKEN'])
#client.chat_postMessage(channel='#dbf-leads',text='Testing Bot, Howdy.... Lets go')
client.chat_postMessage(        
    channel='#general',
    text="""Hello there, welcome to the AIAA-IIT organisation""",
    icon_url='https://aiaa.iit.edu'
)
