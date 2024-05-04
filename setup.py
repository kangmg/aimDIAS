from setuptools import setup, find_namespace_packages

setup(
    name='aimDIAS',
    version='1.0.1',
    author='Kang mingi',
    author_email='kangmg@korea.ac.kr',
    description='SUPER FAST D/I analysis with aimnet2',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  
    url='https://github.com/kangmg/aimDIAS',
    keywords=['chemistry','computational chemistry','machine learning'],
    include_package_data=True,
    packages=find_namespace_packages(), 
    install_requires=[
        'matplotlib',
        'numpy',
        'requests',
        'ase>=3.22.1',
        'torch>=2.2.1',
        'rdkit>=2023.09.6',
        'py3Dmol>=2.1.0'
    ],
    classifiers=[ 
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Chemistry'
    ],
    python_requires='>=3.10.0',
)
