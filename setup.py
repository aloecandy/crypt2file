from setuptools import setup, find_packages

setup(
    name='crypt2file',
    version='0.1.3',
    description='save/load a file with encryption/decryption',
    license='MIT',
    author='Kyunghonn',
    author_email='aloecandy@gmail.com',
    url='https://github.com/aloecandy/crypt2file',
    keywords=['crypt', 'file', 'encrypt'],
    install_requires=[
        'cryptography'
    ],
    packages=find_packages(exclude=['tests'])
)