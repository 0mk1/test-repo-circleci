from setuptools import find_packages, setup

import test_repo


INSTALL_REQUIREMENTS = []


setup(
    name='test-repo',
    packages=find_packages(),
    include_package_data=True,
    version=test_repo.__version__,
    install_requires=INSTALL_REQUIREMENTS,
)
