import pygal
from dice import Dice

dice_1 = Dice()
dice_2 = Dice()
dice_3 = Dice()

results = []
for d in range(1000):
	roll = dice_1.roll_dice() + dice_2.roll_dice() + dice_3.roll_dice()
	results.append(roll)
	
analyz = []
max_value = dice_1.num_sides + dice_2.num_sides + dice_3.num_sides
for number in range(3, max_value+1):
	count_values = results.count(number)
	analyz.append(count_values)
	
hist = pygal.Bar()
hist.title = "Results for rolling of three D6"
hist.x_labels = [str(x) for x in range(3, max_value+1)]
hist.x_title = "Results"
hist.y_title = "Counting Values"
hist.add("D6 + D6 + D6", analyz)
hist.render_to_file('dices_three_vizual.svg')
