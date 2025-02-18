#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2025 Shlomi Fish < https://www.shlomifish.org/ >
#
# Licensed under the terms of the MIT license.

"""

"""
import re

with open('src.xhtml', 'rt') as infh:
    src = infh.read()

for bef in [False, True]:
    for mid in [False, True]:
        for aft in [False, True]:
            fn = "test-{}-{}-{}.xhtml".format(
                ("beforeslash" if bef else "nobeforeslash"),
                ("middle" if mid else "nomiddle"),
                ("aftertag" if aft else "noaftertag"),
            )

            def repl(m):
                return " " * bef + "/" + " " * mid + ">" + " " * aft
            newtxt = re.sub("\\s*/\\s*>\\s*", repl, src)

            with open('dest-lynx-test/{}'.format(fn), 'wt') as o:
                o.write(newtxt)
