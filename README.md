# Darkify
Darkify – Because your screen doesn’t need to be the sun. A hotkey-powered dimmer overlay for stealth mode in class, cafes, or anywhere brightness equals attention. Built to reduce glow, not judgment. Ctrl+Alt+D your way to peace.

# 💡 Dimmer - Screen Overlay Brightness Controller

**Dimmer** is a lightweight Windows utility that adds a black transparent overlay to your screen, helping reduce eye strain in low-light environments. With global hotkeys and system tray support, it’s built for convenience and simplicity.

### 🔧 Features

- 🌓 Adjustable screen dimming overlay
- 🎚️ Change brightness using hotkeys
- 🖱️ Tray icon with tooltips
- ⚡ Toggle overlay anytime
- 📦 Available as a standalone `.exe` (no install required)

---
## 🛠️ Usage Instructions

- Download the `.exe` from the [Releases](https://github.com/TechFreak1000/Darkify/releases) page  
- Double-click to run  
- App will start in background – it won't show a popup or window  
- Use the hotkey `Ctrl + Shift + D` to toggle dimming  
- Right-click the tray icon to adjust brightness or exit


## ⚠️ Note

**Don’t panic if nothing happens when you run it!**  
There’s no splash screen or message — but it *is* running in the background.  
Just press `Ctrl + Shift + D` or check the system tray (near the clock) for a new icon.  
That’s your ninja-mode dimmer in action.

---

### ⚙️ Controls

| Action                      | Shortcut             |
|----------------------------|----------------------|
| Toggle Dimmer              | `Ctrl + Alt + D`     |
| Increase Brightness        | `Ctrl + Alt + ↑`     |
| Decrease Brightness        | `Ctrl + Alt + ↓`     |
| Exit App                   | `Ctrl + Alt + X`     |

---

### 🛠️ Tech Stack

- Python 3
- `pywin32` – Win32 API access
- `pystray` – System tray integration
- `PIL` – Icon drawing
- `Auto Py to Exe` – For generating `.exe`

---

### 💻 Running from Source

#### Prerequisites

Install dependencies:

```bash
pip install pywin32 pystray pillow
python dimmer.py

📦 Download .exe
Don't want to mess with Python?

👉 Download the latest release here
https://github.com/TechFreak1000/Darkify/releases/download/v3.0/Dim_scr_v3.0.exe

🔐 Permissions
The script uses Win32 API and may require admin rights on some systems.

🙋‍♂️ Author
Made by Rudrang Darade
"For those who like their screens chill and their vibes chill-er."

📃 License
MIT License. Free to use and modify.

