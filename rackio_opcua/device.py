# -*- coding: utf-8 -*-
"""rackio_opcua/device.py

This module implements the device class for RackioOPCUA.
"""


class Device:

    def __init__(self, name, server, idx):

        self.name = name
        self.server = server
        self.idx = idx

        self._device = server.nodes.base_object_type.add_object_type(idx, name)

        self.mappings = list()

    def define_mapping(self, tag, mode, period=0.25):

        pass