# -*- coding: utf-8 -*-
# @Time    : 2019-09-05 22:57
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : About the sheen
from sheen import Str, Color

text = Str(r"""
                                   
     ____ _  _ ____ ____ _  _      
     [__  |__| |___ |___ |\ |      
     ___] |  | |___ |___ | \|      
                                   
Sheen Has been installed successful 
""")

for i in range(len(text)):
    if text[i] != '\n':
        text[i:i+1] = Color.RGB(i+16) if text[i] == ' ' else Color.rgb(231) | Color.RGB(i+16)

text += Str("""
>>> from sheen import Str, Color
>>> Str.blue('render font color with lowercase')
""")
text += repr(Str.blue('render font color with lowercase'))
text += Str('''\n>>> Str.BLUE('render background color with uppercase')\n''')
text += repr(Str.BLUE('render background color with uppercase'))
text += Str('''\n>>> Str.Underline('render style with capital')\n''')
text += repr(Str.Underline('render style with capital'))
text += Str('''\n>>> Str.lightblue.BLUE('joint rendering with dot')\n''')
text += repr(Str.lightblue.BLUE('joint rendering with dot'))
text += Str('''\n>>> Str.BLUE.lightblue("yes! it's free, no order restrain")\n''')
text += repr(Str.BLUE.lightblue("yes! it's free, no order restrain"))
text += Str('''\n>>> Str.cyan.LIGHTCYAN.Underline('esay to lean, ease to use')\n''')
text += repr(Str.cyan.LIGHTCYAN.Underline('esay to lean, ease to use'))
text += Str('''\n>>> Str.lightcyan("You can use it like builtin 'str'").split(' ')\n''')
text += Str.lightcyan("You can use it like builtin 'str'").split(' ')
text += Str('''
>>> text = Str.lightcyan.Twinkle("Let us integrate more imagination")
>>> text.replace('Let us', Str.lightblue('pip install sheen, to'))
''')
text += repr(Str.lightcyan.Twinkle("Let us integrate more imagination").replace('Let us', Str.lightblue('pip install sheen, to')))
text += Str('''\n>>> text = Str.black.LIGHTWHITE('@!$#!&*&simplify for human! i am sheen!#@$#%^&')''')
text += Str('''\n>>> text.title().strip('!@#$%^&*')\n''')
text += repr(Str.black.LIGHTWHITE('@!$#!&*&simplify for human! i am sheen!#@$#%^&').title().strip('!@#$%^&*'))
text += Str('''\n>>>''')
text += Str('''\n>>> Color.palette()''')
print(text)
Color.palette()