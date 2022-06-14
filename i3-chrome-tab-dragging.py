#!/usr/bin/env python3
# vi:expandtab tabstop=4
# This is intended to be run when i3 starts it will exit on restart; make sure
# to use "exec_always --no-startup-id" to run this
from argparse import ArgumentParser
from pynput.mouse import Listener, Button
from i3ipc import Connection, Event

# Constants
browser_classes = [
    "Google-chrome",
    "Google-chrome-beta",
    "Google-chrome-unstable",
    "Chromium",
    "Chromium-browser",
    "Brave-browser",
]

# Global Variables
mouse_pressed = False
current_window = None

# Called by mouse listener when the mouse is clicked
def on_click(x, y, button, pressed):
    global mouse_pressed
    global current_window

    # we want to store the status of the left mouse button
    if button == Button.left:
        mouse_pressed = pressed

        # if the button is released and we were currently dragging a window, unfloat it
        if not pressed and current_window:
            current_window.command('floating disable')
            current_window = None

# Called by i3 when a new window is created
def on_window_new(i3, e):
    global current_window

    # we only care about chromium windows
    if e.container.window_class in browser_classes:
        # only switch to floating mode if the user is currently dragging (=mouse button pressed)
        if mouse_pressed:
            e.container.command('floating enable')

            # store the reference to the window, so we can unfloat it later
            current_window = e.container


def main(args):
    i3 = Connection()
    i3.on(Event.WINDOW_NEW, on_window_new)

    with Listener(on_click=on_click) as listener:
        i3.main()


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-v", "--verbose", action="count")
    args = parser.parse_args()

    main(args)
