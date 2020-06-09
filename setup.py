from setuptools import setup
import os


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


extra_files = package_files('8fact')

setup(
    name='py8fact',
    version='0.1.0',
    packages=['py8fact'],
    url='https://github.com/OpenJarbas/8fact',
    package_data={'': extra_files},
    include_package_data=True,
    license='Apache2.0',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    description='random facts'
)
