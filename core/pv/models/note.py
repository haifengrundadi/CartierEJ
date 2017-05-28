#!/usr/bin/env python
# -*- coding: utf-8 -*-

from core.pv.models import BasePageModel
import logging

logger = logging.getLogger(__name__)


class NoteModel(BasePageModel):
    def __init__(self, driver):
        self.driver = driver

    def click(self):
        pass

