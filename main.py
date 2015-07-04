#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  
#  Copyright 2015 Matteo Alessio Carrara <sw.matteoac@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import sys

if (len(sys.argv)<3):
	print "Uso: ff fakelogin_root_url nome1 [nome2 nome3 ... nomen]"
	exit(1)

import requests

for i in sys.argv[2:]:
	print sys.argv[1]+i, requests.head(sys.argv[1]+i).status_code
exit(0)