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
    #link_names: true
    #channel='#exec-board',  
    #channel='#general',
    #channel='#dbf',       
    #channel='#bot-test',
    #channel='#web', 
    text=""" <!channel> reminder, DBF meeting starts in 7 min """,
    # text=""" <!channel> remThanksinder, We'll have our first GBM of this year tomorrow at 12:45PM in RE104. Visit  <https://aiaa.iit.edu> for more.""",
    #text=""" <@U02CEB6H44V> nYOu'll get blocked."",
    icon_url='https://twitter.com/AiaaTech/photo'
)
