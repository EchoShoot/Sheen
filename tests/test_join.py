# -*- coding: utf-8 -*-
# @Time    : 2019-09-01 20:52
# @Author  : EchoShoot
# @Email   : BiarFordlander@gmail.com
# @URL     : https://github.com/EchoShoot
# @File    : test_join.py
# @Explain :
from sheen import Str


class TestJoin(object):
    def test_join(self):
        assert Str.red(',').join(['1', '2', '3', '4']) == ','.join(['1', '2', '3', '4'])
        assert Str.red('!!!').join(['1', '2', '3', '4']) == '!!!'.join(['1', '2', '3', '4'])
        assert Str.red(',').join(['1', Str.blue('2'), '3', '4']) == ','.join(['1', '2', '3', '4'])
        assert Str.red(',').join(['1', Str.blue('2'), '3', '4']) != Str.red(',').join(['1', Str.red('2'), '3', '4'])
        assert Str.red(',').join(['1', Str.blue('2'), '3', '4']) != Str.red(',').join(['1', '2', Str.red('3'), '4'])
