from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

# exec(open("random_mitype/version.py").read())

setup(
    name="random_mitype",
    version="0.1.3",
    packages=find_packages(),
    include_package_data=True,
    description="Generate random typing tests for mitype.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Cyrus Yip",
    install_requires=["Click"],
    entry_points={"console_scripts": ["random-mitype=random_mitype.random_mitype:cli", ], },
    license="MIT",
    url="https://github.com/RealCyGuy/random-mitype",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Natural Language :: English",
        "Topic :: Terminals",
        "Environment :: Console :: Curses",
        "Development Status :: 4 - Beta",
    ],
)
