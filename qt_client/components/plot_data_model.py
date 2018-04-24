import numpy as np
from PyQt5.QtCore import (QAbstractTableModel, QModelIndex, QObject, Qt,
                          QVariant, pyqtProperty, pyqtSignal, pyqtSlot)

from ..hub import Hub, Message


class PlotDataModel(QAbstractTableModel):
    # DataRole = Qt.UserRole + 1

    def __init__(self, *args, **kwargs):
        super(PlotDataModel, self).__init__(*args, **kwargs)

        self._data = list(zip(np.arange(100), np.random.sample(100)))

        # The data model needs to listen for add data events
        self._hub = Hub()
        # self._hub.subscribe(AddDataMessage, self.add_data, self)
        # self._hub.subscribe(AddPlotDataMessage, self.add_data, self)

    # def roleNames(self):
    #     return {
    #         self.DataRole: b'data'
    #     }

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self._data)

    def columnCount(self, parent=None, *args, **kwargs):
        return 2

    def data(self, index, role=None):
        return self._data[index.row()][index.column()]
        # if role == self.DataRole:
        #     return self._data[index.row()]
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        elif role == Qt.EditRole:
            return self._data[index.row()][index.column()]

        return QVariant()
