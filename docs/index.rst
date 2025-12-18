fits2physical
===============

Overview
--------

fits2physical is a Python package to analyze FITS files, compute pixel and physical sizes, and generate plots.

Installation
============

You can install `fits2physical` directly from GitHub using:

.. code-block:: bash

    pip install git+https://github.com/siwakotiutsav/fits2physical.git

After that, use it in Python:

.. code-block:: python

    import f2p
    df = f2p.analyze("path/to/file.fits", distance_mpc=3.5)
    print(df)

API
---

.. automodule:: f2p
    :members:
    :undoc-members:
    :show-inheritance:
