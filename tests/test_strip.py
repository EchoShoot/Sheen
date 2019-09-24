# -*- coding: utf-8 -*-
# @Time    : 2019-09-01 16:57
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : test_strip.py
# @Explain :

from sheen import Str


class TestStrip(object):
    raw = 'xxooAß西xoox'
    obj = Str.red(raw)
    obj[2:-2] = Str.green
    obj[4:-4] = Str.blue
    obj[5:-5] = Str.magenta

    def test_lstrip(self):
        assert self.obj.lstrip(Str.green('o') + Str.red('x')) == self.raw.lstrip('o' + 'x')
        assert self.obj.lstrip(Str.green('o') + Str.red('x')) == self.obj[4:]

    def test_rstrip(self):
        assert self.obj.rstrip(Str.green('o') + Str.red('x')) == self.raw.rstrip('x')
        assert self.obj.rstrip(Str.green('o') + Str.red('x')) == self.obj[:-1]

    def test_strip(self):
        assert self.obj.strip(Str.green('o') + Str.red('x')) != self.raw.strip('o' + 'x')
        assert self.obj.strip(Str.green('o') + Str.red('x')) == self.obj[4:-1]
