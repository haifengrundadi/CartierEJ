#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abc import ABCMeta
import logging

logger = logging.getLogger(__name__)


class BaseAction(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def action(self):
        NotImplemented
