import pytest
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QListWidgetItem, QPushButton, QTextEdit, QLineEdit
from ui.condicao_fisica_widget import CondicaoFisica
import database

def test_salvar_condicao_saude(qtbot, qapp, mock_message_box):
    widget = CondicaoFisica()
    qtbot.addWidget(widget)

    qtbot.waitUntil(lambda: widget.lista_alunos.count() > 0, timeout=2000)

    widget.lista_alunos.setCurrentRow(0)
    selected_item = widget.lista_alunos.currentItem()
    assert selected_item is not None

    qtbot.keyClicks(widget.condicao_edit, "Asma Leve (Teste)")
    qtbot.keyClicks(widget.alergias_edit, "Poeira (Teste)")
    qtbot.keyClicks(widget.contato_edit, "Contato Teste")
    qtbot.keyClicks(widget.telefone_edit, "99999-0000")

    buttons = widget.findChildren(QPushButton)
    save_button = next((b for b in buttons if b.text() == "Salvar Ficha"), None)
    assert save_button is not None

    qtbot.mouseClick(save_button, Qt.MouseButton.LeftButton)

def test_filtro_alunos_condicoes(qtbot, qapp):
    widget = CondicaoFisica()
    qtbot.addWidget(widget)
    qtbot.waitUntil(lambda: widget.lista_alunos.count() > 0, timeout=1000)

    test_name = "Aluno Teste Filtro"
    found = False
    for i in range(widget.lista_alunos.count()):
        if test_name in widget.lista_alunos.item(i).text():
            found = True
            break
    if not found:
        item = QListWidgetItem(test_name)
        item.setData(Qt.ItemDataRole.UserRole, 999)
        widget.lista_alunos.addItem(item)

    initial_visible_count = sum(1 for i in range(widget.lista_alunos.count()) if not widget.lista_alunos.item(i).isHidden())
    qtbot.keyClicks(widget.filtro_aluno, test_name.lower()[:5])

    visible_count_after_filter = 0
    filtered_item_visible = False
    for i in range(widget.lista_alunos.count()):
        item = widget.lista_alunos.item(i)
        if not item.isHidden():
            visible_count_after_filter += 1
            if test_name in item.text():
                filtered_item_visible = True

    assert visible_count_after_filter <= initial_visible_count
    assert filtered_item_visible
