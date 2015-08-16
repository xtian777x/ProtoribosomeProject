# ProtoribosomeProject

Installing Shapely (package to work with polygons, among other things)

First install GEOS library (SRC: http://geonode.readthedocs.org/en/2.0/tutorials/admin/install/install_postgis.html)

download the latest version from

http://trac.osgeo.org/geos/

untar and in the new folder do:

./configure
make
sudo make install

check version with

geos-config --version

After that I had to do 

sudo apt-get install libgeos-dev

Now Shapely

sudo pip install shapely

//With the latest version there's a bug using GEOS. The version that worked for me is 1.4.3:

sudo pip install "Shapely==1.4.3"

Shapely User Manual: http://toblerity.org/shapely/manual.html

TODO: Clean up this file and make a nice one