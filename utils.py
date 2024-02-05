import csv
from collections import OrderedDict
from itertools import combinations
import math

NAME_INDEX = 0
PERCENTAGE_INDEX = 5

csv_file_path = 'StatsData/projections.csv'

# Read data from the CSV file
def read_and_filter_data(csv_file_path):
    filtered_data = []
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            percentage = float(row[PERCENTAGE_INDEX].rstrip('%'))  # Remove '%' and convert to float
            if percentage > 57: filtered_data.append((row[NAME_INDEX],percentage))

    unique_data = OrderedDict()
    for name, percentage in filtered_data:
        if name not in unique_data:
            unique_data[name] = percentage

    return list(unique_data.keys())

def get_projection_names():
    filtered_names = read_and_filter_data(csv_file_path)
    return filtered_names

def calculate_probability(hits, probs):
    """
    Calculate the probability of exactly 'hits' successful picks.
    """
    total_probability = 0
    for comb in combinations(range(len(probs)), hits):
        hit_prob = 1
        for i in comb:
            hit_prob *= probs[i]
        miss_prob = 1
        for i in set(range(len(probs))) - set(comb):
            miss_prob *= (1 - probs[i])
        total_probability += hit_prob * miss_prob
    return total_probability

def calculate_5pick_ev(probs, payouts, x=1):
    """
    Calculate the expected value of the 5-pick parlay bet.
    """
    p_5hits = calculate_probability(5, probs)
    p_4hits = calculate_probability(4, probs)
    p_3hits = calculate_probability(3, probs)
    p_else = 1 - (p_5hits + p_4hits + p_3hits)
    print(p_5hits, p_4hits, p_3hits, p_else)

    ev = (p_5hits * payouts[5] + p_4hits * payouts[4] + p_3hits * payouts[3] + p_else * payouts['else']) * x
    return ev

def calculate_3pick_ev(probs, payouts, x=1):
    """
    Calculate the expected value of the 3-pick parlay bet.
    """
    p_3hits = calculate_probability(3, probs)
    p_2hits = calculate_probability(2, probs)
    p_else = 1 - (p_3hits + p_2hits)

    ev = (p_3hits * payouts[3] + p_2hits * payouts[2] + p_else * payouts['else']) * x
    return ev

def calculate_2pick_ev(probs, payouts, x=1):
    p_2hits = math.prod(probs)
    p_else = 1 - p_2hits
    print(p_2hits)

    ev = (p_2hits * payouts[2] + p_else * payouts['else']) * x
    return ev

# probs5 = [0.70, 0.695, 0.61, 0.61, 0.61]
# five_normal_payouts = {5: 10, 4: 2, 3: 0.4, 'else': -1}

# probs2 = [0.6, 0.6]
# two_normal_payouts = {2: 3.0, 'else': -1}

probs3 = [0.6, 0.6, 0.7]
three_normal_payouts = {3: 1.75, 2: 0.5, 'else': -1}

# Calculate EV
# ev5 = calculate_5pick_ev(probs5, five_normal_payouts)
# ev2 = calculate_2pick_ev(probs2, two_normal_payouts)
ev3 = calculate_3pick_ev(probs3, three_normal_payouts)

# print(f"Expected Value: {ev2}")
print(f"Expected Value: {ev3}")