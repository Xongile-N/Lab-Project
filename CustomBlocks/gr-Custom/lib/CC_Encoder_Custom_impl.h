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

#ifndef INCLUDED_CUSTOM_CC_ENCODER_CUSTOM_IMPL_H
#define INCLUDED_CUSTOM_CC_ENCODER_CUSTOM_IMPL_H

#include <Custom/CC_Encoder_Custom.h>

namespace gr {
  namespace Custom {

    class CC_Encoder_Custom_impl : public CC_Encoder_Custom
    {
     private:
		int _constraint =0;
		int rate =2;
		int bitsIn=1;
		std::vector<uint8_t> codes;
		bool** polyCodes=NULL;
		bool * codeBuffer=NULL;
		bool skip=true;
		bool flush=false;
		bool done=false;
		size_t numElems=0;
		size_t _frameLength;
		size_t procCount=0;
		void encode(bool* ,bool*, const size_t );
		void BytesToBool(const uint8_t* ,bool* ,size_t );
		void BoolToBytes(bool* ,uint8_t* ,size_t );
		bool XOR(bool , bool );
		bool getBit(unsigned char , int );


     public:
      CC_Encoder_Custom_impl(int constraint, int frameLength, std::vector<int> polynomial);
      ~CC_Encoder_Custom_impl();

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace Custom
} // namespace gr

#endif /* INCLUDED_CUSTOM_CC_ENCODER_CUSTOM_IMPL_H */

