'''
Copyright 2010 Pearson Education, Inc.
This program is free software:
you can redistribute it and/or modify it under the terms of the GNU General
 Public License as published by the Free Software Foundation,
 either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
GNU General Public License for more details.

You should have received a copy of the GNU General Public License 
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
import random


def get_int(msg, minimum, default):
    while True:
        try:
            line = input(msg)
            if not line and default is not None:
                return default
            i = int(line)
            if i < minimum:
                print("must be >=", minimum)
            else:
                return i
        except ValueError as err:
            print(err)


rows = get_int("rows: ", 1, None)
columns = get_int("columns: ", 1, None)
minimum = get_int("minimum (or Enter for 0): ", -1000000, 0)

default = 1000
if default < minimum:
    default = 2 * minimum

maximum = get_int("maximum (or Enter for " + str(default) + "): ", minimum, default)

row = 0
while row < rows:
    line = " "
    column = 0
    while column < columns:
        i = random.randint(minimum, maximum)
        s = str(i)
        while len(s) < 10:
            s = " " + s
            line += s
            column += 1
        print(line)
        row += 1
