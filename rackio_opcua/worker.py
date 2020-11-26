# -*- coding: utf-8 -*-
"""rackio_opcua/worker.py

This module implements the worker for RackioOPCUA.
"""
import time

from threading import Thread


class OCPUAWorker(Thread):

    def __init__(self, updaters, *args, **kwargs):

        super(OCPUAWorker, self).__init__(*args, **kwargs)

        self.updaters = updaters

    def run(self):

        for updater in self.updaters:

            updater.start()

        while True:

            time.sleep(0.25)

