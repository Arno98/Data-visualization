import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url =  'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status Code:", r.status_code)
json_r = r.json()

top_list = []
for number_id in json_r[:20]:
	url_2 =  ('https://hacker-news.firebaseio.com/v0/item/' + str(number_id) + '.json')
	r_2 = requests.get(url_2)
	print("Status Code:", r_2.status_code)
	json_r_2 = r_2.json()
	
	dictt = {'title' : json_r_2['title'], 'link' : 'https://news.ycombinator.com/item?id=' + str(number_id), 'comments' : json_r_2.get('descendants', 0)}
	top_list.append(dictt)
	
top_list = sorted(top_list, key=itemgetter('comments'), reverse=True)

titles, plot_dicts = [], []
for dicts in top_list:
	titles.append(dicts['title'])
	plot_dict = {'value' : dicts['comments'], 'xlink' : dicts['link']}
	plot_dicts.append(plot_dict)
	
my_vizual_style = LS('#334455', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
diagram = pygal.Bar(my_config, style=my_vizual_style)
diagram.title = "TOP 20 most discussed articles on the site 'Hacker-News'"
diagram.x_labels = titles
diagram.add("", plot_dicts)
diagram.render_to_file('vizual_hacker_news.svg')
