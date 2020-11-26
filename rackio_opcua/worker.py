# -*- coding: utf-8 -*-
"""rackio_opcua/worker.py

This module implements the worker for RackioOPCUA.
"""
import time

from threading import Thread


class SocketWorker(Thread):

    def __init__(self, updaters, *args, **kwargs):

        super(SocketWorker, self).__init__(*args, **kwargs)

        self.updaters = updaters

    def run(self):

        while True:

            for updater in self.updaters:

                updater.start()

            time.sleep(0.25)

