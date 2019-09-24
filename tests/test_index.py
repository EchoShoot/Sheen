# -*- coding: utf-8 -*-
# @Time    : 2019-09-01 18:21
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : test_index.py
# @Explain :

from sheen import Str
import pytest


class TestIndex(object):
    raw = 'xxooAß西xoox'
    obj = Str.red(raw)
    obj[2:-2] = Str.green
    obj[4:-4] = Str.blue
    obj[5:-5] = Str.magenta

    def test_index(self):
        with pytest.raises(ValueError):
            self.obj.index('echoshoot')
        assert self.obj.index(Str.green('xo')) == 7
        assert self.obj.index(Str.red('x') + Str.green('o')) == 1
        assert self.obj.index('xo') == 1

    def test_rindex(self):
        with pytest.raises(ValueError):
            self.obj.rindex('echoshoot')
        assert self.obj.rindex(Str.green('xo')) == 7
        assert self.obj.rindex(Str.red('x') + Str.green('o')) == 1
        assert self.obj.rindex('xo') == 7
