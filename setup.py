from setuptools import setup, find_packages


setup(
    name='example_publish_pypi_medium',
    version='0.1',
    license='MIT',
    author="Mustafa Qazi",
    author_email='mus.qazi999@gmail.com',
    packages=['cygnusdatautils'],
    description='Data utils for cygnus',
    url='https://github.com/CygnusAIInternal/cygnusdatautils',
    keywords='cygnus data utils',
    install_requires=[
            'pandas',
            'numpy',
            'psycopg2-binary'
      ],

)