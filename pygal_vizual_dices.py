import pygal
from dice import Dice

dice_one = Dice()
dice_two = Dice()

results = []
for roll in range(1000):
	dices_rolls = dice_one.roll_dice() + dice_two.roll_dice()
	results.append(dices_rolls)
	
analyz_results = []
max_result = dice_one.num_sides + dice_two.num_sides
for values in range(2, max_result+1):
	result = results.count(values)
	analyz_results.append(result)
	
hist_two = pygal.Bar()

hist_two.title = "Results for two dices(1000 rolls)"
hist_two.x_labels = [str(x) for x in range(2, max_result+1)]
hist_two.x_title = "Results"
hist_two.y_title = "Counting results"

hist_two.add("D6 + D6", analyz_results)
hist_two.render_to_file('dices_vizual.svg')
