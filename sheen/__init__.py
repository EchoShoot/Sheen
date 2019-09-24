# -*- coding: utf-8 -*-
# ____ _  _ ____ ____ _  _
# [__  |__| |___ |___ |\ |
# ___] |  | |___ |___ | \|
# > pip install sheen


from sheen.color import *
from sheen.colored import *
import platform

# 公开给外部的函数 (interface)
__all__ = (
    'Str',  # Color string
    'Color',  # Color translator
    'ColoredHandler',  # Design colored logger for yourself to integrate more imagination
)

# Let windows 10 support ANSI Escape Code
if platform.system() == 'Windows':
    import ctypes

    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
