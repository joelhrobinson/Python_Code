##########################################
# Selenium GET and parsing the JSON DATA response
# 
import requests

url = 'https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
json_data = response.json()

############################################
# parse the resonse. APPEND into an array of Photo URLs
# 
url_list = []
for photo in json_data:
    url_list.append(photo['url'])

#############################################
# Count how many photos in json_data
# Count how many UNIQUE (set) photos in Json_data
print (len(url_list))
print (len (set (url_list)))
