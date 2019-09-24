# -*- coding: utf-8 -*-
# @Time    : 2019-09-01 17:14
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : test_partition.py
# @Explain :

from sheen import Str


class TestPartition(object):
    raw = 'xxooAß西xoox'
    obj = Str.red(raw)
    obj[2:-2] = Str.green
    obj[4:-4] = Str.blue
    obj[5:-5] = Str.magenta

    def test_partition(self):
        assert self.obj.partition('x') == self.raw.partition('x')
        assert self.obj.partition(Str.red('x')) == ('', self.obj[:1], self.obj[1:])
        assert self.obj.partition(Str.red('x')) != self.obj.partition(Str.green('x'))
        assert self.obj.partition(Str.green('o')) == (self.obj[:2], self.obj[2:3], self.obj[3:])
        assert self.obj.partition(Str.blue('x')) == (self.obj[:], '', '')

    def test_rpartition(self):
        assert self.obj.rpartition('x') == self.raw.rpartition('x')
        assert self.obj.rpartition(Str.red('x')) == (self.obj[:-1], self.obj[-1], '')
        assert self.obj.rpartition(Str.red('x')) != self.obj.rpartition(Str.green('x'))
        assert self.obj.rpartition(Str.green('o')) == (self.obj[:8], self.obj[8:-2], self.obj[-2:])
        assert self.obj.rpartition(Str.blue('x')) == ('', '', self.obj[:])
