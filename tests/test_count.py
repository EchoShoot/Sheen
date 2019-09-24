# -*- coding: utf-8 -*-
# @Time    : 2019-09-01 18:50
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : test_count.py
# @Explain :

from sheen import Str


class TestCount(object):
    raw = 'xxooAß西xoox'
    obj = Str.red(raw)
    obj[2:-2] = Str.green
    obj[4:-4] = Str.blue
    obj[5:-5] = Str.magenta

    def test_count(self):
        assert self.obj.count(Str.green('o'), 2, 4) == self.raw.count('o', 2, 4)
        assert self.obj.count('x') == self.raw.count('x')
        assert self.obj.count(Str.red('x')) == 3
        assert self.obj.count(Str.red('x')) < self.raw.count('x')
        assert self.obj.count(Str.green('oo')) == 1
        assert self.obj.count(Str.red('o') + Str.green('o')) == 0
        assert self.obj.count(Str.green('o') + Str.red('o')) == 1
