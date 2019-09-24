# -*- coding: utf-8 -*-
# @Time    : 2019-08-29 18:55
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : color.py
# @Explain : About the function that sheen can provide

from collections.abc import Sequence
from itertools import chain, groupby
import sys as _sys

# 公开给外部的函数 (interface)
__all__ = (
    'Str',  # Color string
    'Color',  # Color translator
)


# \-改进原则 ( Development principle ):
#   |- 坚持简单易上手, 符合大众使用习惯. (easy to use, easy to learn)
#   |- 紧跟内建的风格, 若无必要就不新增. (  Don't to gild the lily  )

class Color(object):
    __isabstractmethod__ = False

    def __init__(self, code):
        self.code = ord(code) if isinstance(code, str) else code
        self.fore = self.code & int('0b11111111', 2)
        self.back = self.code >> 8 & int('0b11111111', 2)
        self.style = self.code >> 16 & int('0b00001111', 2)

    @classmethod
    def palette(cls):
        text = ""
        flat = 1
        for i in range(16, 232):
            if (i - 16) % 18 == 0:
                text += '\n'
                flat ^= 1
            colorstyle = Color.RGB(i) | (Color.rgb(16) if flat else Color.rgb(231))
            text += "{:^5}".format(colorstyle(i))
        else:
            print(text)

    @classmethod
    def rgb(cls, rgb):
        """ r,g,b scope is 0 ~ 5 """
        if isinstance(rgb, (tuple, list)):
            r, g, b, *_ = [int(i) // 43 for i in rgb]
            fore = (36 * r + 6 * g + b + 16) & int('0b11111111', 2)
            return cls(fore)
        elif isinstance(rgb, int):
            fore = rgb & int('0b11111111', 2)
            return cls(fore)

    @classmethod
    def RGB(cls, RGB):
        """ R,G,B scope is 0 ~ 5 """
        if isinstance(RGB, (tuple, list)):
            R, G, B, *_ = [int(i) // 43 for i in RGB]
            back = (36 * R + 6 * G + B + 16) & int('0b11111111', 2)
            return cls(back << 8)
        elif isinstance(RGB, int):
            back = RGB & int('0b11111111', 2)
            return cls(back << 8)

    def __int__(self):
        return int(self.code)

    def __eq__(self, other):
        return self.code == other.code

    def __or__(self, other):
        fore = other.fore or self.fore
        back = other.back or self.back
        style = self.style | other.style if other.style else self.style
        return self.__class__(chr(style << 16 | back << 8 | fore))

    def render(self):
        # FORE
        if 16 <= self.fore <= 231:  # 按照 216 色翻译
            fore = (38, 5, self.fore)
        elif 240 <= self.fore <= 255:  # 按照 16 色翻译方式
            fore = ((self.fore & int('0b0111', 2)) + 30 + 60 * (self.fore >> 3 & 1),)
        else:  # 其他的不翻译
            fore = ()
        # BACK
        if 16 <= self.back <= 231:  # 按照 216 色翻译
            back = (48, 5, self.back)
        elif 240 <= self.back <= 255:  # 按照 16 色翻译方式
            back = ((self.back & int('0b0111', 2)) + 40 + 60 * (self.back >> 3 & 1),)
        else:  # 其他的不翻译
            back = ()
        # STYLE
        style = [n for _, n in enumerate([1, 3, 4, 5]) if self.style & 1 << _]
        color = ';'.join(map(str, chain(fore, back, style)))
        # prefix & suffix
        if color:
            return "\033[{}m".format(color), "\033[0m"
        else:
            return "", ""

    def __repr__(self):
        clsname = self.__class__.__name__
        prefix, suffix = self.render()
        return "{}{}({}){}".format(prefix, clsname, self.code, suffix)

    def __call__(self, string) -> str:
        if isinstance(string, Str):
            string = string.data
        return Str(string, chr(self.code))

    def __set__(self, instance, value):
        return instance

    def __get__(self, instance, instance_cls):
        if self.__doc__ is None:
            prefix, suffix = self.render()
            self.__doc__ = """```
                                >>> {}('Its color is like this')
                                >>> {}Its color is like this{}
                            ```""".format(instance_cls.__name__, prefix, suffix)
        return instance or self

    def __getattr__(self, item):
        color = getattr(Str, item, None)
        if isinstance(color, self.__class__):
            return self | color
        else:
            raise AttributeError("the object 'Str.{}' is invalid '{}' type".format(item, self.__class__.__name__))


class Str(Sequence):
    black = Color(int('0b0000''00000000''11110000', 2))  # type:Str
    red = Color(int('0b0000''00000000''11110001', 2))  # type:Str
    green = Color(int('0b0000''00000000''11110010', 2))  # type:Str
    yellow = Color(int('0b0000''00000000''11110011', 2))  # type:Str
    blue = Color(int('0b0000''00000000''11110100', 2))  # type:Str
    magenta = Color(int('0b0000''00000000''11110101', 2))  # type:Str
    cyan = Color(int('0b0000''00000000''11110110', 2))  # type:Str
    white = Color(int('0b0000''00000000''11110111', 2))  # type:Str
    lightblack = Color(int('0b0000''00000000''11111000', 2))  # type:Str
    lightred = Color(int('0b0000''00000000''11111001', 2))  # type:Str
    lightgreen = Color(int('0b0000''00000000''11111010', 2))  # type:Str
    lightyellow = Color(int('0b0000''00000000''11111011', 2))  # type:Str
    lightblue = Color(int('0b0000''00000000''11111100', 2))  # type:Str
    lightmagenta = Color(int('0b0000''00000000''11111101', 2))  # type:Str
    lightcyan = Color(int('0b0000''00000000''11111110', 2))  # type:Str
    lightwhite = Color(int('0b0000''00000000''11111111', 2))  # type:Str
    BLACK = Color(int('0b0000''11110000''00000000', 2))  # type:Str
    RED = Color(int('0b0000''11110001''00000000', 2))  # type:Str
    GREEN = Color(int('0b0000''11110010''00000000', 2))  # type:Str
    YELLOW = Color(int('0b0000''11110011''00000000', 2))  # type:Str
    BLUE = Color(int('0b0000''11110100''00000000', 2))  # type:Str
    MAGENTA = Color(int('0b0000''11110101''00000000', 2))  # type:Str
    CYAN = Color(int('0b0000''11110110''00000000', 2))  # type:Str
    WHITE = Color(int('0b0000''11110111''00000000', 2))  # type:Str
    LIGHTBLACK = Color(int('0b0000''11111000''00000000', 2))  # type:Str
    LIGHTRED = Color(int('0b0000''11111001''00000000', 2))  # type:Str
    LIGHTGREEN = Color(int('0b0000''11111010''00000000', 2))  # type:Str
    LIGHTYELLOW = Color(int('0b0000''11111011''00000000', 2))  # type:Str
    LIGHTBLUE = Color(int('0b0000''11111100''00000000', 2))  # type:Str
    LIGHTMAGENTA = Color(int('0b0000''11111101''00000000', 2))  # type:Str
    LIGHTCYAN = Color(int('0b0000''11111110''00000000', 2))  # type:Str
    LIGHTWHITE = Color(int('0b0000''11111111''00000000', 2))  # type:Str
    Bold = Color(int('0b0001''00000000''00000000', 2))  # type:Str
    Italic = Color(int('0b0010''00000000''00000000', 2))  # type:Str
    Underline = Color(int('0b0100''00000000''00000000', 2))  # type:Str
    Twinkle = Color(int('0b1000''00000000''00000000', 2))  # type:Str

    def __init__(self, string, colors=chr(0)):
        if isinstance(string, self.__class__):
            self.data = string.data
            self.colors = string.colors
        else:
            self.data = str(string)
            self.colors = colors if len(colors) == len(self.data) else colors * len(self.data)

    def __setitem__(self, key, color):
        if isinstance(color, Color):
            colors = list(self.colors)
            colors[key] = [chr(int(Color(ord(c)) | color)) for c in colors[key]]
            self.colors = ''.join(colors)
        else:
            raise TypeError("'{}' object only support item assignment 'Color' object, rather then '{}'".format(
                self.__class__.__name__, color.__class__.__name__))

    def __call__(self, *args, **kwargs) -> str:
        raise TypeError("'{}' object is not callable".format(self.__class__.__name__))

    def __str__(self):
        string = []
        _from = 0
        for color_number, group in groupby(self.colors):
            _to = _from + len(tuple(group))
            prefix, suffix = Color(color_number).render()
            string.append(prefix + self.data[_from:_to] + suffix)
            _from = _to
        else:
            return ''.join(string)

    def __repr__(self):
        string = []
        _from = 0
        for color_number, group in groupby(self.colors):
            _to = _from + len(tuple(group))
            data = self.data[_from:_to].__repr__()[1:-1]  # can't use strip, due to "'''''just like this situation'"
            if data:
                prefix, suffix = Color(color_number).render()
                string.append(prefix + data + suffix)
            _from = _to
        else:
            return "'" + ''.join(string) + "'"

    def __format__(self, format_spec):
        string = []
        _from = 0
        for color_number, group in groupby(self.colors):
            _to = _from + len(tuple(group))
            data = self.data[_from:_to].__format__(format_spec)
            if data:
                prefix, suffix = Color(color_number).render()
                string.append(prefix + data + suffix)
            _from = _to
        else:
            return ''.join(string)

    def __int__(self):
        return int(self.data)

    def __float__(self):
        return float(self.data)

    def __complex__(self):
        return complex(self.data)

    def __hash__(self):
        return hash(self.data)

    def __getnewargs__(self):
        return (self.data[:],)

    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.data == value.data and self.colors == value.colors
        return self.data == value

    def __lt__(self, value):
        if isinstance(value, self.__class__):
            return self.data < value.data
        return self.data < value

    def __le__(self, value):
        if isinstance(value, self.__class__):
            return self.data <= value.data
        return self.data <= value

    def __gt__(self, value):
        if isinstance(value, self.__class__):
            return self.data > value.data
        return self.data > value

    def __ge__(self, value):
        if isinstance(value, self.__class__):
            return self.data >= value.data
        return self.data >= value

    def __contains__(self, key):
        if isinstance(key, self.__class__):
            _self = "".join(chain(*zip(self.data, self.colors)))
            _other = "".join(chain(*zip(key.data, key.colors)))
            return _other in _self
        else:
            return key in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.__class__(self.data[key], self.colors[key])

    def __add__(self, value):
        if isinstance(value, self.__class__):
            return self.__class__(self.data + value.data, self.colors + value.colors)
        else:
            return self + self.__class__(value)

    def __radd__(self, value):
        if isinstance(value, self.__class__):
            return self.__class__(value.data + self.data, value.colors + self.colors)
        else:
            return self.__class__(value) + self

    def __mul__(self, n):
        return self.__class__(self.data * n, self.colors * n)

    __rmul__ = __mul__

    def __mod__(self, args):  # TODO: 未返回 Str (should return 'Str' type)
        try:
            return self.__class__(str(self) % args)
        except ValueError as e:
            raise ValueError("The color may not fully cover the placeholder") from e

    def __rmod__(self, format):  # TODO: 未返回 Str (should return 'Str' type)
        try:
            return self.__class__(format % args)
        except ValueError as e:
            raise ValueError("The color may not fully cover the placeholder") from e

    def capitalize(self):
        return self.__class__(self.data.capitalize(), self.colors)

    def casefold(self):
        data = []
        colors = []
        _from = 0
        for color_number, group in groupby(self.colors):
            _to = _from + len(tuple(group))
            string = self.data[_from: _to].casefold()
            data.append(string)
            colors.append(self.colors * len(string))
            _from = _to
        else:
            return self.__class__(''.join(data), ''.join(colors))

    def center(self, width, fillchar=' '):
        if isinstance(fillchar, self.__class__):
            string = self.data.center(width, fillchar.data)
            colors = self.colors.center(width, fillchar.colors)
        else:
            string = self.data.center(width, fillchar)
            colors = self.colors.center(width, chr(0))
        return self.__class__(string, colors)

    def count(self, sub, start=0, end=_sys.maxsize) -> int:
        if isinstance(sub, self.__class__):
            _self = "".join(chain(*zip(self.data, self.colors)))
            _other = "".join(chain(*zip(sub.data, sub.colors)))
            return _self.count(_other, start * 2, min(end * 2, _sys.maxsize))
        else:
            return self.data.count(sub, start, end)

    def encode(self, encoding='utf-8', errors='strict'):
        return self.data.encode(encoding, errors)  # 返回值是 bytes 不是 Str

    def endswith(self, suffix, start=0, end=_sys.maxsize) -> bool:
        if isinstance(suffix, self.__class__):
            return self.data.endswith(suffix.data, start, end) and self.colors.endswith(suffix.colors, start, end)
        else:
            return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        string = []
        colors = []
        pos = 0
        for char, color in zip(self.data, self.colors):
            if char == "\t":
                char = " " * (tabsize - pos % tabsize)
                color = color * (tabsize - pos % tabsize)
            if char == "\n":
                pos = 0
            else:
                pos += len(char)
            string.append(char)
            colors.append(color)
        return self.__class__(''.join(string), ''.join(colors))

    def find(self, sub, start=0, end=_sys.maxsize) -> int:
        if isinstance(sub, self.__class__):
            _self = "".join(chain(*zip(self.data, self.colors)))
            _other = "".join(chain(*zip(sub.data, sub.colors)))
            return _self.find(_other, start, end) // 2
        else:
            return self.data.find(sub, start, end)

    def format(self, *args, **kwds) -> str:  # TODO: 未返回 Str (should return 'Str' type)
        try:
            return str(self).format(*args, **kwds)
        except ValueError as e:
            raise ValueError("The color may not fully cover the placeholder") from e

    def format_map(self, mapping) -> str:  # TODO: 未返回 Str (should return 'Str' type)
        try:
            return str(self).format_map(mapping)
        except ValueError as e:
            raise ValueError("The color may not fully cover the placeholder") from e

    def index(self, sub, start=0, end=_sys.maxsize):
        if isinstance(sub, self.__class__):
            _self = "".join(chain(*zip(self.data, self.colors)))
            _other = "".join(chain(*zip(sub.data, sub.colors)))
            return _self.index(_other, start, end) // 2
        else:
            return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isascii(self):
        return self.data.isascii()  # support version 3.7

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def isidentifier(self):
        return self.data.isidentifier()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isprintable(self):
        return self.data.isprintable()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, iterable):
        datas = []
        colors = []
        for index, _ in enumerate(iterable):
            if isinstance(_, self.__class__):
                datas.append(_.data)
                colors.append(_.colors)
            elif isinstance(_, str):
                s = self.__class__(_)
                datas.append(s.data)
                colors.append(s.colors)
            else:
                raise TypeError("sequence item {}: expected str instance, int found".format(index))
        else:
            return self.__class__(self.data.join(datas), self.colors.join(colors))

    def ljust(self, width, fillchar=' '):
        if isinstance(fillchar, self.__class__):
            string = self.data.ljust(width, fillchar.data)
            colors = self.colors.ljust(width, fillchar.colors)
        else:
            string = self.data.ljust(width, fillchar)
            colors = self.colors.ljust(width, chr(0))
        return self.__class__(string, colors)

    def lower(self):
        return self.__class__(self.data.lower(), self.colors)

    maketrans = str.maketrans  # TODO: 与 translate 结合完成颜色翻译 (should be support translate char with maketrans)

    def lstrip(self, chars=None):
        if isinstance(chars, self.__class__):
            _start = 0
            _end = len(self)
            for v in self:
                if v not in chars:
                    break
                else:
                    _start += 1
            return self[_start: _end]
        else:
            string = self.data.lstrip(chars)
            colors = self.colors[-len(string):]
            return self.__class__(string, colors)

    def partition(self, sep):
        result = []
        if isinstance(sep, self.__class__):
            _self = "".join(chain(*zip(self.data, self.colors)))
            _other = "".join(chain(*zip(sep.data, sep.colors)))
            for sub in _self.partition(_other):
                result.append(self.__class__(sub[::2], sub[1::2]))
            else:
                return tuple(result)
        else:
            _from = 0
            for sub in self.data.partition(sep):
                _to = _from + len(sub)
                result.append(self.__class__(sub, self.colors[_from:_to]))
                _from = _to
            else:
                return tuple(result)

    def replace(self, old, new, count=-1):
        if not isinstance(new, self.__class__):
            new = self.__class__(new)
        return new.join(self.split(old, count))

    def rfind(self, sub, start=0, end=_sys.maxsize) -> int:
        if isinstance(sub, self.__class__):
            _self = "".join(chain(*zip(self.data, self.colors)))
            _other = "".join(chain(*zip(sub.data, sub.colors)))
            return _self.rfind(_other, start, end) // 2
        else:
            return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=_sys.maxsize) -> int:
        if isinstance(sub, self.__class__):
            _self = "".join(chain(*zip(self.data, self.colors)))
            _other = "".join(chain(*zip(sub.data, sub.colors)))
            return _self.rindex(_other, start, end) // 2
        else:
            return self.data.rindex(sub, start, end)

    def rjust(self, width, fillchar=" "):
        if isinstance(fillchar, self.__class__):
            string = self.data.rjust(width, fillchar.data)
            colors = self.colors.rjust(width, fillchar.colors)
        else:
            string = self.data.rjust(width, fillchar)
            colors = self.colors.rjust(width, chr(0))
        return self.__class__(string, colors)

    def rpartition(self, sep):
        result = []
        if isinstance(sep, self.__class__):
            _self = "".join(chain(*zip(self.data, self.colors)))
            _other = "".join(chain(*zip(sep.data, sep.colors)))
            for sub in _self.rpartition(_other):
                result.append(self.__class__(sub[::2], sub[1::2]))
            else:
                return tuple(result)
        else:
            _from = 0
            for sub in self.data.rpartition(sep):
                _to = _from + len(sub)
                result.append(self.__class__(sub, self.colors[_from:_to]))
                _from = _to
            else:
                return tuple(result)

    def rstrip(self, chars=None):
        if isinstance(chars, self.__class__):
            _start = 0
            _end = len(self)
            for v in reversed(self):
                if v not in chars:
                    break
                else:
                    _end -= 1
            return self[_start: _end]
        else:
            string = self.data.rstrip(chars)
            colors = self.colors[:len(string)]
            return self.__class__(string, colors)

    def split(self, sep=None, maxsplit=-1):
        result = []
        if isinstance(sep, self.__class__):
            _self = "".join(chain(*zip(self.data, self.colors)))
            _other = "".join(chain(*zip(sep.data, sep.colors)))
            for sub in _self.split(_other, maxsplit):
                result.append(self.__class__(sub[::2], sub[1::2]))
            else:
                return result
        else:
            _from = 0
            for sub in self.data.split(sep, maxsplit):
                _to = _from + len(sub)
                result.append(self.__class__(sub, self.colors[_from:_to]))
                _from = _to + len(sep)
            else:
                return result

    def rsplit(self, sep=None, maxsplit=-1):
        result = []
        if isinstance(sep, self.__class__):
            _self = "".join(chain(*zip(self.data, self.colors)))
            _other = "".join(chain(*zip(sep.data, sep.colors)))
            for sub in _self.rsplit(_other, maxsplit):
                result.append(self.__class__(sub[::2], sub[1::2]))
            else:
                return result
        else:
            _from = 0
            for sub in self.data.rsplit(sep, maxsplit):
                _to = _from + len(sub)
                result.append(self.__class__(sub, self.colors[_from:_to]))
                _from = _to + len(sep)
            else:
                return result

    def splitlines(self, keepends=False):
        result = []
        _from = 0
        for each in self.data.splitlines(True):
            _to = _from + len(each)
            if keepends is True:
                colors = self.colors[_from:_to]
            else:
                each = each.rstrip('\r\n')
                colors = self.colors[_from:_from + len(each)]
            result.append(self.__class__(each, colors))
            _from = _to
        return result

    def startswith(self, prefix, start=0, end=_sys.maxsize) -> bool:
        if isinstance(prefix, self.__class__):
            return self.data.startswith(prefix.data, start, end) and self.colors.startswith(prefix.colors, start, end)
        else:
            return self.data.startswith(prefix, start, end)

    def strip(self, chars=' \n\t'):
        return self.lstrip(chars).rstrip(chars)

    def swapcase(self):
        return self.__class__(self.data.swapcase(), self.colors)

    def title(self):
        return self.__class__(self.data.title(), self.colors)

    def translate(self, table):  # TODO:还不支持带颜色翻译 (should be support translate char with maketrans)
        return self.__class__(self.data.translate(table), self.colors)

    def upper(self):
        return self.__class__(self.data.upper(), self.colors)

    def zfill(self, width):
        return self.__class__(self.data.zfill(width), self.colors.zfill(width).replace('0', self.colors[0]))


if __name__ == '__main__':
    from time import perf_counter

    startime = perf_counter()
    obj = Str.red.Underline('nice to meet you!')
    obj[3:-3] = Str.BLUE.Twinkle
    for i in range(10000):
        print(obj)
    print(perf_counter() - startime)
