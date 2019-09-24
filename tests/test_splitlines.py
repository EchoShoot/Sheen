# -*- coding: utf-8 -*-
# @Time    : 2019-09-01 19:46
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : test_splitlines.py
# @Explain :

from sheen import Str


class TestSplitlines(object):
    raw = 'xx\noo\tAß西\rxo\r\nox'
    obj = Str.red(raw)
    obj[2:-2] = Str.green
    obj[4:-4] = Str.blue
    obj[5:-5] = Str.magenta

    def test_splitlines(self):
        assert self.obj.splitlines() == self.raw.splitlines()
        assert self.obj.splitlines(True) == self.raw.splitlines(True)
        assert self.obj.splitlines(False) == self.raw.splitlines(False)
