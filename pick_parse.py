import csv
# 3-PT Made,Assists,Blks+Stls,Blocked Shots,Points,Pts+Asts,Pts+Rebs,Pts+Rebs+Asts,Rebounds,Rebs+Asts,Steals,Turnovers


# Function to find matching projections with "Regular" line
def find_normal_line_projections(prize_pick_lines, projects):
    matching_projections = []
    for project in projects:
        for line in prize_pick_lines:
            if line['Name'] == project['Name'] and line['Line_Type'] == 'Regular':
                # Map project stats to prize pick line columns
                stat_key = {
                    '3-PT Made': '3-PT Made',
                    'Assists': 'Assists',
                    'Blks+Stls': 'Blks+Stls',
                    'Blocked Shots': 'Blocked Shots',
                    'Points': 'Points',
                    'Pts+Asts': 'Pts+Asts',
                    'Pts+Rebs': 'Pts+Rebs',
                    'Pts+Rebs+Asts': 'Pts+Rebs+Asts',
                    'Rebounds': 'Rebounds',
                    'Rebs+Asts': 'Rebs+Asts',
                    'Steals': 'Steals',
                    'Turnovers': 'Turnovers'
                }.get(project['Stat'])
                
                if stat_key and line[stat_key] and float(line[stat_key]) == float(project['Line']):
                    matching_projections.append(project)
    return matching_projections

# Reading the CSV files
def read_csv_file(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

# Assume CSV files are named 'prize_pick_lines.csv' and 'projects.csv'
prize_pick_lines = read_csv_file('prizepicks_lines.csv')
projects = read_csv_file('StatsData/projections.csv')

# Find and display matching projections
matching_projections = find_normal_line_projections(prize_pick_lines, projects)
for p in matching_projections:
    print(p)
