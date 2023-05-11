from setuptools import setup, find_packages

setup(
    name='tc-messageBroker',
    version='0.0.1',
    author='Mohammad Amin Dadgar, RnDAO',
    maintainer='Mohammad Amin Dadgar',
    maintainer_email='dadgaramin96@gmail.com',
    packages= find_packages(),
    description='Shared library for message broker in Python',
    long_description=open('README.md').read(),
    install_requires=[
        "pytest",
    ],
)
