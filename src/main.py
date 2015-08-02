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

from sys import argv
import requests


if len(argv) < 3:
	print "Uso: ff fakelogin_root_url nome1 [nome2 nome3 ... nomen]"
	exit(1)

url = argv[1]

for nome in argv[2:]:
	print requests.head(url+nome).status_code, nome 
exit(0)