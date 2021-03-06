# ⚠ Deprecation
With version 83 chromium has changed the way tab dragging works. This makes this
little tool unnecessary.

# Description – What it does
This script aims to solve a problem I have with dragging Chrome tabs while using
the i3 window manager where it can be hard to place a second tab into another
Chrome window. If it detects a Chrome window has been opened while the user is
dragging (left mouse button is being pressed down), it switches the new window to 
floating mode so it can easily and independently be dragged to another Chrome window. 
If the mouse is released without the window being droped in another chrome window,
floating is toggled off, so the window will receive it's own new tile.

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


# Without and With
Without `i3-chrome-tab-dragging.py`:
![without](https://user-images.githubusercontent.com/16988672/77919224-300fdf80-729d-11ea-8c8a-c1c0c3f9c2fb.gif)

With `i3-chrome-tab-dragging.py`:
![with](https://user-images.githubusercontent.com/16988672/77919232-31d9a300-729d-11ea-8404-7623b5017615.gif)


# Issues
currently none
 
# Contributing
You are very welcome to contribute by PR or Issue to report wishes or bugs.
Please honor PEP-8 if you open a PR, but don't worry if you don't know it, I
will fix it for you.
