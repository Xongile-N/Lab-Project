#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/xongile/Lab-Project/CustomBlocks/gr-Custom/lib
export PATH=/home/xongile/Lab-Project/CustomBlocks/gr-Custom/build/lib:$PATH
export LD_LIBRARY_PATH=/home/xongile/Lab-Project/CustomBlocks/gr-Custom/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-Custom 
