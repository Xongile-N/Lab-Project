/* -*- c++ -*- */
/* 
 * Copyright 2019 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_CUSTOM_CCDECODER_IMPL_H
#define INCLUDED_CUSTOM_CCDECODER_IMPL_H

#include <Custom/CCDecoder.h>
#include "ViterbiNode.h"

namespace gr {
  namespace Custom {

    class CCDecoder_impl : public CCDecoder
    {
     private:
      int _constraint =0;
      int rate =2;
      uint8_t stateCount=0;
      int bitsIn=1;
      std::vector<uint8_t> codes;
      
      bool** polyCodes=NULL;
      bool * codeBuffer=NULL;

      
      int decodeOutput=5000;
      uint8_t ** trellis;
      int stateAttri=7;
      int currState=0;
      int zeroNext=1;
      int zeroOutput=2;
      int oneNext=3;
      int oneOutput=4;
      int prev_0=5;
      int prev_1=6;
      
      ViterbiNode ** nodes;
      
      bool done=false;
      size_t numElems=0;
      int _frameLength;
      bool flush=true;
      size_t procCount=0;
      int Decode(const bool* ,bool*, const size_t);
      void destroyTrellis();
      void buildTrellis(int ,std::vector<uint8_t> ,int );
      int getHammingDist(uint8_t,uint8_t );
      bool getBit(unsigned char , int);
      bool XOR(bool , bool );
      void BytesToBool(const uint8_t* ,bool* ,size_t );
      void BoolToBytes(bool* ,uint8_t* ,size_t );
     public:
      CCDecoder_impl(int constraint, int frameLength, std::vector<int> polys);
      ~CCDecoder_impl();

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace Custom
} // namespace gr

#endif /* INCLUDED_CUSTOM_CCDECODER_IMPL_H */

