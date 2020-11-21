import pathlib
from setuptools import find_packages, setup

here = pathlib.Path(__file__).parents[0]

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="NoodleExtensions",
    version="1.3.1",
    license='MIT license',
    description="Edit Beat Saber Noodle Extensions level easily using this library.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/megamaz/NoodleExtensions-python',
    author='megamaz',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.9'
    ],
    keywords='Beat Saber, Noodle Extensions',
    packages=find_packages(where='noodle_extensions'),
    python_requires='>=3.8, <4',
    project_urls={
        'Bug Reports': 'https://github.com/megamaz/NoodleExtensions-python/issues'
    }
)