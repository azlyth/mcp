#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time


class Timer:

    def __init__(self):
        self.reset()

    def seconds_elapsed(self):
        return time.time() - self.time

    def reset(self):
        self.time = time.time()

    def reset_if_elapsed(self, seconds):
        if self.seconds_elapsed() > seconds:
            self.reset()
            return True
        return False
