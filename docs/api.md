# API Documentation

Abaixo, você encontrará detalhes sobre as funções e módulos do nosso projeto.

## Módulo `consolidador`

### `extract`

```python
def extract(input_folder: str) -> list:
    """
    Função para extrair dados de arquivos Excel.

    Args:
        input_folder (str): Caminho da pasta contendo arquivos Excel.

    Returns:
        list: Lista contendo DataFrames do pandas.
    """
```

### `transform`

```python
def transform(data: list) -> pd.DataFrame:
    """
    Função para transformar uma lista de DataFrames em um único DataFrame consolidado.

    Args:
        data (list): Lista contendo DataFrames para consolidação.

    Returns:
        DataFrame: DataFrame consolidado.
    """
```

### `load`

```python
def load(df: pd.DataFrame, output_folder: str, filename: str) -> None:
    """
    Função para carregar (ou salvar) um DataFrame em um arquivo Excel.

    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        output_folder (str): Diretório onde o arquivo será salvo.
        filename (str): Nome do arquivo Excel.

    Returns:
        None
    """
```

### `consolidate_excels`

```python
def consolidate_excels(input_folder: str, output_folder: str, filename: str) -> None:
    """
    Função para consolidar múltiplos arquivos Excel em um único arquivo.

    Args:
        input_folder (str): Pasta contendo arquivos Excel.
        output_folder (str): Pasta onde o arquivo consolidado será salvo.
        filename (str): Nome do arquivo Excel consolidado.

    Returns:
        None
    """
