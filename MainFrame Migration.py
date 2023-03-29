import openai
import json
import pandas as pd
from pandas import DataFrame
import numpy as np
import os
import re
from datetime import date
import openpyxl
import xlsxwriter
from openpyxl.styles import Alignment

# Initializing the directory

current_dir = "C:\\Users" # Please change the directory
os.chdir(current_dir)

# Set up your OpenAI API key
openai.api_key = ""   # Put your API Key

Prompt1 = " Pre conditions for AM Policy Association Establishment are as follows 1. UE initial registration with the network.2. The AMF re-allocation with PCF change in handover procedure and registration procedure.3. EPS to 5GS mobility when there is no existing AM Policy Association between AMF and PCF for this UE."

Prompt2 = " Pre conditions for AM Policy Association Modification initiatedby the AMF are as follows 1. A Policy Control Request Trigger condition is met: the procedure is initiated by the AMF.2. PCF policy decision per local decision or per trigger by other peers of the PCF (i.e. UDR, AF or NWDAF): the procedure is initiated by the PCF.3. AM Policy Association Modification with the old PCF during AMF relocation: the procedure is initiated by the AMF. "

Prompt_Ilan = "Please generate a comprehensive testing strategy for application refactoring and rationalization, covering key use cases such as portfolio consolidation/rationalization, application rationalization, and decoupling and isolation. The strategy should include requirements gathering, optimization and automation, unit and functional testing, security and non-functional requirements testing, and co-existence testing. Identify suitable tools for each stage of the strategy, including IBM ADDI and IGNITE STAM for requirements gathering, IGNITE Optimization and HP UFT for optimization and automation, IBM Z Unit and STeF on UFT/RFT for unit and functional testing, and IBM Application Performance Analyzer for z/OS for security testing. Finally, include co-existence testing for data and architecture, with suitable tools including Mainframe System Log Analyzer."

'''
# Define the prompt you want to use for ChatGPT
question1 = str("Please train this model with following use case "+ Prompt1 +"Please provide weightage to this use case in your model")
response = openai.Completion.create(engine="text-davinci-003",prompt=question,max_tokens=2000)

# Define the prompt you want to use for ChatGPT
question2 = str("Please train this model with following use case "+ Prompt2 +"Please provide weightage to this use case in your model")
response = openai.Completion.create(engine="text-davinci-003",prompt=question,max_tokens=2000)

'''

question = "How can a comprehensive testing strategy be developed to support application refactoring and rationalization, with a focus on portfolio consolidation, application rationalization, and decoupling and isolation??"
question1 = str(Prompt_Ilan+question)
print(question)
# Send the API request to ChatGPT
response = openai.Completion.create(engine="text-davinci-003",prompt=question1,max_tokens=2000,temperature=0)
print(response.choices[0]['text'])
Output = response.choices[0]['text']



