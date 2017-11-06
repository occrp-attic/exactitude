from setuptools import setup, find_packages


setup(
    name='exactitude',
    version='2.0.1',
    description="A library with real-world data parsers.",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='names countries phones domains email country',
    author='Friedrich Lindenberg',
    author_email='friedrich@pudo.org',
    url='http://github.com/alephdata/dalet',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'test']),
    namespace_packages=[],
    package_data={},
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        'six >= 1.11.0',
        'normality >= 0.5.3',
        'babel >= 2.5.1',
        'urlnormalizer >= 1.0.3',
        'countrynames >= 1.2',
        'parsedatetime >= 2.1',
        'phonenumbers >= 8.8.4'
    ],
    tests_require=['nose'],
    entry_points={}
)
