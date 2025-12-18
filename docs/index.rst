fits2physical
=============


Overview
--------
fits2physical is a Python package to analyze FITS files, compute pixel and physical sizes, and generate plots.  
It works for both 2D and 3D FITS data, and provides dimensions in pixels, angular, and physical units.  
The figure is automatically displayed when you run the analysis.

Installation
------------
Install via **PyPI** (recommended) or directly from **GitHub**:

.. code-block:: bash

    pip install f2p
    # or directly from GitHub
    pip install git+https://github.com/siwakotiutsav/fits2physical.git

Usage
-----
The workflow is simple: provide a FITS file path and distance in Mpc.

**Example code:**

.. code-block:: python

    import f2p

    # Analyze FITS file and automatically display figure
    df = f2p.analyze(
        "../data/ngc253/NGC253_sky_v1_17_1_ch3-shortmediumlong_s3d.fits",
        distance_mpc=3.5
    )

    # Print computed dimensions
    print(df)

Expected Output
---------------
The analysis returns a table of dimensions:

.. code-block:: text

       Quantity     Pixels                    Angular               Physical
    0    Length  85.529646   17.10592943977466 arcsec  290.26160171739974 pc
    1   Breadth  50.442038  10.088407695872492 arcsec  171.18493250494006 pc
    2  Diagonal  97.406365   19.48127334931105 arcsec   330.5675745813207 pc

Figure
------
The figure showing the measured dimensions is automatically displayed when `analyze()` is run.

.. image:: _static/example_plot.png
    :alt: FITS Analysis Figure
    :align: center
    :width: 80%


Data Source / Citation
----------------------
*Example FITS analysis of NGC 253.*  
Data are from **JWST Cycle 1 GO Programme 1701 (PI: Alberto D. Bolatto et al.)**, which includes high-resolution imaging of the starburst galaxy NGC 253.


Author
------
Utsav Siwakoti
