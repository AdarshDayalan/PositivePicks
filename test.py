import csv

# Input and output file names
input_file_name = 'StatsData/p1.txt'
output_file_name = 'output.csv'

# Open the input file and read the lines
with open(input_file_name, 'r') as file:
    lines = file.readlines()

# Start processing from line 6, where the actual data starts, skipping the header
data_lines = lines[11:131]

print(data_lines)
cleaned_data = [x.strip() for x in data_lines]
records = [cleaned_data[i:i+6] for i in range(0, len(cleaned_data), 6)]

print(records)

# # Open the output CSV file
# with open('output.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
    
#     # Write the header row
#     writer.writerow(['Name', 'Team', 'Stat', 'Line', 'Bet', 'Win'])
    
#     # Process and write each record to the CSV file
#     for record in records:
#         writer.writerow(record)

# print('Data has been successfully written to output.csv')