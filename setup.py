
from setuptools import setup, find_packages
setup(name='pathology',
      version='0.1',
      url='https://github.com/the-gigi/pathology',
      license='MIT',
      author='Gigi Sayfan',
      author_email='the.gigi@gmail.com',
      description='Add static script_dir() method to Path',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)
    
setup(
    name='ml_logwriter',
    version='0.1',
    url='https://github.com/pedrohrafael/ml-logwriter',
    description='A ML logger package',
    author='Pedro H Rafael',
    author_email='pedro.rodrigues.rafael@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'os', 
        'sys',
        'random',
        'hashlib',
        'joblib',
        'datetime',
        'logging'
    ],
)