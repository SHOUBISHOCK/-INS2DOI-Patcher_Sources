import os
import webbrowser

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QFrame,
)

from resources.texts import MAIN_TEXT


class MainPage(QWidget):
    """Home/launcher page.

    The original project included scan/patcher/disabler flows.
    Per request, this trimmed version keeps only the Server Spam Blocker
    and the informational/credits/support UI.
    """

    def __init__(self, go_blocker, go_home):
        super().__init__()
        self.go_blocker = go_blocker
        self.go_home = go_home

        self.init_ui()

    # ---------------------------------------------------------
    # UI Setup
    # ---------------------------------------------------------
    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(10)

        title = QLabel("INS2DOI Community Patcher")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #FFD700;")
        layout.addWidget(title)

        subtitle = QLabel("⚠️ Please run as Administrator")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: orange;")
        layout.addWidget(subtitle)

        # Intro text from resources
        desc_frame = QFrame()
        desc_frame.setFrameShape(QFrame.StyledPanel)
        desc_frame.setStyleSheet("QFrame{background-color:#111;border:1px solid #444;border-radius:6px;}")
        desc_layout = QVBoxLayout(desc_frame)
        desc_layout.setContentsMargins(10, 10, 10, 10)

        self.desc_box = QTextEdit()
        self.desc_box.setReadOnly(True)
        self.desc_box.setPlainText(MAIN_TEXT)
        self.desc_box.setStyleSheet(
            "background-color:transparent; color:#ccc; font-family:Consolas; "
            "font-size:12px; border:0px;"
        )
        desc_layout.addWidget(self.desc_box)
        layout.addWidget(desc_frame, 1)

        # Actions row (no scan / patcher / disabler)
        actions = QHBoxLayout()
        actions.setSpacing(10)

        self.btn_blocker = QPushButton("Open Server Spam Blocker")
        self.btn_blocker.clicked.connect(self.go_blocker)
        self.btn_blocker.setStyleSheet("background-color:#2c2c2c; color:#ffcc00; height:30px;")
        actions.addWidget(self.btn_blocker, 2)

        self.btn_support = QPushButton("💖 Support Us")
        self.btn_support.clicked.connect(self.show_support)
        self.btn_support.setStyleSheet("background-color:#2c2c2c; color:white; height:30px;")
        actions.addWidget(self.btn_support, 1)

        self.btn_credits = QPushButton("Credits")
        self.btn_credits.clicked.connect(self.show_credits)
        self.btn_credits.setStyleSheet("background-color:#2c2c2c; color:white; height:30px;")
        actions.addWidget(self.btn_credits, 1)

        self.btn_exit = QPushButton("Exit")
        self.btn_exit.clicked.connect(self.close_app)
        self.btn_exit.setStyleSheet("background-color:#2c2c2c; color:white; height:30px;")
        actions.addWidget(self.btn_exit, 1)

        layout.addLayout(actions)

        self.setLayout(layout)

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------
    def close_app(self):
        os._exit(0)

    def show_credits(self):
        QMessageBox.information(
            self,
            "CREDITS",
            (
                "CREDITS:\n"
                "DeltaMike (contributor)\n"
                "ChrisTX (coder tips)\n"
                "SHOUBI (publishing)\n"
                "OnSync (.bat installers clarification)\n"
                "Rafai (original workaround idea)\n"
                "Bouncy-Henky‼ (spam filter web server)\n"
                "E.G.Cage (all in one patcher coding)\n"
            ),
        )

    def show_support(self):
        # Open website directly when button is pressed
        webbrowser.open("https://mygamingedge.online/")
        # (No log on the trimmed launcher page)
