import time

import keyboard
import win32com.client

dm = win32com.client.Dispatch(r"dm.dmsoft")
dm_ret = dm.Reg("dudao47a4e02c6713777c8593243cce8488b1", "")


def show_window_by_process():
    hwnd = dm.FindWindow("Chrome_WidgetWin_1", "Cocos Creator")
    dm.SetWindowState(hwnd, 1)
    dm.KeyDown(17)
    dm.KeyDown(83)
    dm.SetWindowState(hwnd, 3)
    dm.KeyUp(17)
    dm.KeyUp(83)


if __name__ == '__main__':
    keyboard.add_hotkey('ctrl+s', show_window_by_process)
    keyboard.wait()
