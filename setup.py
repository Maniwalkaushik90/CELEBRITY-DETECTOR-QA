from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Celebrity Detector and QA",
    version="0.1",
    author="Manish Kumar",
    packages=find_packages(),
    install_requires = requirements,
)