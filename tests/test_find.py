# -*- coding: utf-8 -*-
# @Time    : 2019-09-01 18:33
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : test_find.py
# @Explain :

from sheen import Str


class TestFind(object):
    raw = 'xxooAß西xoox'
    obj = Str.red(raw)
    obj[2:-2] = Str.green
    obj[4:-4] = Str.blue
    obj[5:-5] = Str.magenta

    def test_find(self):
        assert self.obj.find('echoshoot') == -1
        assert self.obj.find(Str.green('xo')) == 7
        assert self.obj.find(Str.red('x') + Str.green('o')) == 1
        assert self.obj.find('xo') == 1

    def test_rfind(self):
        assert self.obj.rfind('echoshoot') == -1
        assert self.obj.rfind(Str.green('xo')) == 7
        assert self.obj.rfind(Str.red('x') + Str.green('o')) == 1
        assert self.obj.rfind('xo') == 7
