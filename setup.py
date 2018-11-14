from setuptools import setup

setup(
    name='Desenra',
    version='1.0',
    packages=['desenra'],
    install_requires=['youtube-dl', 'discord.py', 'ffmpeg'],
    url='https://github.com/Squantonias/DesenraBot',
    license='',
    author='Anthony Stonto',
    author_email='Squantonias@gmail.com',
    description='The Desenra Discord bot',
    entry_points={
        "console_scripts": [
            "desenra = desenra.__main__:main",
        ]
    }
)
