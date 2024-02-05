import csv
import json

# Function to find matching projections with "Regular" line
def find_normal_line_projections(prize_pick_lines, projects):
    matching_projections = []
    for project in projects:
        if prize_pick_lines[project['Name']][project['Stat']][project['Line']] == 'Normal':
                matching_projections.append(project)
    return matching_projections

# Reading the CSV files
def read_csv_file(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

# Assume CSV files are named 'prize_pick_lines.csv' and 'projects.csv'
with open('PlayerData/players.json', 'r', encoding='utf-8') as file:
    prize_pick_lines = json.load(file)
projects = read_csv_file('StatsData/projections.csv')

# Find and display matching projections
matching_projections = find_normal_line_projections(prize_pick_lines, projects)
for p in matching_projections:
    print(p)
