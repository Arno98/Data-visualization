import pygal
from dice import Dice

dice_1 = Dice(8)
dice_2 = Dice(8)

results_of_rolling = []
for rolling in range(1000):
	roll = dice_1.roll_dice() * dice_2.roll_dice()
	results_of_rolling.append(roll)
	
count_values_rolls = []
max_value = dice_1.num_sides * dice_2.num_sides
for number in range(1, max_value+1):
	count_values = results_of_rolling.count(number)
	count_values_rolls.append(count_values)
	
graph = pygal.Bar()

graph.title = "Results for multiply of two D8(1000 items)"
graph.x_labels = [str(x) for x in range(1, max_value+1)]
graph.x_title = "Result"
graph.y_title = "Counting Values"

graph.add("D8 * D8", count_values_rolls)
graph.render_to_file('dices_multiply_vizual.svg')

