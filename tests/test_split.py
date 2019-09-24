# -*- coding: utf-8 -*-
# @Time    : 2019-09-01 19:15
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : test_split.py
# @Explain :

from sheen import Str


class TestSplit(object):
    raw = 'xxooAß西xoox'
    obj = Str.red(raw)
    obj[2:-2] = Str.green
    obj[4:-4] = Str.blue
    obj[5:-5] = Str.magenta

    def test_split(self):
        assert self.obj.split('x') == self.raw.split('x')
        assert self.obj.split(Str.magenta('ß')) == self.raw.split('ß')
        assert self.obj.split(Str.red('o')) == [self.obj[:-2], self.obj[-1]]
        assert self.obj.split(Str.green('o')) == [self.obj[:2], '', self.obj[4:8], self.obj[9:]]
        assert self.obj.split(Str.green('o'), 1) == self.raw.split('o', 1)
        assert self.obj.split(Str.green('o'), 2) == self.raw.split('o', 2)
        assert self.obj.split(Str.green('o'), 3) == self.raw.split('o', 3)
        assert self.obj.split(Str.green('o'), 4) != self.raw.split('o', 4)

    def test_rsplit(self):
        assert self.obj.rsplit('x') == self.raw.rsplit('x')
        assert self.obj.rsplit(Str.magenta('ß')) == self.raw.rsplit('ß')
        assert self.obj.rsplit(Str.red('o')) == [self.obj[:-2], self.obj[-1]]
        assert self.obj.rsplit(Str.green('o')) == [self.obj[:2], '', self.obj[4:8], self.obj[9:]]
        assert self.obj.rsplit(Str.green('o'), 1) != self.raw.rsplit('o', 1)
        assert self.obj.rsplit(Str.green('o'), 2) != self.raw.rsplit('o', 2)
        assert self.obj.rsplit(Str.green('o'), 3) != self.raw.rsplit('o', 3)
        assert self.obj.rsplit(Str.green('o'), 4) != self.raw.rsplit('o', 4)
