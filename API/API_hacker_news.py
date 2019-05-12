import requests
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status Code:", r.status_code)

json_r = r.json()
listt = []
for dictt in json_r[:30]:
	url_2 = ('https://hacker-news.firebaseio.com/v0/item/' + str(dictt) + '.json')
	r_2 = requests.get(url_2)
	print("Status Code 0:", r_2.status_code)
	json_r_2 = r_2.json()
	
	dictt_2 = {'title' : json_r_2['title'], 'link' : 'https://news.ycombinator.com/item?id=' + str(dictt), 'comments' : json_r_2.get('descendants', 0)}
	
	listt.append(dictt_2)
	
listt = sorted(listt, key=itemgetter('comments'), reverse=True)

for dictt_2 in listt:
	try:
		print("\nTitle:", dictt_2['title'])
		print("Link:", dictt_2['link'])
		print("Comments:",dictt_2['comments'])
	except UnicodeEncodeError:
		None
	else:
		None
