import pytest
from random import randint
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QPushButton
from ui.alunos_widgets import NovoAluno
import database

def test_cadastrar_aluno_sucesso(qtbot, qapp, mock_message_box):
    widget = NovoAluno()
    qtbot.addWidget(widget)

    # Dados exclusivos por execução
    cpf_random = f"111.111.111-{randint(10, 99)}"

    qtbot.keyClicks(widget.nome_input, f"Aluno Teste Pytest {cpf_random}")
    widget.data_nasc_input.setDate(QDate(2000, 1, 1))
    qtbot.keyClicks(widget.cpf_input, cpf_random)
    widget.combo_plano.setCurrentIndex(0)
    widget.combo_status.setCurrentIndex(0)

    buttons = widget.findChildren(QPushButton)
    save_button = next((b for b in buttons if "Salvar" in b.text()), None)
    assert save_button is not None

    # Espera sinal de sucesso — se o BD estiver ok, o sinal é emitido
    with qtbot.waitSignal(widget.aluno_salvo, timeout=3000):
        qtbot.mouseClick(save_button, Qt.MouseButton.LeftButton)
