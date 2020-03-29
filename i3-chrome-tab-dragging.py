#!/usr/bin/env python3
# vi:expandtab tabstop=4
# This is intended to be run when i3 starts it will exit on restart; make sure
# to use "exec_always --no-startup-id" to run this
from i3ipc import Connection, Event

i3 = Connection()
last_new_window_title = ""

# windows with these titles will never be converted to floating
backlisted_window_titles = [
    "New Tab - Google Chrome",
    "New Tab - Chromium",
]

def on_window_new(i3, e): 
    global last_new_window_title
    
    if e.container.window_class in ["Google-chrome", "Chromium-browser"]:
        # only switch to floating mode if the last window had the same name
        if last_new_window_title == e.container.window_title \
                and e.container.window_title not in backlisted_window_titles:
            e.container.command('floating enable')

        # save current title
        last_new_window_title = e.container.window_title


i3.on(Event.WINDOW_NEW, on_window_new) 
i3.main()
