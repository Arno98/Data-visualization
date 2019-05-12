from random import choice

class RandomWalkRefactoring():
	
	def __init__(self, number_points=3000):
		self.number_points = number_points
		self.x_value = [0]
		self.y_value = [0]
		
	def get_x_step(self):
		x_direction = choice([1, -1])
		x_distance = choice([0, 1, 2, 3, 4, 5])
		x_step = x_direction * x_distance
		return x_step
		
	def get_y_step(self):
		y_direction = choice([1, -1])
		y_distance = choice([0, 1, 2, 3, 4, 5])
		y_step = y_direction * y_distance
		return y_step
		
	def walk(self):
		while len(self.x_value) < self.number_points:
			x_step = self.get_x_step()
			y_step = self.get_y_step()
			
			if x_step and y_step == 0:
				continue
				
			next_step_x = self.x_value[-1] + x_step
			next_step_y = self.y_value[-1] + y_step
			
			self.x_value.append(next_step_x)
			self.y_value.append(next_step_y)
			
			
			
			
