from setuptools import setup, find_packages

setup(
    name="projectdump",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'projectdump=projectdump.__main__:main',  # gọi hàm main() trong __main__.py
        ],
    },
)

