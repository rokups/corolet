from setuptools import setup


setup(
    name='corolet',
    version='0.0.1',
    py_modules=['corolet'],
    install_requires=['greenlet'],
    author='Ben Pringle',
    author_email='ben.pringle@gmail.com',
    url='http://github.com/Pringley/corolet',
    description='Use greenlets as coroutines in asyncio',
    license='MIT',
)
