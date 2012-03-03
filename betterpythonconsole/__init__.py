#!/usr/bin/env python

#    This file is part of the Better Python Console Plugin for Gedit
#    Copyright (C) 2007 Zeth Green <zethgreen@gmail.com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""IDLE like Console for Gedit, hit F5 and it executes the module"""

import gtk
import gedit
import consolefunctions
import sys

class BetterConsolePlugin(gedit.Plugin):
    """This Class creates the Gedit plugin. """
    def __init__(self):
        gedit.Plugin.__init__(self)
        self._instances = {}

    def activate(self, window):
        """This adds the plugin to the running Gedit. This method is used
        when the plugin is turned on and then when Gedit starts"""
        home_path = __path__[0]
        self._instances[window] = \
        consolefunctions.BetterConsoleHelper(self, window, home_path)

    def deactivate(self, window):
        """This removes the plugin from the running Gedit."""
        self._instances[window].deactivate()
        del self._instances[window]

    def update_ui(self, window):
        """We do not use this yet."""
        self._instances[window].update_ui()
