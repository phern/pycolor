
<img width="660" height="162" alt="image" src="https://github.com/user-attachments/assets/bda9ae8c-3db6-4431-9b7c-e5c806b5a5f0" />



## Obligatory Too Long Backstory

  The project started because of my interest in colorbots (pixelbots) being
used to cheat in online video games. Many competitive shooters implement anti cheat software that scans for signatures of software
that has been injected into the games process (such as DLL injection) or processes currently in memory. 
The ability of an anti cheat to detect memory signatures injected into a games process
can be entirely circumvented by simply not injecting into memory at all.

Colorbots rapidly search the screen for a specific color or color pattern and perform an action based on what color was found. If
the enemy health bar is always red, it could find the location of it on the screen and then move your crosshair
to a slightly offset location, like their head. Pycolor started so I could learn about how colorbots are made without actually cheating.

   **TL:DR** Pycolor started so I could learn about how these colorbots are made without actually cheating.

## Features
<img width="330" height="147" alt="image" src="https://github.com/user-attachments/assets/2f96aee8-9d0b-42fc-8ef6-e1bff2d3dd7c" />

* Calculate the average RGB color of a selected screen region
* Search a selected region for a specific RGB value
* Eyedropper with real time color output
* Interactive terminal interface through Rich

### Requirements

* Python 3.12+
* [uv](https://docs.astral.sh/uv/) recommended for dependency and environment management

### Installation

Clone the repository:

```bash
git clone https://github.com/phern/pycolor.git
cd pycolor
```

Install the project and its dependencies:

```bash
uv sync
```

### Usage


```bash
uv run pycolor
```

Follow the on screen prompts

### Project Status

`pycolor` was made just for fun, I do not intend to spend significant time updating or maintaining it.

### Built With

pycolor is built with Python and several open-source libraries for screen capture, input handling, and terminal presentation.

* **PyAutoGUI** - screenshots, pixel inspection, mouse position, and desktop interaction
* **PyDirectInput** - direct mouse input
* **pynput** - mouse event listening
* **Rich** - terminal menus, prompts, panels, and live output
* **PyWinCtl** - desktop window management
* **Pillow** - image representation and pixel-level image processing
* **PyScreeze** - screenshot-related functionality used by the desktop automation stack

Dependency and project management is handled with uv.

