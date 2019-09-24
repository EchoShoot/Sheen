# -*- coding: utf-8 -*-
# @Time    : 2019-09-01 17:49
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : test_others.py
# @Explain :

from sheen import Str
import pytest


class TestOthers(object):
    raw = 'xxooAß西xoox'
    obj = Str.red(raw)
    obj[2:-2] = Str.green
    obj[4:-4] = Str.blue
    obj[5:-5] = Str.magenta

    def test_upper(self):
        assert self.obj.upper() == self.raw.upper()
        assert self.obj.upper() != Str(self.raw).upper()

    def test_lower(self):
        assert self.obj.lower() == self.raw.lower()
        assert self.obj.lower() != Str(self.raw).lower()

    def test_swapcase(self):
        assert self.obj.swapcase() == self.raw.swapcase()
        assert self.obj.swapcase() != Str(self.raw).swapcase()

    def test_title(self):
        assert self.obj.title() == self.raw.title()
        assert self.obj.title() != Str(self.raw).title()

    def test_capitalize(self):
        assert self.obj.capitalize() == self.raw.capitalize()
        assert self.obj.capitalize() != Str(self.raw).capitalize()

    def test_casefold(self):
        assert self.obj.casefold() == self.raw.casefold()
        assert self.obj.casefold() != Str(self.raw).casefold()

    def test_startswith(self):
        assert self.obj.startswith('xxoo') is True
        assert self.obj.startswith('xoox') is False
        assert self.obj.startswith(Str.green('xx') + Str.red('oo')) is False
        assert self.obj.startswith(Str.red('xx') + Str.green('oo')) is True

    def test_endswith(self):
        assert self.obj.endswith('xxoo') is False
        assert self.obj.endswith('xoox') is True
        assert self.obj.endswith(Str.green('xo') + Str.red('ox')) is True
        assert self.obj.endswith(Str.red('xo') + Str.green('ox')) is False

    def test_zfill(self):
        assert self.obj.zfill(-1) == self.raw.zfill(-1)
        assert self.obj.zfill(0) == self.raw.zfill(0)
        assert self.obj.zfill(30) == self.raw.zfill(30)

    def test_encode(self):
        assert self.obj.encode() == self.raw.encode()
        assert self.obj.encode(encoding='gbk', errors='ignore') == self.raw.encode(encoding='gbk', errors='ignore')
        assert self.obj.encode(encoding='gbk', errors='replace') == self.raw.encode(encoding='gbk', errors='replace')
        with pytest.raises(UnicodeEncodeError):
            self.obj.encode(encoding='gbk', errors='strict')
        with pytest.raises(UnicodeEncodeError):
            self.raw.encode(encoding='gbk', errors='strict')
