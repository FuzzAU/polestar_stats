import openpyxl

import os
import pandas as pd
from dateutil import parser

from stats.models import Journey

test_file = './data/anonymous_test_log.xlsx'


def parse(file_obj):
    # Open workbook and get to the active sheet
    wb = pd.read_excel(file_obj, sheet_name='Trips')
    wb.head()
    
    # These are the headers I want!!!!!
    expected_headers = ['Start Date','End Date','Start Address','End Address',
                        'Distance in kilometres','Consumption in kwh','Category',
                        'Start Latitude','Start Longitude','End Latitude','End Longitude']


    # If headers aren't the same as what we expect, throw some sort of error!
    valid_headers = list(wb.keys()) == expected_headers
    
    for _, polestar_log_journey in wb.iterrows():
        journey_items = {
            'start_date': parser.parse(polestar_log_journey['Start Date']),
            'end_date': parser.parse(polestar_log_journey['End Date']),
            'start_address': polestar_log_journey['Start Address'],
            'end_address': polestar_log_journey['End Address'],
            'distance': polestar_log_journey['Distance in kilometres'],
            'energy_consumption': polestar_log_journey['Consumption in kwh'],
            'category': polestar_log_journey['Category'],
            'start_latitude': polestar_log_journey['Start Latitude'],
            'start_longitude': polestar_log_journey['Start Longitude'],
            'end_latitude': polestar_log_journey['End Latitude'],
            'end_longitude': polestar_log_journey['End Longitude'],
        }
        j = Journey(**journey_items)
        j.save()

