# This setup.py file will be responsible for creating ML application as a package

from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."


def getRequirements(filepath: str) -> list:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open('requirements.txt') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        # if -e . is present in the requirements, then remove it
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="ml_app",
    version="0.1",
    author="Rashid",
    author_email="abdur363@gmail.com",
    packages=find_packages(),
    install_requires=getRequirements('requirements.txt')
)