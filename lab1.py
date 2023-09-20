import requests

#URL to Google
URLGoogle = "https://google.com/"

#Get URL
resp = requests.get(URLGoogle)

#URL to GitHub code
URLGitHub = "https://raw.githubusercontent.com/jggeiger/CMPUT404_lab01/main/lab1.py"

#Get URL and print text
resp = requests.get(URLGitHub)
print(resp.text)
