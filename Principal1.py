from datetime import datetime

hojeD = int(datetime.now().strftime('%d'))
hojeM = int(datetime.now().strftime('%m'))
hojeY = int(datetime.now().strftime('%Y'))
Hoje = (hojeD * 24) + (hojeM * 730) + (hojeY * 8760)

limiteD = 9
limiteM = 12
limiteY = 2021
limite = (limiteD * 24) + (limiteM * 730) + (limiteY * 8760)

if Hoje >= limite:
    import os
    import sys
    import time

    import win32con
    from win32api import *
    from win32gui import *


    class WindowsBalloonTip:
        def __init__(self, title, msg):
            message_map = {
                win32con.WM_DESTROY: self.OnDestroy,
            }

            wc = WNDCLASS()
            hinst = wc.hInstance = GetModuleHandle(None)
            wc.lpszClassName = "PythonTaskbar"
            wc.lpfnWndProc = message_map
            classAtom = RegisterClass(wc)

            style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
            self.hwnd = CreateWindow(classAtom, "Taskbar", style,
                                     0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
                                     0, 0, hinst, None)
            UpdateWindow(self.hwnd)
            iconPathName = os.path.abspath(os.path.join(sys.path[0], "balloontip.ico"))
            icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
            try:
                hicon = LoadImage(hinst, iconPathName,
                                  win32con.IMAGE_ICON, 0, 0, icon_flags)
            except:
                hicon = LoadIcon(0, win32con.IDI_APPLICATION)
            flags = NIF_ICON | NIF_MESSAGE | NIF_TIP
            nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "tooltip")
            Shell_NotifyIcon(NIM_ADD, nid)
            Shell_NotifyIcon(NIM_MODIFY,
                             (self.hwnd, 0, NIF_INFO, win32con.WM_USER + 20,
                              hicon, "Balloon  tooltip", msg, 200, title))

            time.sleep(10)
            DestroyWindow(self.hwnd)

        def OnDestroy(self):
            nid = (self.hwnd, 0)
            Shell_NotifyIcon(NIM_DELETE, nid)
            PostQuitMessage(0)


    def balloon_tip(title, msg):
        w = WindowsBalloonTip(title, msg)


    if __name__ == '__main__':
        balloon_tip("Data de manutenção vencida",
                    "O prazo da sua manutenção foi vencida,"
                    " entre em contato com MasterTech Soluções em Informática para a "
                    "manutenção de seu computador.\n"
                    "-(99) 99999-9999")
