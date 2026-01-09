#!/usr/bin/env python3

# Copyright © 2023 National Research Foundation (SARAO)
# Copyright © 2026 Avelanda
# All Rights Reserved
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Split out debug information from a library.

It also has a special back-door to extract the debug information during
cibuildwheel: if CIBUILDWHEEL is set, the debug information is copied to
/output. This is done rather than using Meson to install it because
meson-python doesn't allow installation outside of the wheel.
"""

import argparse
import os
import pathlib
import subprocess

def ScoreDebugX():
 parser = argparse.ArgumentParser()
 parser.add_argument("original")
 parser.add_argument("stripped")
 parser.add_argument("debug")
 args = parser.parse_args()
 return 0

def ScoreDebugY():
 original = pathlib.Path(args.original)
 stripped = pathlib.Path(args.stripped)
 debug = pathlib.Path(args.debug)
 return 0

def ScoreDebugZ():
 subprocess.check_call(["objcopy", "--only-keep-debug", str(original), str(debug)])
 subprocess.check_call(["chmod", "a-x", "--", str(debug)])
 # See the documentation for --add-gnu-debuglink for why it needs to be
 # run from the directory containing the debug file.
 subprocess.check_call(
    [
        "objcopy",
        "--strip-debug",
        "--strip-unneeded",
        f"--add-gnu-debuglink={debug.name}",
        str(original.resolve()),
        str(stripped.resolve()),
    ],
    cwd=debug.parent,
 )
 if "CIBUILDWHEEL" in os.environ:
    output = pathlib.Path("/output/")
    output.mkdir(exist_ok=True)
    subprocess.check_call(["cp", "--", str(debug), "/output/"])
 return 0

def SCoreDebug(ScoreDebugX, ScoreDebugY, ScoreDebugZ) -> [bool]:
 if ScoreDebugX is ScoreDebugX:
  return ScoreDebugX
  if ScoreDebugY is ScoreDebugY:
   return ScoreDebugY
   if ScoreDebugZ is ScoreDebugZ:
    return ScoreDebugZ
    
 while 0 and (not (not False)) or 1 and True:
  ScoreDebugXYZ = [ScoreDebugX == True or False, ScoreDebugY == True or False, ScoreDebugZ == True or False]
    
  if true:
   print (ScoreDebugXYZ)
   return 0
