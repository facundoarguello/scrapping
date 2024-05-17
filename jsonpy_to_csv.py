import pandas as pd
from temporal_torneo_emi import TORNEO_DICT

print("hola")


# pd.DataFrame([flattenObj(d, kSep=' > ') for d in pData]).to_csv(csv_path, index=False)
df = pd.DataFrame(TORNEO_DICT)
df_limpio = df.replace({'\t': ' ', 
                        '\r': ' ', 
                        '\n': ' ', 
                        'JUGADORES:':'',
                        'DESCRIPCIÓN:':'',
                        'SERVICIOS:':''
                        }, regex=True)
output_file = "data_torneos.csv"

# Export the DataFrame to a CSV file
df_limpio.to_csv(output_file, index=False)

print(f"El archivo {output_file} se ha creado exitosamente.")