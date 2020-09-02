from setuptools import setup, Extension
from Cython.Distutils import build_ext
import numpy as np

NAME = "weighted-bipartite-cython"
VERSION = "0.1"
DESCR = "A small template project that shows how to wrap C/C++ code into python using Cython"
URL = "http://www.google.com"
REQUIRES = ['numpy', 'cython']

AUTHOR = "yuchen"
EMAIL = "chenyu414@gmail.com"

LICENSE = "Apache 2.0"

SRC_DIR = "hungarian"
PACKAGES = [SRC_DIR]

ext_1 = Extension("pyhungrarian",
                  [SRC_DIR + "/hungarian.cpp", SRC_DIR + "/pyhungarian.pyx"],
                  libraries=[],
                  include_dirs=[np.get_include()],
                  extra_compile_args=["-O3"],
                  language="c++"
        )


EXTENSIONS = [ext_1]

if __name__ == "__main__":
    setup(install_requires=REQUIRES,
          packages=PACKAGES,
          zip_safe=False,
          name=NAME,
          version=VERSION,
          description=DESCR,
          author=AUTHOR,
          author_email=EMAIL,
          url=URL,
          license=LICENSE,
          cmdclass={"build_ext": build_ext},
          ext_modules=EXTENSIONS
          )
