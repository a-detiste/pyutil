#!/usr/bin/env python
# -*- coding: utf-8-with-signature-unix; fill-column: 77 -*-
# -*- indent-tabs-mode: nil -*-

# pyutil -- utility functions and classes
#
# This file is part of pyutil; see README.rst for licensing terms.

import versioneer
from setuptools import setup

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)

