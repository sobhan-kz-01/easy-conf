from setuptools import setup,find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="easy-conf",
    version="0.0.1",
    author="sobhan-kz-01",
    description="work with config files in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),

)