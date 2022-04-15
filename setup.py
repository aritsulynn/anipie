import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anipie", 
    version="0.0.2",
    author="Ritsu",
    author_email="lynniswaifu@gmail.com",
    description="a simple python wrapper for the Anilist API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires= ['requests'],
    python_requires='>=3.6',
)