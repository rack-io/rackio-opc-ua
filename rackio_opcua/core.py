# -*- coding: utf-8 -*-
"""rackio_opcua/core.py

This module implements the core app class and methods for Rackio OPC-UA.
"""

import json

from ._singleton import Singleton


class OPCUACore(Singleton):

    def __init__(self):

        super(OPCUACore, self).__init__()

        self.app = None
        self.port = None

    def define_mapping(self, tag, mode, period=0.25):

        pass

    def define_device(self, device_name):

        pass

    def define_folder(self, folder_name):

        pass

    def __call__(self, app=None, port=4840, period=0.25):

        if not app:
            return self

        self.period = period
        
        self.app = app
