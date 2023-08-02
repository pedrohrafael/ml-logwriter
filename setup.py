from setuptools import setup, find_packages

setup(
    name='ml_logwriter',
    version='0.2.3',
    url='https://github.com/pedrohrafael/ml-logwriter',
    license='MIT',
    description='A ML logger package',
    author='Pedro H Rafael',
    author_email='pedro.rodrigues.rafael@gmail.com',
    packages=find_packages(),
    long_description_content_type='text/markdown',
    long_description=open('README.md', encoding='utf-8').read()
    
)