from setuptools import setup, find_packages


requirements = [requirement for requirement in open('requirements.txt')]

setup(
    name='apis',
    version='0.1',
    packages=find_packages(),
    description='Python package for API',
    author='SalemShaikh',
    author_email='salem.shaikh@cipla.com',
    url='https://github.com/salemshaikh/cip_api',
    install_requires=requirements
)