import six, abc
import logging
from collections import namedtuple
from PyQt5.QtCore import QObject, pyqtSlot

from .singletons import Singleton


Receipt = namedtuple('Receipt', ['handler', 'subscriber', 'filter'])


@six.add_metaclass(Singleton)
class Hub:
    def __init__(self):
        self._subscriptions = {}

    def subscribe(self, message, handler, subscriber, filt=lambda x, y: True):
        if isinstance(message, Message):
            logging.error("Message is not of type {}.".format(Message))
            return

        receipt = Receipt(handler, subscriber, filt)

        self._subscriptions.setdefault(message, []).append(receipt)

    def unsubscribe(self, message, subscriber):
        self._subscriptions.get(message, []).remove(subscriber)

    def publish(self, message, *args, publisher=None, **kwargs):
        logging.info("[client] Sending message {}".format(message))

        subs = self._subscriptions.get(message, [])
        [rec.handler(*args) for rec in subs if rec.filter(message, publisher)]


class HubProxy(QObject):
    """
    Proxy object to communicate between QML and python.
    """
    def __init__(self, *args, **kwargs):
        super(HubProxy, self).__init__(*args, **kwargs)

        self._hub = Hub()

    @pyqtSlot(QObject)
    def item_selected(self, item):
        print("Clicked on item {}.".format(item.name))


class Message:
    AddData = None
    LoadData = None
    NewPlot = None
    AddPlotData = None
    CurrentItemChanged = None
