#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from __future__ import absolute_import, print_function, unicode_literals

from setuptools import find_packages, setup


with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

setup_requirements = [
    "pytest-runner",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Amninder S Narota",
    author_email="anarota@truveris.com",
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="This project contains all the slack event listeners",
    install_requires=requirements,
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="audicus",
    name="audicus",
    packages=find_packages(include=["audicus", "audicus.*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/amninder/audicus",
    version="0.1.0",
    zip_safe=False,
)
