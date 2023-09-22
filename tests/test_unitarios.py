"""Tests for unit functionalities."""

import os

import pandas as pd
import pytest

from app.ETL import extract_excel, load_em_um_novo_excel, transforma_em_um_unico

# Sample data for testing
df1 = pd.DataFrame({"A": [1, 2, 3], "B": ["a", "b", "c"]})
df2 = pd.DataFrame({"A": [4, 5, 6], "B": ["d", "e", "f"]})


@pytest.fixture
def mock_input_folder(tmpdir):
    """
    Fixture to create mock input folder with sample Excel files for testing.
    """
    # Criando arquivos Excel de exemplo para testes
    input_folder = tmpdir.mkdir("input_folder")
    df1.to_excel(
        input_folder.join("file1.xlsx"), index=False
    )  # Retirado engine='openpyxl'
    df2.to_excel(
        input_folder.join("file2.xlsx"), index=False
    )  # Retirado engine='openpyxl'
    return str(input_folder)


@pytest.fixture
def mock_output_folder(tmpdir):
    """Fixture to create a mock output folder for testing."""
    return str(tmpdir.mkdir("output_folder"))


def test_extract(mock_input_folder):
    """Test the extraction of data from the input folder."""
    extracted_data = extract_excel(mock_input_folder)
    assert len(extracted_data) == 2  # Expecting two DataFrames
    assert all(isinstance(df, pd.DataFrame) for df in extracted_data)


def test_extract_no_files(tmpdir):
    """Test extraction functionality with an empty input folder."""
    # Criando uma pasta vazia
    empty_folder = tmpdir.mkdir("empty_folder")
    with pytest.raises(ValueError, match="No Excel files found"):
        extract_excel(str(empty_folder))


def test_transform():
    """Test the transformation of dataframes."""
    data = [df1, df2]
    consolidated_df = transforma_em_um_unico(data)
    assert len(consolidated_df) == 6  # 3 rows from df1 + 3 rows from df2
    assert list(consolidated_df.columns) == ["A", "B"]


def test_transform_empty_list():
    """Test the transformation functionality with an empty list."""
    empty_list = []
    with pytest.raises(ValueError, match="No data to transform"):
        transforma_em_um_unico(empty_list)


def test_load_no_permission(tmpdir):
    """Test the load functionality with a protected output folder."""
    # Supondo que a pasta não tenha permissões de gravação
    protected_folder = tmpdir.mkdir("protected_folder")
    os.chmod(str(protected_folder), 0o444)  # Somente permissões de leitura

    df = pd.DataFrame({"A": [1], "B": ["a"]})
    with pytest.raises(PermissionError):
        load_em_um_novo_excel(df, str(protected_folder), "test.xlsx")


def test_load(mock_output_folder):
    """Test the load functionality."""
    df = pd.concat([df1, df2], axis=0, ignore_index=True)
    output_file_name = "consolidated.xlsx"
    load_em_um_novo_excel(df, mock_output_folder, output_file_name)
    assert os.path.exists(os.path.join(mock_output_folder, output_file_name))

    # Verifying the contents of the loaded file
    loaded_df = pd.read_excel(
        os.path.join(mock_output_folder, output_file_name)
    )  # Retirado engine='openpyxl'
    pd.testing.assert_frame_equal(loaded_df, df)
