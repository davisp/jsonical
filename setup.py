#
# Copyright 2009 New England Biolabs <davisp@neb.com>
#
# This file is part of the nebgb package released under the MIT license.
#

import os
from distutils.core import setup

long_desc = """
Canonical serializations for JSON.

Similar to the basic API for the `json`/`simplejson` modules with
a few restrictions on modifiying serialization.
"""


setup(
    name = "jsonical",
    description = "Canonical JSON",
    long_description = long_desc,
    author = "Paul Joseph Davis",
    author_email = "paul.joseph.davis@gmail.com",
    url = "http://github.com/davisp/jsonical",
    version = "0.0.1",
    license = "MIT",
    keywords = "JSON canonical serialization",
    platforms = ["any"],
    zip_safe = True,
    py_modules = ["jsonical"]
)
