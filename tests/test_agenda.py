import pytest
from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QPushButton
from ui.agenda_aulas_widget import AgendaAulas
import database

def test_agendar_aula_sucesso(qtbot, qapp, mock_message_box):
    widget = AgendaAulas()
    qtbot.addWidget(widget)

    # Localiza o botão "Agendar Nova Aula"
    buttons = widget.findChildren(QPushButton)
    add_button = next((b for b in buttons if b.text() == "➕ Agendar Nova Aula"), None)
    assert add_button is not None

    # O sinal aula_salva deve ser emitido ao clicar no botão
    with qtbot.waitSignal(widget.aula_salva, timeout=3000):
        qtbot.mouseClick(add_button, Qt.MouseButton.LeftButton)

    # Após salvar, verifica se há pelo menos uma aula agendada
    widget.date_edit.setDate(QDate.currentDate())
    qtbot.waitUntil(lambda: widget.tabela_aulas.rowCount() > 0, timeout=2000)

