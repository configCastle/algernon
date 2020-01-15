from setuptools import find_packages, setup


install_requires = [
    'aiohttp==3.6.2'
]


setup(
    name='algernon_backend',
    version=0.1,
    platforms=['POSIX'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)
