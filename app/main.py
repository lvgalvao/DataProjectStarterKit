# main.py

import os
import pandas as pd
from absenteeism_generator import generate_absenteeism_data
from consolidador import consolidate_excels

def generate_excel_files(files: int = 10):
    """Gera n arquivos Excel com dados de absenteísmo."""
    for i in range(files):
        df = generate_absenteeism_data()
        output_path = os.path.join("data", f"absenteeism_data_{i}.xlsx")
        df.to_excel(output_path, index=False)

def consolidate_files():
    """Consolida os arquivos Excel gerados em um único arquivo."""
    input_folder = "data"
    output_folder = "consolidado"
    output_file_name = "consolidated_absenteeism_data.xlsx"
    consolidate_excels(input_folder, output_folder, output_file_name)

if __name__ == "__main__":
    generate_excel_files(50)
    consolidate_files()