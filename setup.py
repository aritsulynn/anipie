from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\\n" + fh.read()

setup(
    name="anipie", 
    version='{{VERSION_PLACEHOLDER}}',
    author="Aritsu",
    author_email="lynniswaifu@gmail.com",
    description="a simple python wrapper for the Anilist API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aritsulynn/anipie",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires= ['requests'],
    python_requires='>=3.6',
)