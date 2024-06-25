import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

if __name__ == '__main__':
    install('setuptools')

from setuptools import setup, find_packages

setup(
    name='aimo',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
    ],
    author='yoooousir',
    author_email='your-email@example.com',
    description='A description of your package',
    #long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yoooousir/aimo',
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
)
