import matplotlib.pyplot as plt
from random_walk import RandomWalk
from die import Die
import plotly.express as px
"""Plotting a simple line graph"""
# print(plt.style.available)
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.style.use('seaborn-v0_8')
# fix, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth = 3)

# ax.set_title("Square Numbers", fontsize = 24)
# ax.set_xlabel("Value", fontsize = 14)
# ax.set_ylabel("Square of Value", fontsize = 14)
# ax.tick_params(labelsize = 14)

""""""
# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]
# # == 
# # y_values = []
# # for x in x_values:
# #   y_values.append(x**2)

# plt.style.use('seaborn-v0_8')
# fix, ax = plt.subplots()
# ax.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, s = 10)

# ax.axis([0, 1100, 0, 1_100_000])
# ax.ticklabel_format(style = 'plain')

# plt.savefig('squares_plot.png', bbox_inches = 'tight')
# plt.show()

""""""
# while True:
#   rw = RandomWalk(50000)
#   rw.fill_walk()
#   plt.style.use('classic')
#   fig, ax = plt.subplots(figsize = (15, 9))
#   point_numbers = range(rw.num_points)
#   ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors = 'none', s = 15)
#   ax.scatter(0, 0, c='green', edgecolors = 'none', s = 1)
#   ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors = 'none', s = 100)
#   ax.get_xaxis().set_visible(False)
#   ax.get_yaxis().set_visible(False)
#   ax.set_aspect('equal')
#   plt.show()
#   keep_running = input("Make another walk? (y/n): ")
#   if keep_running == 'n':
#     break

""""""
die_1 = Die()
die_2 = Die(10)
results = []
for roll_num in range(50000):
  result = die_1.roll() + die_2.roll()
  results.append(result)
  # print(results)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
  frequency = results.count(value)
  frequencies.append(frequency)
# print(frequencies)

title = "Results of Rolling a D6 and a D10 50,000 Times"
lables = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels = lables)
fig.update_layout(xaxis_dtick = 1)
fig.write_html('dice_visual_d6d10.html')
# fig.show()