import ctypes
import os

pathToBmp = os.path.normpath("C:\img.jpg")
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, pathToBmp, 0)
