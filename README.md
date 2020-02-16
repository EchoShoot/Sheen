Sheen:
==========================

**Pythonic** cross-platform colored terminal text **[support 16/256 colors]**
> Let color be your _new dimension_ to integrate _more imagination_.

<div align=center><img src="https://raw.githubusercontent.com/EchoShoot/Sheen/master/docs/Intro.gif"></div>

Quick Learn
---
> Come to try the code below, in your IDLE

```{.sourceCode .python}
>>> from sheen import Str
>>>
>>> Str.red('render font color with lowercase')
>>> Str.RED('render background color with uppercase')
>>> Str.Underline('render style with capital')
>>> 
>>> Str.red.BLUE('joint rendering with dot')
>>> Str.BLUE.red("yes! it's free, no order restrain")
>>> Str.cyan.LIGHTBLUE.Underline('esay to lean, ease to use')
>>>
>>> Str.red("You can use it like builtin 'str'").split(' ')
>>> text = Str.lightcyan.Twinkle("Let us integrate more imagination")
>>> text.replace('Let us', Str.lightred('pip install sheen, to'))
>>> Str.LIGHTWHITE('@!$#!&*&simplify for human! i am sheen!#@$#%^&').title().strip('!@#$%^&*')
```
<p align="right">Simple is better than complex. flat is better than nested. Readability counts. </br>-- excerpt from the zen of python</p>

**Str Type Supported:**
<table style="text-align: center; align: center;">
<thead><tr><td colspan=5 bgcolor="#c0c0c0"><b>Str Type Supported Attribute Chain</b></td></tr></thead>
<tr>
	<td rowspan=4 bgcolor=#f0f0f0>Font Color</td><td>black</td><td>red</td><td>green</td><td>yellow</td>
</tr>
<tr>
	<td>lightblack</td><td>lightred</td><td>lightgreen</td><td>lightyellow</td>
</tr>
<tr>
	<td>blue</td><td>magenta</td><td>cyan</td><td>white</td>
</tr>
<tr>
    <td>lightblue</td><td>lightmagenta</td><td>lightcyan</td><td>lightwhite</td>
</tr>
<tr>
	<td rowspan=4 bgcolor=#f0f0f0>Background Color</td><td>BLACK</td><td>RED</td><td>GREEN</td><td>YELLOW</td>
</tr>
<tr>
	<td>BLUE</td><td>MAGENTA</td><td>CYAN</td><td>WHITE</td>
</tr>
<tr>
	<td>LIGHTBLACK</td><td>LIGHTRED</td><td>LIGHTGREEN</td><td>LIGHTYELLOW</td>
</tr>
<tr>
	<td>LIGHTBLUE</td><td>LIGHTMAGENTA</td><td>LIGHTCYAN</td><td>LIGHTWHITE</td>
</tr>
<tr>
<td bgcolor=#f0f0f0>Style Type</td><td>Bold</td><td>Italic</td><td>Underline</td><td>Twinkle</td>
</tr>
</table>


Installation
---
> To install sheen, simply use pip:

```{.sourceCode .bash}
$ pip install sheen
$ python -m sheen
```

**If it's successfully installed, it will be as shown below.**

<div align=center><img src="https://raw.githubusercontent.com/EchoShoot/Sheen/master/docs/Tutor.gif"></div>

<p align="right">It's a simple way to get tutorial, you don't need to come here every time
<br>when you forget the usage of sheen</p>

Learn More
---
###  How to display with 256 colors
> Your can choose the color that your like with 'Color' type

```{.sourceCode .python}
>>> from sheen import Str, Color
>>> Color.palette()  # Reference color code
>>>
>>> Color.rgb(222)('render font color with rgb')
>>> Color.RGB(123)('render background color with RGB')
>>> 
>>> Color.rgb([255,200,190])('render font color with rgb')
>>> Color.RGB([150,120,250])('render background color with RGB')
>>>
>>> DIYcolor = Color.rgb(222) | Color.RGB(123) | Str.Underline
>>> DIYcolor("It's my color style")
>>>
>>> text = Str.Underline('Use slice to modification color')
>>> text[:] = Color.rgb(222)
>>> text[-3:-5] = Color.RGB(123)
>>> text
``` 

<div align=center><img src="https://raw.githubusercontent.com/EchoShoot/Sheen/master/docs/Paletee.png"></div>

<p align="right"> It's said that 256 colors can be valid in the terminal<br>but maybe invalid in the IDE</p>

### How to config Multicolored logging
> Sheen has been build-in scheme, which can prints different colored logs based on log level:

<div align=center><img src="https://raw.githubusercontent.com/EchoShoot/Sheen/master/docs/ColoredHandler.png"></div>

<p align="right"> As you can see, sheen <b>only takes 5 lines</b> to complete
<br> the configuration of the Multicolored logging</p>

> You can design 'Formatter', to get color scheme which belong to yourself

```python
import logging
from sheen import Str, ColoredHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


handle = ColoredHandler()
handle.setFormatter({
    logging.DEBUG: logging.Formatter(fmt=str(Str.blue('%(asctime)s - %(levelname)s | %(message)s')), datefmt='%Y-%m-%d'),
    logging.INFO: Str.magenta('%(asctime)s - %(levelname)s | %(message)s'),
})
logger.addHandler(handle)

logger.debug('debug')
logger.info('info')
logger.warning('warning')
logger.error('error')
logger.critical('critical')
```
<p align="right"> Take it easy, it will be use after rendered as 'str' type 
<br> <b>without affecting the logging output speed</b> <p>

### How to get the best performance
> Sheen was born for convenience, when you want the fastest, there is a way.

```{.sourceCode .python}
>>> from sheen import Str, Color
>>> str(Str.cyan.BLUE('... content ...'))
'\x1b[36;44m... content ...\x1b[0m'
>>>
``` 

<div align=center><img src="https://raw.githubusercontent.com/EchoShoot/Sheen/master/docs/BestPerformance.png"></div>

<p align='right'> Don't forget to 'import sheen', It's necessary on windows.
<br> -- Windows 10 is default closed <i>ANSI Escape Code<i> </p>

FAQ
---
- :speech_balloon: Why not support python2.7
    > Python 2.7 will retire in 2020 https://pythonclock.org/, 
    > Many libraries already or will to give up compatibility 2.7, 
    > such as NumPy, Pandas, Ipython, Matplotlib ... 
- :speech_balloon:  Why not support version below Windows 10
    > Windows support _ANSI Escape Code_ start with win10, 
    > this gives the possibility to use ANSI to display colors for sheen.
    > the version below Windows 10 will retire in future, just like python2.7
- :speech_balloon:  How to get the best running performance
    > Render to _ANSI Escape Code_, and then copy it into your code, no faster than this.
    > but in most cases you needn't to do this