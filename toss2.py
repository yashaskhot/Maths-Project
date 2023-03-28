import random
import plotly.graph_objs as go

# function to simulate tossing 10 coins
def toss_coins():
    coins = ['H', 'T'] # H for heads, T for tails
    return [random.choice(coins) for _ in range(10)]

# ask user for number of trials
num_trials = int(input("Enter the number of trials: "))

# perform the requested number of trials and record the number of heads in each trial
heads_counts = []
for i in range(num_trials):
    outcome = toss_coins()
    heads_count = outcome.count('H')
    heads_counts.append(heads_count)

# create a histogram of the heads counts
data = [go.Histogram(x=heads_counts, nbinsx=11)]

# define layout of the plot
layout = go.Layout(
    title='Count vs Frequency',
    xaxis=dict(title='Count'),
    yaxis=dict(title='Frequency'),
)

# create the plot
fig = go.Figure(data=data, layout=layout)

# display the plot
fig.show()
