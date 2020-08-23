
Project Description:
--------------------

The goal of this project is to develope a technique to use 
gravitational-wave observations from LIGO-Virgo detectors
of coalescing systems of neutron stars in binaries to 
generate sky-maps, and then combine them with catalogs of 
galaxies to get statistical measurement of the Hubble constant
. This technique is going to complement the existing blind 
statistical technique using binary black hole coalescence.
The advantage of this technique is that it reduces the statistical
trials-factor of a completely blind search by incorporating
electromagnetic observations from telescopes. The electromagnetic
observations are the various candidates that are found in the 
follow-up observations of the gravitational-wave triggers. The 
trials-factor that we will encounter in this case will be the 
false-positives rate from the various non-related transients in 
the searched volume, which is orders of magnitude smaller than 
the trials factor in the blind search that comes from the large 
number of galaxies in the searched volume. On the other hand
this method is less powerful than a targeted search (for which
an electromagnetic counterpart is already found). However, we 
only have one such candidate, and our compact binary rates 
estimates suggest that such events will be extremely rate. Thus
this new method sits very nicely between the two techniques of 
blind search and targeted search, complementing the shortcoming 
of the both.


Hubble Constant:
----------------

Astronomical observations suggests that almost all galaxies are 
moving away from us. The more distant the galxies faster is their
velocity of this receding motion from us. If we assume that we, on
Earth do not occupy a special position in the universe, then the 
only explanation of this galaxies moving away from us that the 
universe is expanding. In an expanding universe all galaxies are 
moving away from each other. This expansion is is described by
Hubble's law

v = H0 x D,

where v is the recessional velocity of the galaxies, and D is the 
proper distance to the respective galaxies. The quantity H0 is 
called the Hubble constant. The current best-known value of the 
Hubble constant is about 68 km/s/Mpc



Methods of measuring the Hubble constant:
-----------------------------------------

(1) Observation of Supernovae

(2) Cosmic Microwave Background Radiation

(3) Gravitational waves observation:
    (a) Blind observation of binary black hole coalescences.
    (b) Targeted measurement of H0 from GW event with confirmed 
        EM counterparts
    (c) EM counterpart candidates based statistical search 

The last work is the aim for this project.



How to setup the environment:
-----------------------------

Make sure you have jupyter installed. From your base environment run

$ conda install jupyter

Once you have done this, check that you are able to open Jupyter by running

$ jupyter notebook


First create a conda environment for this project:

$ conda create -n hubble pip

Then activate the environment

$ source activate hubble

Make sure that the python in this environment is the one that you want:

$ which python

This will show something like  <some-prefix-here>/hubble/bin/python

Now install the packages necessary for this work:

$ python -m pip install -r sky-maps/requirements.txt

Then setup the installed ipykernel for using Jupyter notebooks:

$ python -m ipykernel install --user --name=hubble

At this point your environment should be ready. Open the jupyter notebook,
using the command mentioned earlier. Open the notebok named Add_Redshift.ipynb
bly clicking it. This will open in a different tab on your browser.
Note that there is a tab called Kernel at the top menu bar. Click on that
and in the drop-down menu select `change kernel`. This will lead to another
menu that will pop up in the right. Select the environment you just created,
namely hubble. You should be able to run Jupyter here now. 

Now go through the notebook, running the cells by hitting shift + enter for each
one of them. Then read the task at the very bottom and complete it.


Basic knowledge: 
----------------

1. Celestial sphere

2. Concept of distance of astronomical objects

3. Expansion of the universe

4. Redshift 

5. Cosmic distance ladder

6. Large scale structure of the universe 



Distance measurement in gravitational waves:
--------------------------------------------




