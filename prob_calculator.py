import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs): #constructor
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, amount):
    draw_list = []
    if amount > len(self.contents):
      return self.contents
    for i in range(amount):
      removed = self.contents.pop(random.randrange(len(self.contents)))
      draw_list.append(removed)
    return draw_list
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success_count = 0
  for i in range(num_experiments):
    success = True
    copy_hat = copy.deepcopy(hat)
    colors_drawn = copy_hat.draw(num_balls_drawn)
    for key, value in expected_balls.items():
      if colors_drawn.count(key) < value:
        success = False
        break
    if success:
      success_count += 1

  return success_count / num_experiments
