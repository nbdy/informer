from setuptools import setup, find_packages

setup(
    long_description_content_type="text/markdown",
    long_description=open("readme.md", "r").read(),
    name="site_informer",
    version="0.42",
    description="informs upon website changes",
    author="Pascal Eberlein",
    author_email="pascal@eberlein.io",
    url="https://github.com/smthnspcl/informer",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
)
