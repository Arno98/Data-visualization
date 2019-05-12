import pygal
from dice import Dice

dice = Dice()

results = []
for roll in range(100):
	dice_roll = dice.roll_dice()
	results.append(dice_roll)
	
analyz_results = []
for value in range(1, dice.num_sides+1):
	result = results.count(value)
	analyz_results.append(result)
	
hist = pygal.Bar()

hist.title = "Results for 100 rolling dice(100 rolls)"
hist.x_labels = [str(x) for x in range(1, dice.num_sides+1)]
hist.x_title = "Results"
hist.y_title = "Counting results"

hist.add("D6", analyz_results)
hist.render_to_file('dice_vizual.svg')



