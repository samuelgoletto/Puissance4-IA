# from pathlib import Path
from setuptools import setup, find_packages

setup(
    name='game',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='',
    author='',
    author_email='',
    description='',
    python_requires='>=3.10',
    # install_requires=Path('requirements.txt').read_text(),
    entry_points={
        'console_scripts': [
            'game-play=game.main:main'
        ]
    }
)
