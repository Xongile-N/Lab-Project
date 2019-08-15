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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "CC_Encoder_Custom_impl.h"
#include vector;
namespace gr {
  namespace Custom {

    CC_Encoder_Custom::sptr
    CC_Encoder_Custom::make(int constraint, int frameLength, std::vector<int> polynomial)
    {
      return gnuradio::get_initial_sptr
        (new CC_Encoder_Custom_impl(constraint, frameLength, polynomial));
    }

    /*
     * The private constructor
     */
    CC_Encoder_Custom_impl::CC_Encoder_Custom_impl(int constraint, int frameLength, std::vector<int> polynomial)
      : gr::sync_interpolator("CC_Encoder_Custom",
              gr::io_signature::make(1, 1, sizeof(char)),
              gr::io_signature::make(1, 1, sizeof(char)), rate),
              constraint(constraint),
              frameLength(frameLength),

    {
      for(int i=0;i<rate;i++){
        codes.push_back((uint8_t)polynomial[i]);
      }
    }

    /*
     * Our virtual destructor.
     */
    CC_Encoder_Custom_impl::~CC_Encoder_Custom_impl()
    {
    }

    int
    CC_Encoder_Custom_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const  uint8_t*in = (const uint8_t *) input_items[0];
      uint8_t *out = (uint8_t*) output_items[0];


      bool* inBuffer=NULL;
      bool* outBuffer=NULL;
			numElems=noutput_items/rate;

			//outCount=(numElems*rate);
			//outCount+=(flushBits%8)>0?1:0;
			size_t flushBits=constraint*rate;
			size_t flushBytes=flushBits/8;

      uint8_t *temp=new uint8_t [noutput_items];
			inBuffer=new bool[numElems*8];
			outBuffer=new bool[numElems*8*rate];	
			BytesToBool(in,inBuffer,numElems);
			encode(inBuffer,outBuffer,numElems*8);
			BoolToBytes(outBuffer,temp,noutput_items );
      for(int i=0;i<noutput_items;i++){
        out[i]=temp[i];
      }
			std::memcpy(outElems.as<void *>(),temp,outCount);

			delete temp;
			temp=NULL;
			delete inBuffer;
			inBuffer=NULL;
			delete outBuffer;
			outBuffer=NULL;	
      // Do <+signal processing+>
      consume_each(noutput_items/rate); 
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }
    void CC_Encoder_Custom_impl::encode(bool* inBuffer,bool*outBuffer, const size_t numIn){

      //codes.push_back(15);
      //codes.push_back(11)	;	
      polyCodes=new bool*[rate];
      
      for(auto i=0;i<rate;i++){
        polyCodes[i]=new bool[constraint];
        for(auto j=0;j<constraint;j++){
          polyCodes[i][j]=0;
          polyCodes[i][j]=getBit(codes[i],j);
        }
      }
      
      
      codeBuffer=new bool[constraint];
      for(auto i=0;i<constraint;i++){
        codeBuffer[i]=0;		
      }
      for(size_t i=0;i<numIn;i+=bitsIn){
        if(procCount==frameLength){
          procCount=0;
          for(size_t i=numIn;i<constraint+numIn;i++){
            for(int j=constraint-1;j>bitsIn-1;j--){
              codeBuffer[j]=codeBuffer[j-1]	;		
            }
            for(int j=bitsIn-1;j>-1;j--){
              codeBuffer[j]=0	;		
            }
          }
        }
        procCount++;

        for(int j=constraint-1;j>bitsIn-1;j--){
          codeBuffer[j]=codeBuffer[j-1]	;		
        }
        for(int j=bitsIn-1;j>-1;j--){
          codeBuffer[j]=*(inBuffer+i+bitsIn-1-j)	;		
        }
        for(int j=0;j<rate;j++){
          bool out=0;
          for(int k=0;k<constraint;k++){
            bool poly=polyCodes[j][constraint-k-1]&&codeBuffer[k];
            out=XOR(out,poly);
          }
          *(outBuffer+i*rate+j)=out;			
        }	
      }

      for(auto i=0;i<rate;i++){
        delete polyCodes[i];
        polyCodes[i]=NULL;
      }
      delete polyCodes;
      polyCodes=NULL;
      delete codeBuffer;
      codeBuffer=NULL;
	  }
    void CC_Encoder_Custom_impl::BytesToBool(const uint8_t* oldBuff,bool* newBuff,size_t length){
      size_t offset=0;
      for(size_t i=0;i<length;i++){
        for(auto j=7;j>-1;j--){
          *(newBuff+offset)=getBit(*(oldBuff+i),j);	
          offset++;
        }	

      }
    }
    void CC_Encoder_Custom_impl::BoolToBytes(bool* oldBuff,uint8_t* newBuff,size_t length){
      size_t offset=0;
      for(size_t i=0;i<length;i++){
          for(int j=0;j<8;j++){
                *(newBuff+i)*=2;
            *(newBuff+i)+=*(oldBuff+offset);
          offset++;		

        }
      }
    }
    bool CC_Encoder_Custom_impl::XOR(bool A, bool B){
      return A!=B	;
    }
    bool CC_Encoder_Custom_impl::getBit(unsigned char byte, int position)    {
      //return false;
        return (byte >> position) & 0x1;
    }

  } /* namespace Custom */
} /* namespace gr */

