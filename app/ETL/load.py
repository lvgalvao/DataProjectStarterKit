"""modulo com todas as transformações necessárias para consolidar os dados de entrada."""

import os


def load_em_um_novo_excel(df, output_folder, output_file_name):
    """
    Carga: Salva um DataFrame em um arquivo Excel.

    type: df: pd.DataFrame
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df.to_parquet(
        os.path.join(output_folder, output_file_name), index=True
    )  # Retirado engine='openpyxl'
