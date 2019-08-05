#!/bin/sh
export LD_LIBRARY_PATH=/usr/lib:${LD_LIBRARY_PATH}
export DYLD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${DYLD_LIBRARY_PATH}
"/usr/bin/PothosUtil" $@
