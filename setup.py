from setuptools import setup, find_packages

setup(
    name='socialmedia',
    author='leres',
    version='1.0',
    author_email='whereim@onthe.net',
    description='Your description here',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf' ] # list of resources
    },
    install_requires=[
        # Name of packages required for easy_install
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)