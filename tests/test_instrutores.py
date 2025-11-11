import pytest
from random import randint
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QPushButton
from ui.instrutores_widget import NovoInstrutor
import database
import sqlite3

def test_cadastrar_instrutor_sucesso(qtbot, qapp, mock_message_box, monkeypatch):
    # Garante banco limpo em memória
    monkeypatch.setattr(database, "connect", lambda: sqlite3.connect(":memory:"))
    database.criar_tabelas()

    widget = NovoInstrutor()
    qtbot.addWidget(widget)

    cpf_random = f"222.222.222-{randint(10, 99)}"
    qtbot.keyClicks(widget.nome_input, f"Instrutor Teste Pytest {cpf_random}")
    widget.data_nasc_input.setDate(QDate(1990, 5, 15))
    qtbot.keyClicks(widget.cpf_input, cpf_random)
    qtbot.keyClicks(widget.esp_input, "Natação Teste")

    buttons = widget.findChildren(QPushButton)
    save_button = next((b for b in buttons if "Salvar" in b.text()), None)
    assert save_button is not None

    with qtbot.waitSignal(widget.instrutor_salvo, timeout=4000):
        qtbot.mouseClick(save_button, Qt.MouseButton.LeftButton)
