# -*- coding: utf-8 -*-
# @Time    : 2019-09-01 20:24
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : test_is.py
# @Explain :

from sheen import Str
import platform

class TestOthers(object):
    raw = 'xxooAß西xoox'
    obj = Str.red(raw)
    obj[2:-2] = Str.green
    obj[4:-4] = Str.blue
    obj[5:-5] = Str.magenta

    def test_isalpha(self):
        assert self.obj.isalpha() == self.raw.isalpha()
        assert self.obj.isalpha() == Str(self.raw).isalpha()

    def test_isalnum(self):
        assert self.obj.isalnum() == self.raw.isalnum()
        assert self.obj.isalnum() == Str(self.raw).isalnum()

    def test_isascii(self):
        if platform.python_version() >= '3.7':
            assert self.obj.isascii() == self.raw.isascii()
            assert self.obj.isascii() == Str(self.raw).isascii()

    def test_isdecimal(self):
        assert self.obj.isdecimal() == self.raw.isdecimal()
        assert self.obj.isdecimal() == Str(self.raw).isdecimal()

    def test_isdigit(self):
        assert self.obj.isdigit() == self.raw.isdigit()
        assert self.obj.isdigit() == Str(self.raw).isdigit()

    def test_isidentifier(self):
        assert self.obj.isidentifier() == self.raw.isidentifier()
        assert self.obj.isidentifier() == Str(self.raw).isidentifier()

    def test_islower(self):
        assert self.obj.islower() == self.raw.islower()
        assert self.obj.islower() == Str(self.raw).islower()

    def test_isnumeric(self):
        assert self.obj.isnumeric() == self.raw.isnumeric()
        assert self.obj.isnumeric() == Str(self.raw).isnumeric()

    def test_isprintable(self):
        assert self.obj.isprintable() == Str(self.raw).isprintable()
        assert self.obj.isprintable() == Str(self.raw).isprintable()

    def test_isspace(self):
        assert self.obj.isspace() == Str(self.raw).isspace()
        assert self.obj.isspace() == Str(self.raw).isspace()

    def test_istitle(self):
        assert self.obj.istitle() == Str(self.raw).istitle()
        assert self.obj.istitle() == Str(self.raw).istitle()

    def test_isupper(self):
        assert self.obj.isupper() == Str(self.raw).isupper()
        assert self.obj.isupper() == Str(self.raw).isupper()
