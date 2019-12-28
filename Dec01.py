

import requests
import csv                          ## import csv library
import os
os.getcwd()
os.chdir ('L:\software\Python\scripting')
os.getcwd()

>>>


timing_data = []                    ## create blank list
with open ('TestTimingData.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    for row in file_reader:
        TestTimingData.append(row)

column_chart_data = [["Test Name", "Diff from Avg"]]
table_data = [["Test Name","Run Time (s)"]]

for row in timing_data[1:]          ## show row 1 cuz it is the header
    test_name = row[0]              ## this will be first column
    try:
        current_run_time = float(row[1])
        avg_run_time = float(row[2])
    except:
        print (row[1])
        print (row[2])
    diff_from_avg = avg_run_time - current_run_time
    column_chart_data.append([test_name, diff_from_avg])
    table_data.append([test_name,current_run_time])



