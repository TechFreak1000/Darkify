import win32api
import win32con
import win32gui
import ctypes
import ctypes.wintypes
import threading


# Config
CLASS_NAME = "DimOverlayWindow"
MIN_ALPHA = 50
MAX_ALPHA = 255
STEP = 15
default_alpha = 128

# Global vars
overlay_hwnd = None
current_alpha = default_alpha
overlay_visible = False

# Win32 handles
user32 = ctypes.windll.user32

# Hotkey IDs
HK_EXIT = 1
HK_TOGGLE = 2
HK_BRIGHT_UP = 3
HK_BRIGHT_DOWN = 4

def wnd_proc(hwnd, msg, wparam, lparam):
    if msg == win32con.WM_PAINT:
        hdc, ps = win32gui.BeginPaint(hwnd)
        brush = win32gui.CreateSolidBrush(win32api.RGB(0, 0, 0))
        rect = win32gui.GetClientRect(hwnd)
        win32gui.FillRect(hdc, rect, brush)
        win32gui.EndPaint(hwnd, ps)
        return 0
    return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

def register_window_class():
    hInstance = win32api.GetModuleHandle()
    wndClass = win32gui.WNDCLASS()
    wndClass.lpfnWndProc = wnd_proc
    wndClass.hInstance = hInstance
    wndClass.lpszClassName = CLASS_NAME
    try:
        win32gui.RegisterClass(wndClass)
    except:
        pass

def create_overlay(alpha):
    global overlay_hwnd
    hInstance = win32api.GetModuleHandle()
    hwnd = win32gui.CreateWindowEx(
        win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT | win32con.WS_EX_TOPMOST,
        CLASS_NAME,
        None,
        win32con.WS_POPUP,
        0, 0,
        win32api.GetSystemMetrics(0),
        win32api.GetSystemMetrics(1),
        None, None,
        hInstance, None
    )
    win32gui.SetLayeredWindowAttributes(hwnd, 0, alpha, win32con.LWA_ALPHA)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
    win32gui.UpdateWindow(hwnd)
    overlay_hwnd = hwnd

def destroy_overlay():
    global overlay_hwnd
    if overlay_hwnd and win32gui.IsWindow(overlay_hwnd):
        win32gui.DestroyWindow(overlay_hwnd)
        overlay_hwnd = None

def update_overlay_alpha(alpha):
    global overlay_hwnd
    if overlay_hwnd and win32gui.IsWindow(overlay_hwnd):
        win32gui.SetLayeredWindowAttributes(overlay_hwnd, 0, alpha, win32con.LWA_ALPHA)

def register_hotkeys():
    user32.RegisterHotKey(None, HK_EXIT, win32con.MOD_CONTROL | win32con.MOD_ALT, ord('X'))
    user32.RegisterHotKey(None, HK_TOGGLE, win32con.MOD_CONTROL | win32con.MOD_ALT, ord('D'))
    user32.RegisterHotKey(None, HK_BRIGHT_UP, win32con.MOD_CONTROL | win32con.MOD_ALT, win32con.VK_UP)
    user32.RegisterHotKey(None, HK_BRIGHT_DOWN, win32con.MOD_CONTROL | win32con.MOD_ALT, win32con.VK_DOWN)

def main():
    global overlay_visible, current_alpha

    register_window_class()
    register_hotkeys()
    print("Dimmer ready.")
    print("   - Ctrl + Alt + D : Toggle Dimmer")
    print("   - Ctrl + Alt + UP / DOWN : Adjust Brightness")
    print("   - Ctrl + Alt + X : Exit App")


    msg = ctypes.wintypes.MSG()
    while user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
        if msg.message == win32con.WM_HOTKEY:
            if msg.wParam == HK_EXIT:
                destroy_overlay()
                break

            elif msg.wParam == HK_TOGGLE:
                if overlay_visible:
                    destroy_overlay()
                    overlay_visible = False
                else:
                    create_overlay(current_alpha)
                    overlay_visible = True

            elif msg.wParam == HK_BRIGHT_UP:
                if overlay_visible and current_alpha > MIN_ALPHA:
                    current_alpha = max(MIN_ALPHA, current_alpha - STEP)
                    update_overlay_alpha(current_alpha)

            elif msg.wParam == HK_BRIGHT_DOWN:
                if overlay_visible and current_alpha < MAX_ALPHA:
                    current_alpha = min(MAX_ALPHA, current_alpha + STEP)
                    update_overlay_alpha(current_alpha)

        user32.TranslateMessage(ctypes.byref(msg))
        user32.DispatchMessageA(ctypes.byref(msg))

    setup_tray()




from pystray import Icon, MenuItem as Item, Menu
from PIL import Image, ImageDraw
import threading

# Function to generate a simple round black icon
def create_icon():
    size = (64, 64)
    image = Image.new('RGB', size, color=(0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.ellipse((16, 16, 48, 48), fill=(100, 100, 100))
    return image

# Function to run tray icon in a separate thread
def setup_tray():
    icon_image = create_icon()

    def on_exit(icon, item):
        destroy_overlay()
        icon.stop()

    menu = Menu(
        Item('Toggle Dimmer (Ctrl+Alt+D)', lambda: None, enabled=False),
        Item('Brightness Up (Ctrl+Alt+↑)', lambda: None, enabled=False),
        Item('Brightness Down (Ctrl+Alt+↓)', lambda: None, enabled=False),
        Item('Exit', on_exit)
    )

    tray_icon = Icon("Dimmer", icon_image, "Screen Dimmer", menu)
    threading.Thread(target=tray_icon.run, daemon=True).start()






if __name__ == "__main__":
    main()
