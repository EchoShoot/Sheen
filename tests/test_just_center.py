# -*- coding: utf-8 -*-
# @Time    : 2019-09-01 17:37
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : test_just_center.py
# @Explain :

from sheen import Str


class TestJustCenter(object):
    raw = 'xxooAß西xoox'
    obj = Str.red(raw)
    obj[2:-2] = Str.green
    obj[4:-4] = Str.blue
    obj[5:-5] = Str.magenta

    def test_ljust(self):
        assert self.obj.ljust(10) == self.obj
        assert self.obj.ljust(30, '*') == self.raw.ljust(30, '*')
        assert self.obj.ljust(30, Str.blue('*')) == self.raw.ljust(30, '*')
        assert self.obj.ljust(30, Str.blue('*')) != self.obj.ljust(30, Str.red('*'))

    def test_rjust(self):
        assert self.obj.rjust(10) == self.obj
        assert self.obj.rjust(30, '*') == self.raw.rjust(30, '*')
        assert self.obj.rjust(30, Str.blue('*')) == self.raw.rjust(30, '*')
        assert self.obj.rjust(30, Str.blue('*')) != self.obj.rjust(30, Str.red('*'))

    def test_center(self):
        assert self.obj.center(10) == self.obj
        assert self.obj.center(30, '*') == self.raw.center(30, "*")
        assert self.obj.center(30, Str.blue('*')) == self.raw.center(30, "*")
        assert self.obj.center(30, Str.blue('*')) != self.obj.center(30, Str.red('*'))
