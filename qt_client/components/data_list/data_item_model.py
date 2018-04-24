import numpy as np
from PyQt5.QtQml import QQmlListProperty

from qml_client.hub import Hub, Message

from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt, QVariant, pyqtSlot

from .data_items import DataItem


class DataItemModel(QAbstractListModel):
    ItemRole = Qt.UserRole + 1

    def __init__(self, *args, **kwargs):
        super(DataItemModel, self).__init__(*args, **kwargs)

        self._items = [
            DataItem(name="My data {}".format(np.random.randint(0, 100)), color="cyan", parent=self),# model=PlotDataModel()),
            DataItem(name="My data {}".format(np.random.randint(0, 100)), color="blue", parent=self)#model=PlotDataModel())
        ]

        # The data model needs to listen for add data events
        self._hub = Hub()
        # self._hub.subscribe(AddDataMessage, self.add_data, self)
        # self._hub.subscribe(AddPlotDataMessage, self.add_data, self)

    def roleNames(self):
        return {
            self.ItemRole: b'item'
        }

    def rowCount(self, parent=QModelIndex(), **kwargs):
        return len(self._items)

    @pyqtSlot(int, result=DataItem)
    def at(self, index):
        return self._items[index]

    def data(self, index, role):
        if role == self.ItemRole:
            return self._items[index.row()]

        return QVariant()

    def insertRow(self, row, parent=QModelIndex(), **kwargs):
        self.beginInsertRows(parent, row, row + 1)
        self._items.insert(row, DataItem(name="New data item", color="black"))
        self.endInsertRows()

    def insertRows(self, row, count, parent=QModelIndex(), **kwargs):
        self.beginInsertRows(parent, row, row + count - 1)
        for i in count:
            self._items.insert(row + i, DataItem(name="New data item", color="black"))
        self.endInsertRows()

    @pyqtSlot(int)
    def removeRow(self, p_int, parent=QModelIndex(), *args, **kwargs):
        self.beginRemoveRows(parent, p_int, p_int)
        self._items.pop(p_int)
        self.endRemoveRows()

        return True

    def removeRows(self, p_int, p_int_1, parent=QModelIndex(), *args, **kwargs):
        self.beginRemoveRows(parent, p_int, p_int_1)
        del self._items[p_int:p_int_1 + 1]
        self.endRemoveRows()

        return True

    def setData(self, index, value, *args, **kwargs):
        # if not index.isValid():
        #     return False

        if not 0 <= index.row() < self.rowCount():
            self._items.append(value)
        else:
            self._items[index.row()] = value

        return True