import pytest
from PyQt6.QtWidgets import QApplication, QMessageBox
import sys
import os
import sqlite3

# Adiciona o diretório raiz ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="session")
def qapp():
    """Cria a instância QApplication necessária para os testes."""
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    return app

@pytest.fixture
def mock_message_box(monkeypatch):
    """
    Substitui QMessageBox.information/warning/critical por uma função mock.
    Evita bloqueios de pop-ups durante os testes.
    """
    def mock_popup(*args, **kwargs):
        if len(args) > 1:
            print(f"Mock QMessageBox '{args[0].__class__.__name__}': {args[1]} - {args[2]}")
        return QMessageBox.StandardButton.Ok

    monkeypatch.setattr(QMessageBox, "information", mock_popup)
    monkeypatch.setattr(QMessageBox, "warning", mock_popup)
    monkeypatch.setattr(QMessageBox, "critical", mock_popup)

@pytest.fixture(autouse=True)
def reset_database():
    """
    Recria o banco de dados limpo antes de cada teste.
    Evita bloqueios e dados duplicados.
    """
    import database

    # remove o arquivo antigo, se existir
    if os.path.exists("academia.db"):
        os.remove("academia.db")

    # recria o banco vazio e as tabelas
    database.criar_tabelas()
