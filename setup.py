from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(
    name='geocluster',
    version='1.0',
    author='Safia Ahmedou',
    description='clusteting spatial data',
    url='https://github.com/Safiaaaaa/geocluster',
    keywords='spacial data, clustering, mapping, social data',
    # python_requires='>=3.7, <4',
    packages=find_packages(),
    include_package_data=True,
    install_requires= requirements,
    # package_data={
    #     'sample': ['sample_data.csv'],
    # },
    # entry_points={
    #     'runners': [
    #         'sample=sample:main',
    #     ]
    # }
)