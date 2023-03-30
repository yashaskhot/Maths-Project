import random
import plotly.graph_objs as go
import numpy as np


# function to simulate tossing 10 coins
def toss_coins():
    coins = ['H', 'T']  # H for heads, T for tails
    return [random.choice(coins) for _ in range(10)]


# ask user for number of trials
num_trials = int(input("Enter the number of trials: "))

# perform the requested number of trials and record the number of heads in each trial
heads_counts = []
for i in range(num_trials):
    outcome = toss_coins()
    heads_count = outcome.count('H')
    heads_counts.append(heads_count)

mean = np.mean(heads_counts)
stdev_plus = np.std(heads_counts)
stdev_minus = np.std(heads_counts)*-1
# create a histogram and line chart of the heads counts
data = [go.Histogram(x=heads_counts, nbinsx=11, name='Histogram')]
line = [go.Scatter(x=list(range(11)), y=[heads_counts.count(i) for i in range(11)], mode='lines', name='Line chart')]

# define layout of the plot
layout = go.Layout(
    title='Count vs Frequency',
    xaxis=dict(title='Count'),
    yaxis=dict(title='Frequency'),
)

# combine the histogram and line chart into one plot
fig = go.Figure(data=data + line, layout=layout)

# display the plot
fig.show()

print(mean)
print(stdev_plus)
print(stdev_minus)