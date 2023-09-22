import pandas as pd
import os
import glob

def consolidate_excels(input_folder, output_folder, output_file_name):
    """
    Consolida todos os arquivos Excel em uma pasta em um único arquivo Excel.
    """
    
    # Garantir que a pasta de saída exista
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Lista de arquivos Excel na pasta input_folder
    files = glob.glob(os.path.join(input_folder, "*.xlsx"))

    # Lendo todos os arquivos Excel em uma lista de DataFrames
    all_data = [pd.read_excel(file, engine='openpyxl') for file in files]

    # Concatenando todos os DataFrames em um único DataFrame
    consolidated_df = pd.concat(all_data, axis=0, ignore_index=True)

    # Salvando o DataFrame consolidado em um arquivo Excel
    consolidated_df.to_excel(os.path.join(output_folder, output_file_name), index=False, engine='openpyxl')