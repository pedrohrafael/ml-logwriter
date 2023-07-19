from setuptools import setup
  
setup(
    name='ml_logwriter',
    version='0.1',
    url='https://github.com/pedrohrafael/ml-logwriter',
    description='A ML logger package',
    author='Pedro H Rafael',
    author_email='pedro.rodrigues.rafael@gmail.com',
    packages=['ml_logwriter'],
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