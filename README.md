# Disclaimer ⚠️
There are versions for chromium/Google Chrome that work better than others.
Here is a rough overview when this tool worked or was unnecessary:

- pre 83.x: Dragging is not working flawlessly, this tool was born to work
  around the issues
- 83.x–95.0.4630.0: Perfect window dragging, no tool assist needed
- 95.0.4630.0–97.0.4692.99: Major breakage in dragging, this tool cannot fix it
- 97.0.4692.99+: Dragging works like pre 83.x again, tool can work again, but
  it's not perfect
- around 100: It broke again see Issues
  [#5](https://github.com/Syphdias/i3-chrome-tab-dragging/issues/5) and
  [#6](https://github.com/Syphdias/i3-chrome-tab-dragging/issues/6)
- ~103: Works like pre 83.x again, tool can work again, but it's not perfect

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

For Arch Linux, there is a package in the AUR: https://aur.archlinux.org/packages/python-i3-chrome-tab-dragging-git

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
