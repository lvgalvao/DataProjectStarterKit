"""pipeline principal do projeto."""

import os

from ETL import pipeline_completa
from utils import generate_absenteeism_data


def generate_excel_files(files: int = 10):
    """Gera n arquivos Excel com dados de absenteísmo."""
    for i in range(files):
        df = generate_absenteeism_data()
        output_path = os.path.join("data/input", f"absenteeism_data_{i}.xlsx")
        df.to_excel(output_path, index=False)


def consolidate_files():
    """Consolida os arquivos Excel gerados em um único arquivo."""
    input_folder = "data/input"
    output_folder = "data/output"
    output_file_name = "consolidated_absenteeism_data.xlsx"
    pipeline_completa(input_folder, output_folder, output_file_name)


if __name__ == "__main__":
    generate_excel_files(50)
    consolidate_files()
    print("hello!")
