#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 6

# Upper part of the rhombus
for i in range(a):
    print(' ' * (a - i - 1) + '*' + ' ' * (2 * i - 1) + ('*' if i > 0 else ''))

# Lower part of the rhombus
for i in range(a - 2, -1, -1):
    print(' ' * (a - i - 1) + '*' + ' ' * (2 * i - 1) + ('*' if i > 0 else ''))