import requests

#URL to GitHub code
URL = "https://raw.githubusercontent.com/jggeiger/CMPUT404_lab01/main/lab1.py"

#Get URL and print text
resp = requests.get(URL)
print(resp.text)