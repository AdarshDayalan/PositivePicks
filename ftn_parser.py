import csv
import os
from bs4 import BeautifulSoup

pages = 4
csv_file_path = 'StatsData/projections.csv'

# Function to parse HTML content and return extracted data
def parse_html_content(html_content):
    soup = BeautifulSoup(html_content, 'lxml')
    projections = soup.find_all(class_='rt-tr-group')
    data_rows = []

    for projection in projections:
        row_data = []
        cells = projection.find_all(class_='rt-td-inner')
        for cell in cells:
            text = cell.get_text(strip=True)
            row_data.append(text)
        data_rows.append(row_data)

    return data_rows

def parse_text_content(text_content):
    data_lines = text_content[11:131]
    cleaned_data = [x.strip() for x in data_lines]
    records = [cleaned_data[i:i+6] for i in range(0, len(cleaned_data), 6)]
    return records


def parseFTN():
    all_data = []
    for i in range(1, pages + 1):
        file_path = f'StatsData/page{i}.txt'
        with open(file_path, 'r') as file:
            text_content = file.readlines()
            # Parse the HTML content and extract data
            page_data = parse_text_content(text_content)
            all_data.extend(page_data)
        os.remove(file_path)

    # Write extracted data to a CSV file
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Name', "Team", "Stat", "Line", "Bet", "Win"])
        for row in all_data:
            csvwriter.writerow(row)

    print("All data has been stored in the CSV file.")