import pytest
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton
from ui.ponto_widgets import FolhaDePonto
import database

def test_registrar_entrada_ponto(qtbot, qapp, mock_message_box):
    widget = FolhaDePonto()
    qtbot.addWidget(widget)

    buttons = widget.findChildren(QPushButton)
    entry_button = next((b for b in buttons if b.text() == "Registrar Entrada"), None)
    assert entry_button is not None

    # Espera o sinal ser emitido (sem abrir diálogo)
    with qtbot.waitSignal(widget.ponto_registrado, timeout=3000):
        qtbot.mouseClick(entry_button, Qt.MouseButton.LeftButton)

def test_registrar_saida_ponto(qtbot, qapp, mock_message_box):
    widget = FolhaDePonto()
    qtbot.addWidget(widget)

    buttons = widget.findChildren(QPushButton)
    exit_button = next((b for b in buttons if b.text() == "Registrar Saída"), None)
    assert exit_button is not None

    with qtbot.waitSignal(widget.ponto_registrado, timeout=3000):
        qtbot.mouseClick(exit_button, Qt.MouseButton.LeftButton)
