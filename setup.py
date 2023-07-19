import setuptools
import os.path


setuptools.setup(
    name='pyboard',
    version='1.0',
    license='MIT License',
    author='Kevin Pontes',
    author_email='kevboyz@pm.me',
    description='TUI Interface based for board applications',
    long_description='''''',
    url='https://github.com/KevBoyz/PyBoard',
    keywords='''
            
             ''',
    python_requires=">=3.11",
    packages=setuptools.find_packages(
        os.path.join(os.path.dirname(__file__), 'src')),
    zip_safe=True,
    classifiers=[

    ]
)
