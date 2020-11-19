#!/usr/bin/env python

from setuptools import setup, find_packages
from python_modhex._version import __version__

setup(
    name="python_modhex",
    version=__version__,
    description="Very simple modhex library when working with yubikey OTPs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Norman Moeschter-Schenck",
    author_email="<norman.moeschter@gmail.com>",
    maintainer="Norman Moeschter-Schenck",
    maintainer_email="<norman.moeschter@gmail.com>",
    url="https://github.com/normoes/python_modhex",
    download_url=f"https://github.com/normoes/python_modhex/archive/{__version__}.tar.gz",
    packages=find_packages(exclude=["tests*"]),
    scripts=["bin/python_modhex"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
    ],
)
