########################################################################
#  install REST module 
# first from a DOC COMMAND (not python) console window run this command
#   python -m pip install requests
# Now you are able in Visual Studio Code run import requests
import requests     # comment

/* 
This is a comment
*/
# run a request on a site
#url = 'http://joelhrobinson.com'       -- none
#url = 'http://jsonplaceholder.typicode.com'
url = 'http://jsonplaceholder.typicode.com/photos'
response = requests.get (url)
json_data = response.json()
print (json_data)