#!/usr/bin/env python
# -*- coding: utf-8 -*-

import blessed

from .utils import Timer


# Times are in seconds
REDRAW_INTERVAL = 1
INPUT_TIMEOUT = 0.1


class MasterControlProgram:

    @classmethod
    def boot(cls):
        instance = cls()
        instance.keep_drawing()
        return instance

    def __init__(self):
        self.terminal = blessed.Terminal()
        self.timer = Timer()
        self.running = True

    def keep_drawing(self):
        while self.running:
            self.draw()
            self.handle_input()

    def handle_input(self):
        # Get the key entered
        with self.terminal.cbreak():
            key_entered = self.terminal.inkey(INPUT_TIMEOUT)

        # Handle the input
        {
            'q': self.stop,
        }.get(key_entered, self.do_nothing)()

    def redraw_required(self):
        return self.timer.reset_if_elapsed(REDRAW_INTERVAL)

    def draw(self):
        with self.terminal.hidden_cursor(), self.terminal.fullscreen():

            # Centered greeting
            move = self.terminal.move(int(self.terminal.height / 2), 0)
            print(move + self.terminal.center(self.terminal.bold('It\'s working.')))

            # Instruction at the bottom
            move = self.terminal.move(self.terminal.height - 2, 0)
            print(move + self.terminal.center('- press q to quit -'))

    def do_nothing(self):
        pass

    def stop(self):
        self.running = False
