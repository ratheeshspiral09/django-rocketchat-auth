import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-rocketchat-auth',
    version='1.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Authenticate Rocket.Chat with Django Framework',
    long_description=README,
    url='https://rodorgas.github.com/django-rocketchat-auth',
    author='Rodrigo Orem',
    author_email='orem.rodrigo@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Communications :: Chat',
    ],
    install_requires=[
        'pymongo',
    ],
)
