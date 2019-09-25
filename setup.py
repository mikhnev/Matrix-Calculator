import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mcalc",
    version="0.0.1",
    author="Denis Mikhnev and Vlad Orlov",
    author_email="denis.mikhnev@gmail.com",
    description="Python3 project for cmc msu course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mikhnev/Matrix-Calculator",
    packages=setuptools.find_packages(),
    setup_require=["mo_installer"],
    locale_src='./mcalc/locale',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
