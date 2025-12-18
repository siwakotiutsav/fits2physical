fits2physical
===============

Overview
--------

fits2physical is a Python package to analyze FITS files, compute pixel and physical sizes, and generate plots.

Usage
-----

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
