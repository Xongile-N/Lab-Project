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
#include "DiffEncoderFlush_impl.h"

namespace gr {
  namespace Custom {

    DiffEncoderFlush::sptr
    DiffEncoderFlush::make(int modulus, bool flush, int flushLength )
    {
      return gnuradio::get_initial_sptr
        (new DiffEncoderFlush_impl(modulus, flush, flushLength));
    }

    /*
     * The private constructor
     */
    DiffEncoderFlush_impl::DiffEncoderFlush_impl(int modulus, bool flush, int flushLength )
      : gr::sync_block("DiffEncoderFlush",
                 io_signature::make(1, 1, sizeof(unsigned char)),
                 io_signature::make(1, 1, sizeof(unsigned char))),
              toFlush(flush),
              _modulus(modulus),
              _flushLength(flushLength),
              _lastOut(0),
              procCount(0)
    {}

    /*
     * Our virtual destructor.
     */
    DiffEncoderFlush_impl::~DiffEncoderFlush_impl()
    {
    }

    int
    DiffEncoderFlush_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const unsigned char* in = (const unsigned char*)input_items[0];
      unsigned char* out = (unsigned char*)output_items[0];

      unsigned last_out = _lastOut;
      unsigned modulus = _modulus;
      for (int i = 0; i < noutput_items; i++) {
          out[i] = (in[i] + last_out) % modulus;
          last_out = out[i];
          procCount++;
         // std::cout<<"Running"<<i<<std::endl;
          if(procCount==_flushLength){
            procCount=0;
            if(toFlush){
              last_out=0;
            //  std::cout<<"Flushed"<<i<<std::endl;
            }
          }
      }
      _lastOut = last_out;
      return noutput_items;
    }

  } /* namespace Custom */
} /* namespace gr */

