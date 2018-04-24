import numpy as np
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal, pyqtSlot


class DataItem(QObject):
    nameChanged = pyqtSignal()
    dataChanged = pyqtSignal()
    colorChanged = pyqtSignal()
    visibilityChanged = pyqtSignal()

    def __init__(self, name, color, data=None, *args, **kwargs):
        super(DataItem, self).__init__(*args, **kwargs)

        self._data = data or [[x[0], x[1]] for x in zip(np.arange(200), np.random.sample(200))]
        self._color = color
        self._name = name
        self._visible = True

    @pyqtProperty(str, notify=nameChanged)
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @pyqtProperty(list, notify=dataChanged)
    def data(self):
        return self._data

    @pyqtSlot(int, result=float)
    def x(self, index):
        return list(np.array(self.data)[:, 0])[index]

    @pyqtSlot(int, result=float)
    def y(self, index):
        return list(np.array(self.data)[:, 1])[index]

    @data.setter
    def data(self, value):
        self._data = value

    @pyqtProperty(str, notify=colorChanged)
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @pyqtProperty(bool, notify=visibilityChanged)
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, value):
        self._visible = value
