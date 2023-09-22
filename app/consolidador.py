"""modulo com todas as transformações necessárias para consolidar os dados de entrada."""

import glob
import os
import sys

import pandas as pd

print(sys.executable)


def extract(input_folder):
    """
    função para extrair dados de arquivos Excel.

    type: input_folder: str
    """
    files = glob.glob(os.path.join(input_folder, "*.xlsx"))
    if not files:
        raise ValueError("No Excel files found in the specified folder")
    all_data = [pd.read_excel(file) for file in files]
    return all_data


def transform(all_data):
    """
    função para consolidar os dados de arquivos Excel.

    type: all_data: list
    """
    if not all_data:
        raise ValueError("No data to transform")
    consolidated_df = pd.concat(all_data, axis=0, ignore_index=True)
    return consolidated_df


def load(df, output_folder, output_file_name):
    """
    Carga: Salva um DataFrame em um arquivo Excel.

    type: df: pd.DataFrame
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df.to_excel(
        os.path.join(output_folder, output_file_name), index=False
    )  # Retirado engine='openpyxl'


def consolidate_excels(input_folder, output_folder, output_file_name):
    """
    Função ETL: Extrai, Transforma e Carrega dados de arquivos Excel.

    type: input_folder: strs
    """
    data = extract(input_folder)
    consolidated_df = transform(data)
    load(consolidated_df, output_folder, output_file_name)
