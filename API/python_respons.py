import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)

print("Status Code : " + str(r.status_code))

response_dict = r.json()

print(response_dict.keys())
print("Number of repositories : " + str(response_dict["total_count"]))

repo_dicts = response_dict['items']
print("Repositories returned : " + str(len(repo_dicts)))

repo_dict = repo_dicts[0]
print("Number of keys : " + str(len(repo_dict)))
for key in sorted(repo_dict.keys()):
	print(key)
	
print("\nSelected information about first repository:")
print("Name :", repo_dict['name'])
print("Owner :", repo_dict['owner']['login'])
print("Stars:", repo_dict['stargazers_count'])
print("Repository:", repo_dict['html_url'])
print("Created:", repo_dict["created_at"])
print("Updated:", repo_dict["updated_at"])
print("Description:", repo_dict["description"])

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
	try:
		print("Name :", repo_dict['name'])
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
