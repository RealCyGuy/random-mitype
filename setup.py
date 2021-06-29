from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

exec(open("version.py").read())


setup(
    name="random-mitype",
    version=__version__,
    py_modules=["random_mitype"],
    description="Generate random typing tests for mitype.",
    long_description=long_description,
    author="Cyrus Yip",
    install_requires=["Click", "mitype"],
    entry_points={"console_scripts": ["random-mitype = random_mitype:cli",],},
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python 3",
        "Programming Language :: Python :: Implementation :: CPython"
        "Natural Language :: English",
        "Topic :: Terminals",
        "Environment :: Console :: Curses",
        "Development Status :: 4 - Beta",
    ],
)
