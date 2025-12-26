from PySide6.QtWidgets import QMainWindow, QStackedWidget

from ui.pages.main_page import MainPage
from ui.pages.blocker_page import BlockerPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("INS2DOI Community Patcher")
        # Main window is now a simple launcher for the remaining tool(s)
        self.resize(900, 560)

        # Initialize pages
        self.main_page = MainPage(
            go_blocker=self.open_blocker,
            go_home=self.go_home,
        )
        self.blocker_page = BlockerPage(back_cb=self.go_home)

        # Central stack
        self.stack = QStackedWidget()
        self.stack.addWidget(self.main_page)
        self.stack.addWidget(self.blocker_page)
        self.setCentralWidget(self.stack)

        self.stack.setCurrentWidget(self.main_page)

    # Navigation
    def go_home(self):
        self.stack.setCurrentWidget(self.main_page)

    def open_blocker(self):
        self.stack.setCurrentWidget(self.blocker_page)
