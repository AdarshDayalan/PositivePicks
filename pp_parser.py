from bs4 import BeautifulSoup
import json
import os

date = "02-01-24"

directory = 'PlayerData'
txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

player_data = {}

for filename in txt_files:
    player_name = filename[:-4]
    file_path_txt = '{}/{}.txt'.format(directory, player_name)
    with open(file_path_txt, 'r', encoding='utf-8') as file:
        html_content = file.read()
    os.remove(file_path_txt)

    soup = BeautifulSoup(html_content, 'lxml')

    projections = soup.find_all('li', class_='projection')

    for projection in projections:
        if player_name not in player_data:
            player_data[player_name] = {}

        # Determine the type of projection (e.g., Points, Rebounds)
        projection_type = projection.find('p', class_='text').text

        score_value = projection.find('div', class_='presale-score').text
        modifier = "Normal"
        goblin_icon = projection.find('img', alt="Goblin")
        demon_icon = projection.find('img', alt="Demon")
        if goblin_icon:
            modifier = "Goblin"
        elif demon_icon:
            modifier = "Demon"

        if projection_type not in player_data[player_name]:
            player_data[player_name][projection_type] = {}
        player_data[player_name][projection_type][float(score_value)] = modifier

file_path_json = '{}/players.json'.format(directory)
with open(file_path_json, 'w') as json_file:
    json.dump(player_data, json_file, indent=2)

# file_path_txt = 'PlayerData/{}/{}.txt'.format(date,name)

# if os.path.exists(file_path_txt):
#     os.remove(file_path_txt)
#     print(f"File {file_path_txt} has been deleted.")
# else:
#     print(f"The file {file_path_txt} does not exist.")