from setuptools import setup, find_packages

setup(
    name="tc-messageBroker",
    version="1.0.0",
    author="Mohammad Amin Dadgar, RnDAO",
    maintainer="Mohammad Amin Dadgar",
    maintainer_email="dadgaramin96@gmail.com",
    packages=find_packages(),
    description="Shared library for message broker in Python",
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "pytest",
    ],
)
