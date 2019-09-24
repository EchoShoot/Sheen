# -*- coding: utf-8 -*-
# @Time    : 2019-09-01 19:46
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : test_expandtabs.py
# @Explain :

from sheen import Str


class TestExpandtabs(object):
    raw = 'xx\too\nAß西\txo\tox'
    obj = Str.red(raw)
    obj[2:-2] = Str.green
    obj[4:-4] = Str.blue
    obj[5:-5] = Str.magenta

    def test_expandtabs(self):
        assert self.obj.expandtabs() == self.raw.expandtabs()
        assert self.obj.expandtabs() == self.raw.expandtabs()
        assert self.obj.expandtabs(1) == self.raw.expandtabs(1)
        assert self.obj.expandtabs(16) == self.raw.expandtabs(16)
