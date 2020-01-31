from setuptools import setup, find_packages

reqs = ['daiquiri', 'simple_salesforce']

test_reqs = ['ipython', 'pytest', 'pytest-sugar', 'pytest-cov', 'pylint']

setup(
    name='heartcrm',
    description='A Python utility for generating reports from the HEART CRM.',
    author='Matt Robinson',
    author_email='matt@fiddleranalytics.com',
    packages=find_packages(),
    version='0.1.0',
    install_requires=reqs,
    extras_require={
        'test': test_reqs
    }
    entry_points = {
        'console_scripts':'heartcrm=hearcrm.cli:main'
    }
)
