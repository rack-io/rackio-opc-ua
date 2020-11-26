# -*- coding: utf-8 -*-
"""rackio_opcua/folder.py

This module implements the folder class for RackioOPCUA.
"""

from .updater import TagUpdater
from .device import Device

class Folder:

    def __init__(self, name, server, idx):

        self.name = name
        self.server = server
        self.idx = idx

        self._folder = server.nodes.objects.add_folder(idx, name)

        self.devices = list()

    def define_device(self, name):

        server = self.server
        idx = self.idx

        device = Device(name, server, idx)

        self.devices.append(device)

        return device
    