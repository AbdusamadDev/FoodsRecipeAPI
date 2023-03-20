import requests


url = "https://tasty.p.rapidapi.com/recipes/auto-complete"

querystring = {"prefix": "chicken soup"}

headers = {
	"X-RapidAPI-Key": "0ec5633dcfmshb355541d29d7d22p1730b5jsn466c104df7cd",
	"X-RapidAPI-Host": "tasty.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
