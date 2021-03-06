# Licensed under a 3-clause BSD style license - see LICENSE.rst

# Packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

# Enforce Python version check during package import.
# This is the same check as the one at the top of setup.py
import sys

class UnsupportedPythonError(Exception):
    pass

if sys.version_info < tuple((int(val) for val in "2.7".split('.'))):
    raise UnsupportedPythonError("qt_client does not support Python < {}".format(2.7))

if not _ASTROPY_SETUP_:
    # For egg_info test builds to pass, put package imports here.

    pass

