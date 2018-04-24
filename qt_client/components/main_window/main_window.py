import os

from PyQt5.QtWidgets import QMainWindow, QTabBar, QPushButton
from PyQt5.uic import loadUi

from .. import resources

from ..data_list.data_item_model import DataItemModel
from ..data_list.data_delegates import DataItemDelegate

__all__ = ['MainWindow']


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Load the ui file and attached it to this instance
        loadUi(os.path.join(os.path.dirname(__file__), "ui", "main_window.ui"),
               self)

        # Set the tabs to be expanding; os-specific
        self.tab_widget.tabBar().setExpanding(True)

        # Create a button on the tab widget
        # add_button = QPushButton(self)
        # self.tab_widget.tabBar().setTabButton(0, QTabBar.LeftSide, add_button)

        # Create the tab item model
        self._data_item_model = DataItemModel()

        # Set delegates
        # self.list_view.setItemDelegate(DataItemDelegate())

        self.list_view.setModel(self._data_item_model)
