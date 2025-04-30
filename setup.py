from setuptools import setup, find_packages
import os

# Read the content of README.md for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="anipie",
    version="0.0.11",
    author="Aritsu",
    author_email="lynniswaifu@gmail.com",
    description="A simple Python wrapper for the AniList API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aritsulynn/anipie",
    project_urls={
        "Bug Tracker": "https://github.com/aritsulynn/anipie/issues",
        "Documentation": "https://github.com/aritsulynn/anipie#readme",
        "Source Code": "https://github.com/aritsulynn/anipie",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",
        "Intended Audience :: Developers",
    ],
    keywords="anilist, anime, manga, api, wrapper",
    install_requires=["requests>=2.25.0"],
    python_requires=">=3.8",
)
