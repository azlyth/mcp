#!/usr/bin/env python
# -*- coding: utf-8 -*-

import blessed
from terminaltables import SingleTable

from .utils import Timer


# Times are in seconds
REDRAW_INTERVAL = 1
INPUT_TIMEOUT = 0.1


class Drawer:

    @classmethod
    def box(cls, width, height, title=''):
        table_structure = [[' ' * (width - 2)] for x in range(height - 2)]

        table = SingleTable(table_structure, ' {} '.format(title))
        table.inner_row_border = False
        table.inner_heading_row_border = False

        return table.table


class MasterControlProgram:

    @classmethod
    def boot(cls):
        instance = cls()
        instance.keep_drawing()
        return instance

    def __init__(self):
        self.term = blessed.Terminal()
        self.timer = Timer()
        self.running = True

    def keep_drawing(self):
        while self.running:
            self.draw()
            self.handle_input()

    def handle_input(self):
        # Get the key entered
        with self.term.cbreak():
            key_entered = self.term.inkey(INPUT_TIMEOUT)

        # Handle the input
        {
            'q': self.stop,
        }.get(key_entered, self.do_nothing)()

    def redraw_required(self):
        return self.timer.reset_if_elapsed(REDRAW_INTERVAL)

    def draw_box(self, width, height, x, y, title=''):
        # Get the box
        box = Drawer.box(width, height, title=title)

        # Split the box into lines and move to the right starting cursor
        # position before drawing the line
        for i, line in enumerate(box.split('\n')):
            move = self.term.move(y + i, x)
            print(move + line)

    def draw(self):
        # The respective subtractions of 1 and 2 are done to the height and
        # width because it seems those are the workable sizes
        full_height = self.term.height - 1
        full_width = self.term.width - 2
        half_height = int(full_height / 2)
        half_width = int(full_width / 2)

        with self.term.hidden_cursor(), self.term.fullscreen():
            # Draw the boxes
            self.draw_box(half_width - 1, half_height, 0, 0, title='First')
            self.draw_box(half_width - 1, half_height, half_width + 1, 0, title='Second')
            self.draw_box(full_width, half_height, 0, half_height, title='Third')

    def do_nothing(self):
        pass

    def stop(self):
        self.running = False
