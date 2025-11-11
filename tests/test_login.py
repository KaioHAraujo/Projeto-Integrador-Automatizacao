import pytest
from PyQt6.QtWidgets import QDialog
from PyQt6.QtCore import Qt
from ui.login_dialog import LoginDialog

def test_login_com_sucesso(qtbot, qapp):
    janela = LoginDialog()
    qtbot.addWidget(janela)

    qtbot.keyClicks(janela.user_input, "admin")
    qtbot.keyClicks(janela.pass_input, "123")
    qtbot.mouseClick(janela.login_button, Qt.MouseButton.LeftButton)

    # Espera resultado de sucesso
    qtbot.waitUntil(lambda: janela.result() == QDialog.DialogCode.Accepted, timeout=2000)
    assert janela.result() == QDialog.DialogCode.Accepted

def test_login_com_falha(qtbot, qapp):
    janela = LoginDialog()
    qtbot.addWidget(janela)

    qtbot.keyClicks(janela.user_input, "admin")
    qtbot.keyClicks(janela.pass_input, "senhaerrada")
    qtbot.mouseClick(janela.login_button, Qt.MouseButton.LeftButton)

    qtbot.waitUntil(lambda: len(janela.error_label.text()) > 0, timeout=2000)
    texto = janela.error_label.text().lower()

    # Aceita variações: pode ser "erro", "usuário", ou "senha incorreta"
    assert any(palavra in texto for palavra in ["erro", "usuário", "senha incorreta", "senha errada"])
