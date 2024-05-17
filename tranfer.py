import pandas as pd

# Carga el archivo CSV en un DataFrame de Pandas
df = pd.read_csv('players.csv')

# Muestra las primeras filas del DataFrame
list = df.to_dict('records')

fil = [x for x in list if 'Lionel Messi' in x['name'] ]

print(fil[0])

q_in = """
INSERT INTO public.api_players
(player_id, "name", current_club_id, current_club_name, country_of_citizenship, country_of_birth, city_of_birth, date_of_birth, "position", sub_position, foot, height_in_cm, market_value_in_eur, highest_market_value_in_eur, agent_name, contract_expiration_date, current_club_domestic_competition_id, first_name, last_name, player_code, image_url, last_season, url)
VALUES({}, '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, {}, {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}',{}, '{}');"""

final = ''

for x in list:
    final += q_in.format(*x.values())


f = open("transferss", "w")
f.write(final)
f.close()
