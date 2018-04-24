import logging
logging.basicConfig(level=logging.INFO)

import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication, QMainWindow

from .client import launch

from .hub import HubProxy
from .components.tab_area.tab_item_model import TabItemModel


def start(server_ip=None, client_ip=None):
    # Start the server connections
    launch(server_ip=server_ip,
           client_ip=client_ip)

    # Start the application
    app = QApplication(sys.argv)

    w = QMainWindow()

    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())