#IT Group Number 5 maths mini project

import random
import csv
import matplotlib.pyplot as plt

def coin_toss(num_coins, num_tosses, file_name):
    with open(file_name, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Coin', 'Number of Heads'])
        for i in range(num_coins):
            coin = []
            heads_count = 0
            for j in range(num_tosses):
                toss = random.randint(0,1)
                if toss == 0:
                    result = 'Heads'
                    heads_count += 1
                else:
                    result = 'Tails'
                coin.append(result)
            writer.writerow(['Coin ' + str(i+1), heads_count])
            
    # read the CSV file and create a line plot of the head count frequencies
    with open(file_name, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        head_counts = [int(row['Number of Heads']) for row in reader]
        freq_counts = [head_counts.count(i) for i in range(num_tosses+1)]
        plt.plot(range(num_tosses+1), freq_counts, label='Head Count Frequencies')
        plt.xticks(range(num_tosses+1))
        plt.xlabel('Number of Heads')
        plt.ylabel('Frequency')
        plt.title('Head Count Frequencies for {} Coins with {} Tosses Each'.format(num_coins, num_tosses))
        plt.legend()
        plt.show()

num_coins = int(input("Enter the number of coins: "))
num_tosses = int(input("Enter the number of tosses per coin: "))
file_name = input("Enter the name of the CSV file: ")

coin_toss(num_coins, num_tosses, file_name)
