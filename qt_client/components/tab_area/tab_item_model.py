from PyQt5.QtCore import Qt
from PyQt5.QtCore import (QObject, pyqtSignal,
                          QAbstractListModel, QVariant, QModelIndex,
                          pyqtProperty, pyqtSlot)

from .tab_item import TabItem
from ..data_list.data_item_model import DataItemModel


class TabItemModel(QAbstractListModel):
    TabRole = Qt.UserRole + 1

    def __init__(self, *args, **kwargs):
        super(TabItemModel, self).__init__(*args, **kwargs)

        self._tabs = []

    @pyqtSlot()
    def new_tab(self):
        self.insertRow(len(self._tabs))

    def roleNames(self):
        return {
            self.TabRole: b'tab'
        }

    def rowCount(self, parent=QModelIndex(), **kwargs):
        return len(self._tabs)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            pass
        elif role == self.TabRole:
            return self._tabs[index.row()]

        return QVariant()

    def insertRow(self, p_int, parent=QModelIndex(), *args, **kwargs):
        self.beginInsertRows(parent, p_int, p_int)
        self.setData(self.createIndex(len(self._tabs), 0), TabItem(DataItemModel(), "Untitled {}".format(len(self._tabs) + 1)))
        self.endInsertRows()

        return True

    @pyqtSlot(int)
    def removeRow(self, p_int, parent=QModelIndex(), *args, **kwargs):
        self.beginRemoveRows(parent, p_int, p_int)
        self._tabs.pop(p_int)
        self.endRemoveRows()

        return True

    def setData(self, index, value, *args, **kwargs):
        if not index.isValid():
            return False

        if not 0 <= index.row() < self.rowCount():
            self._tabs.append(value)
        else:
            self._tabs[index.row()] = value

        return True