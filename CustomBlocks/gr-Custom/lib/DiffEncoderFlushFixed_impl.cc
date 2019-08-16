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
#include "DiffEncoderFlushFixed_impl.h"

namespace gr {
  namespace Custom {

    DiffEncoderFlushFixed::sptr
    DiffEncoderFlushFixed::make(int modulus, bool flush, int flushLength)
    {
      return gnuradio::get_initial_sptr
        (new DiffEncoderFlushFixed_impl(modulus, flush, flushLength));
    }

    /*
     * The private constructor
     */
    DiffEncoderFlushFixed_impl::DiffEncoderFlushFixed_impl(int modulus, bool flush, int flushLength)
      : gr::block("DiffEncoderFlushFixed",
              io_signature::make(1, 1, sizeof(unsigned char)),
              io_signature::make(1, 1, sizeof(unsigned char))),
              toFlush(flush),
              _modulus(modulus),
              _flushLength(flushLength),
              procCount(0)
      {
            set_history(2); // need to look at two inputs
              set_output_multiple(_flushLength-8);

      }

    /*
     * Our virtual destructor.
     */
    DiffEncoderFlushFixed_impl::~DiffEncoderFlushFixed_impl()
    {
    }

    void
    DiffEncoderFlushFixed_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
                  ninput_items_required[0] =2*noutput_items;
      std::cout<<"Forecast"<<ninput_items_required[0]<<" "<<noutput_items<<std::endl;
      //ninput_items_required[0] =_flushLength*(int)noutput_items/(_flushLength-8);
    }

    int
    DiffEncoderFlushFixed_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const unsigned char* in = (const unsigned char*)input_items[0];
      unsigned char* out = (unsigned char*)output_items[0];
      int offset=0;
      in += 1; // ensure that in[-1] is valid
      unsigned modulus = _modulus;
      int outCount=ninput_items[0];
      /*
      for (int i = 0; i < noutput_items; i++) {
          unsigned char curr=in[i];
          unsigned char prev=in[i-1];


          if(toFlush&&procCount==_flushLength){
            procCount=0;
            removedCount=0;
          }
          
          if(toFlush&&removedCount<8){
            removedCount++;
            outCount--;
          }
          else{
            out[offset] = (curr - prev) % modulus;
            offset++;
          }
          procCount++;

        }
        if(noutput_items<=1){
            procCount=0;
            removedCount=0;
        }
      */
      consume_each(ninput_items[0]);
      std::cout<<_flushLength<<" "<<_flushLength*(int)noutput_items/(_flushLength-8)<<" "<<noutput_items<<std::endl;
      std::cout<<ninput_items[0]/_flushLength<<"<-Count"<<ninput_items[0]<<" <-In "<<outCount<<"<-Out->"<<noutput_items<<std::endl;
      return noutput_items;
    }

  } /* namespace Custom */
} /* namespace gr */

