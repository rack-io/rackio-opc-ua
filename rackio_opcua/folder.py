# -*- coding: utf-8 -*-
"""rackio_opcua/folder.py

This module implements the folder class for RackioOPCUA.
"""


class Device:

    def __init__(self, name, server, idx):

        self.name = name
        self.server = server
        self.idx = idx

        self._folder = server.nodes.objects.add_folder(idx, name)