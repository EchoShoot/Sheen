# -*- coding: utf-8 -*-
# @Time    : 2019-09-01 18:33
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : test_replace.py
# @Explain :

from sheen import Str


class TestReplace(object):
    raw = 'xxooAß西xoox'
    obj = Str.red(raw)
    obj[2:-2] = Str.green
    obj[4:-4] = Str.blue
    obj[5:-5] = Str.magenta

    def test_replace(self):
        assert self.obj.replace('o', 'XX') == self.raw.replace('o', 'XX')
        assert self.obj.replace(Str.blue('A'), 'XX') == self.raw.replace('A', 'XX')
        assert self.obj.replace(Str.red('o'), 'XX') != self.raw.replace('o', 'XX')
        assert self.obj.replace('o', Str.red('x')) == self.obj.replace('o', Str.red('x'))
        assert self.obj.replace('o', Str.red('x')) != self.obj.replace('o', Str.blue('x'))
        assert self.obj.replace(Str.red('x'), 'o') != self.obj.replace(Str.red('x'), Str.blue('o'))
        assert self.obj.replace(Str.red('x'), 'o') == self.obj.replace(Str.red('x'), Str('o'))
        assert self.obj.replace(Str.green('o'), 'x') != self.obj.replace('o', 'x', 2)
        assert self.obj.replace(Str.green('o'), 'x') == self.obj.replace('o', 'x', 3)
