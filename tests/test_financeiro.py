# tests/test_financeiro.py
import pytest
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QPushButton, QTableWidget # Importa as classes
from ui.financeiro_widget import Financeiro
import database

def test_marcar_como_pago(qtbot, qapp, mock_message_box):
    widget = Financeiro()
    qtbot.addWidget(widget)

    qtbot.waitUntil(lambda: widget.table.rowCount() > 0, timeout=1000)

    pay_button = None
    target_row = -1

    # Procura a primeira linha que tenha um botão
    for row in range(widget.table.rowCount()):
        button_widget = widget.table.cellWidget(row, 5) # Coluna de Ações
        if button_widget and isinstance(button_widget, QPushButton):
            status_item = widget.table.item(row, 4) # Coluna de Status
            if status_item and status_item.text() in ["Pendente", "Atrasado"]:
                pay_button = button_widget
                target_row = row
                break # Encontrou um botão válido

    if pay_button:
         with qtbot.waitSignal(widget.mensalidade_paga, timeout=1000):
             qtbot.mouseClick(pay_button, Qt.MouseButton.LeftButton)

         # Verifica se o status mudou para Pago OU se o botão sumiu
         qtbot.waitUntil(lambda: (widget.table.item(target_row, 4) is not None and widget.table.item(target_row, 4).text() == "Pago") or \
                                 (widget.table.cellWidget(target_row, 5) is None),
                         timeout=1000)
    else:
        pytest.skip("Não foi encontrada nenhuma mensalidade pendente/atrasada com botão para testar.")