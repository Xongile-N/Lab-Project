/* -*- c++ -*- */

#define CUSTOM_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "Custom_swig_doc.i"

%{
#include "Custom/CC_Encoder_Custom.h"
%}


%include "Custom/CC_Encoder_Custom.h"
GR_SWIG_BLOCK_MAGIC2(Custom, CC_Encoder_Custom);
