#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Jérémie CUADRADO <redbeard28>
# https://github.com/redbeard28
# https://redbeard-consulting.fr


def getMyIp():
    clientip = web.ctx['ip']
    return clientip


if __name__ == '__main__':
    getMyIp()