#!/usr/bin/env python
# -*- coding: utf-8; Mode: python; tab-width: 4; indent-tabs-mode:nil; -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
# 
# This file is part of FATSLiM --- http://fatslim.github.io/
# 
# Copyright (c) 2013-2018, Sébastien Buchoux
# Copyright (c) 2019, by the FATSLiM development team (see AUTHORS file)
#
# FATSLiM is free software and is released under the GNU Public Licence,
# v3 or any higher version
#
# If you use FATSLiM in publised work, please cite:
#
# S. Buchoux.
# FATSLiM: a fast and robust software to analyze MD simulations of membranes.
# Bioinformatics 33(1) (2017), 133--134, doi:10.1093/bioinformatics/btw563
#
import sys

from setuptools import setup
from setuptools import Extension
from setuptools.command.test import test as TestCommand

# Handle cython modules
from Cython.Build import cythonize

import numpy

cmdclass = {}


# Test command
class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        # Default py.test options (overriden if --pytest-args/-a is set)
        self.pytest_args = ["-v", "-x", "--durations=3", "--tb=short"]

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        print("py.test args: '%s'" % self.pytest_args)
        errno = pytest.main(self.pytest_args)
        if errno != 0:
            print("Ouch... Congratulations! you probably found a bug!")
            print("Please contact the FATSLiM devs with this output so they can work it out!")
        sys.exit(errno)


cmdclass['test'] = PyTest

typedefs_ext = Extension("fatslim._typedefs",
                      ["fatslim/_typedefs.pyx"],
                        include_dirs=[numpy.get_include()],)

geometry_ext = Extension("fatslim._geometry",
                      ["fatslim/_geometry.pyx"],
                        include_dirs=[numpy.get_include()],)

core_ext = Extension("fatslim._core",
                      ["fatslim/_core.pyx"],
                        include_dirs=[numpy.get_include()],
)
setup(name='fatslim',
      ext_modules=cythonize([typedefs_ext, geometry_ext, core_ext]),
      cmdclass=cmdclass
      )
