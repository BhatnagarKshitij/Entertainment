import ctypes

MB_OK = 0x0
MB_OKCXL = 0x01
MB_YESNOCXL = 0x03
MB_YESNO = 0x04
MB_HELP = 0x4000
ICON_EX=0x30
ICON_INFO = 0x40
ICON_STOP = 0x10 
ICON_QUESTION=0x20

ctypes.windll.user32.MessageBoxW(1, "Your PC has been HACKED!!", "WARNING!!", MB_OK|ICON_STOP)
ctypes.windll.user32.MessageBoxW(0, "Your Computer has been infected by a virus", "Warning!", MB_OK| ICON_INFO)
ctypes.windll.user32.MessageBoxW(0, "To avoid deletion of files kindly answer these request", "DELETE?", MB_OK| ICON_EX)
ctypes.windll.user32.MessageBoxW(0, "Will...?", "Will...", MB_OK| ICON_QUESTION)
ctypes.windll.user32.MessageBoxW(0, "You be...", "Will you be ...", MB_OK| ICON_QUESTION)
ctypes.windll.user32.MessageBoxW(0, "My Valentine ^-^ <3 ?", "Waiting for reply", MB_OK| ICON_QUESTION)
ctypes.windll.user32.MessageBoxW(0, "Hehehe.... Thanks for Answering >-<", "Lots of Love!!", MB_OK| ICON_EX)
ctypes.windll.user32.MessageBoxW(0, "Congrats! Your PC has been fixed", "Congo...", MB_OK)
ctypes.windll.user32.MessageBoxW(0, "Have a nice Dayyyyy :)", "Byee!!", MB_OK| ICON_EX )




