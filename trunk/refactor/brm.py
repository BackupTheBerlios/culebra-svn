#!/usr/bin/env python
#
# Copyright (C) 2005 Baiju M <baijum81(at)gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""brm - Bicycle Repair Man based module for refactoring

This module contains BRM based clasess for refactoring in Culebra

Example :- 

>>> import brm
>>> refactor = brm.BRMCulebra()
>>> refactor.initialize()
>>> refactor.find_references('brm.py', 32, 8)
Scanning /home/baiju/wd/culebra/trunk/refactor/brm.py

/home/baiju/wd/culebra/trunk/refactor/brm.py:43:  100% confidence

>>>
"""

__all__ = ["Refactor"]

__author__ = 'Baiju M <baijum81(at)gmail.com>'
__license__ = 'GPL'
__version__ = '0.1'

import bike

class CulebraLogger:
    def __init__(self):
        self.msg = ""

    def write(self, output):
        self.msg = self.msg + output
        if output.endswith("\n"):
            print self.msg
            self.msg = ""

#For time being this is the logger
logger = CulebraLogger()

class BRMCulebra:
    def __init__(self):
        pass

    def initialize(self):
        self.brmctx = bike.init()
        self.brmctx.setProgressLogger(logger)

    def find_references(self, filename, line, column):
        refs = self.brmctx.findReferencesByCoordinates(filename, line, column)
        for ref in refs:
            print ref.filename + ":" + str(ref.lineno) + ":  " + \
                  str(ref.confidence) + "% confidence\n"
