#!/usr/bin/env python
"""
In your collectd python script use this to test it
try:
    import collectd
except ImportError:
    import test_collectd as collectd
"""

class Values:
    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs

    def dispatch(self):
        print(self.kwargs)

class FakeConfig:
    def __init__(self):
        self.children = []

def info(msg):
    print(msg)

def register_config(callback):
    callback(FakeConfig())

def register_read(method, interval):
    method()
    print(interval)
