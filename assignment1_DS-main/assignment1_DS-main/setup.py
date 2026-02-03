from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Topsis-Yashik-102303706",
    version="1.0.0",
    author="Yashik",
    author_email="Yashikgoyal@gmail.com",
    description="A Python package to implement TOPSIS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yashik-Goyal/ds1/tree/main/assignment1_DS-main",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "topsis=Topsis_Yashik_102303706.topsis:main",
        ],
    },
)
