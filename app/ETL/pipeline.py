"""This module contains functions for the ETL process."""

from ETL import extract, load, transform


def pipeline(input_folder, output_folder, output_file_name):
    """
    Função ETL: Extrai, Transforma e Carrega dados de arquivos Excel.

    type: input_folder: strs
    """
    data = extract(input_folder)
    consolidated_df = transform(data)
    load(consolidated_df, output_folder, output_file_name)
