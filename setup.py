from setuptools import setup, find_packages

setup(
    name='ml_logwriter',
    version='0.1',
    url='https://github.com/pedrohrafael/ml-logwriter',
    license='MIT',
    description='A ML logger package',
    author='Pedro H Rafael',
    author_email='pedro.rodrigues.rafael@gmail.com',
    packages=find_packages(),
    long_description=open('README.md').read(),
)