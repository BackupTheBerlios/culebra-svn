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

"""refactoring - Refactoring display classes for Culebra

This module contains refactoring display clasess for Culebra.
"""


import os
import sys

import pygtk
pygtk.require('2.0')
import gtk

#Local modules
import brm

brmrefactor = brm.BRMCulebra()
brmrefactor.initialize()

class Refactor:
    def __init__(self, parent):
        self.editwindow = parent
        pass
    
    def on_find_ref_activated(self, *args):
        print "on_find_ref_activated(self, *args)", args
        name, buff, text, model = self.editwindow.get_current()
        
        if text is None:
            return
            
        tabwidth = text.get_tabs_width()

        iter = buff.get_iter_at_mark(buff.get_insert())

        row = iter.get_line() + 1

        start = iter
        start.set_line_offset(0)
        col = 0

        while not start.equal(iter):
            if start.get_char == '\t':
                col += (tabwidth - (col % tabwidth))
            else:
                col += 1
                start = start.forward_char()
        brmrefactor.find_references(name, row, 9)
        pass
    
