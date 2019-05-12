import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'https://api.github.com/search/repositories?q=language:php&sort=stars'
r = requests.get(url)
json_r = r.json()
dicts = json_r['items']

names, plot_dicts = [], []
for d in dicts:
	names.append(d['name'])
	plot_dict = {'value' : d['stargazers_count'], 'label' : str(d['description']), 'xlink' : d['html_url']}
	plot_dicts.append(plot_dict)
	
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Python Project on GitHub"
chart.x_labels = names
chart.add("", plot_dicts)
chart.render_to_file('php_respons.svg')

