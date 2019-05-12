import requests

def url_python():
	url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
	r = requests.get(url)
	return r.status_code
	
url_python()
