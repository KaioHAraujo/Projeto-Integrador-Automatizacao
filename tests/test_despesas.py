import pytest
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton
from ui.despesas_widget import Despesas
import database
import sqlite3

def test_adicionar_despesa_sucesso(qtbot, qapp, mock_message_box, tmp_path, monkeypatch):
    # Força banco em memória (evita "database is locked")
    monkeypatch.setattr(database, "connect", lambda: sqlite3.connect(":memory:"))
    database.criar_tabelas()

    widget = Despesas()
    qtbot.addWidget(widget)

    buttons = widget.findChildren(QPushButton)
    add_button = next((b for b in buttons if "Adicionar Despesa" in b.text()), None)
    assert add_button is not None

    # Aguarda sinal despesa_salva — deve ser emitido sem bloqueio
    with qtbot.waitSignal(widget.despesa_salva, timeout=4000):
        qtbot.mouseClick(add_button, Qt.MouseButton.LeftButton)
