# Description – What it does
This script aims to solve a problem I have with dragging Chrome tabs while using
the i3 window manager where it can be hard to place a second tab into another
Chrome window. If it detects a Chrome window with the same title has been opened
twice in a row (except for a "New Tab"), it switches the new window to floating
mode so it can easily and independently be dragged to another Chrome window. This
preserves the usual way of dragging a tab to another tile but also enables to
get automatic floating mode if the window snaps to toe wrong place.


# Installation
- make sure all requirements are installed
```
pip install --user -r requirements.txt
```
- copy script to your place of choice, e.g. `~/.i3/i3-chrome-tab-dragging.py`
- add this to i3 config:
```
exec_always --no-startup-id ~/.i3/i3-chrome-tab-dragging.py
```


# Issues
- I have no idea how I could detect a "tab dragging" before it opens a new i3
  window.
- After dragging the tab that has last been moved, it will instantly go to
  floating mode.
- The way this detects a "New Tab" from Chrome in a new window is based on the
  title string. If this changes in a future (or past) version. This will break
  and has to be expanded on.
- Doesn't work for Firefox or other Browsers (feel free to open an PR if you
  have a solution)
- Should there be an option to float instantly?
- aio?


# Contributing
You are very welcome to contribute by PR or Issue to report wishes or bugs.
Please honor PEP-8 if you open a PR, but don't worry if you don't know it, I
will fix it for you.
