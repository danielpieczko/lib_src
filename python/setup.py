# Copyright 2020-2024 XMOS LIMITED.
# This Software is subject to the terms of the XMOS Public Licence: Version 1.
import setuptools

# Another repository might depend on python code defined in this one.  The
# procedure to set up a suitable python environment for that repository may
# pip-install this one as editable using this setup.py file.  To minimise the
# chance of version conflicts while ensuring a minimal degree of conformity,
# the 3rd-party modules listed here require the same major version and at
# least the same minor version as specified in the requirements.txt file.
# The same modules should appear in the requirements.txt file as given below.
setuptools.setup(
    name='lib_src',
    packages=setuptools.find_packages(),
    install_requires=[
        'matplotlib==3.9.2',
        'numpy==2.1.1',
        'soundfile==0.12.1',
        'scipy==1.14.1',
        'mpmath==1.3.0',
        'bitstring==4.2.3'
    ],
    dependency_links=[
    ],
)
