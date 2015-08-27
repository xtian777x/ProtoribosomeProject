# ProtoribosomeProject

* Installing Shapely (package to work with polygons, among other things)

** Install GEOS library (SRC: http://geonode.readthedocs.org/en/2.0/tutorials/admin/install/install_postgis.html)

//These are the instructions that worked for me on Ubuntu 12.04. For 14.04 skip to 4)

1) Download the latest version from

http://trac.osgeo.org/geos/

2) untar and in the new folder do:

./configure

make

sudo make install

3) check version with

geos-config --version

4) After that I had to do:

sudo apt-get install libgeos-dev

** Now Shapely. 

Usually you would do just:

sudo pip install shapely

But with the latest version there's a bug using GEOS. The version that worked for me is 1.4.3:

sudo pip install "Shapely==1.4.3"

Shapely User Manual: http://toblerity.org/shapely/manual.html

TODO: Clean up this file and make a nice one