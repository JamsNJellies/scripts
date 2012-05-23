#!/usr/bin/env python

import os

os.system("sudo pacman -Sy")
packages = os.popen("pacman -Qu | egrep -vi '^(Checking|warning|Remove|Total)'").read().strip()
packages = ", ".join(packages.splitlines())
if packages != "":
    os.system("echo 'Pacman Updates: "+ packages +"' | dzen2 -p 20 -bg '#dc322f'")
