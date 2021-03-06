"""A setuptools based setup module for `py-irobot`."""

from setuptools import setup, find_packages

with open("requirements.txt") as f:
    dependencies = f.read().split("\n")

with open("version.txt") as f:
    version = f.readline().strip()

setup(
    name="py-irobot",
    packages=find_packages(exclude=["tests"]),
    version=version,
    description="iRobot Roomba API",
    author="Peter Hagelund",
    author_email="peterhagelund@mac.com",
    url="https://github.com/peterhagelund/py-irobot.git",
    keywords=["irobot", "roomba", "api"],
    install_requires=dependencies,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Robotics",
        "Programming Language :: Python :: 3.9",
    ],
)
