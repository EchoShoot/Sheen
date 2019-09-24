# -*- coding: utf-8 -*-
# @Time    : 2019-09-01 21:11
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : test_translate.py
# @Explain :
from sheen import Str


class TestOthers(object):
    table = str.maketrans('xA', 'oB')
    raw = 'xxooAß西xoox'
    obj = Str.red(raw)
    obj[2:-2] = Str.green
    obj[4:-4] = Str.blue
    obj[5:-5] = Str.magenta

    def test_translate(self):
        assert self.obj.translate(self.table) == self.raw.translate(self.table)
