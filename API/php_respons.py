import requests

url = 'https://api.github.com/search/repositories?q=language:php&sort=stars'
r = requests.get(url)
print("Status Code:", r.status_code)
json_r = r.json()

dicts = json_r['items']
for repo_dict in dicts:
	try:
		print("\nName :", repo_dict['name'])
		print("Owner :", repo_dict['owner']['login'])
		print("Stars:", repo_dict['stargazers_count'])
		print("Repository:", repo_dict['html_url'])
		print("Created:", repo_dict["created_at"])
		print("Updated:", repo_dict["updated_at"])
		print("Description:", repo_dict["description"])
	except UnicodeEncodeError:
		None
	else:
		None
