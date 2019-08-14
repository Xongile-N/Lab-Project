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


#ifndef INCLUDED_CUSTOM_CC_ENCODER_CUSTOM_H
#define INCLUDED_CUSTOM_CC_ENCODER_CUSTOM_H

#include <Custom/api.h>
#include <gnuradio/sync_interpolator.h>

namespace gr {
  namespace Custom {

    /*!
     * \brief <+description of block+>
     * \ingroup Custom
     *
     */
    class CUSTOM_API CC_Encoder_Custom : virtual public gr::sync_interpolator
    {
     public:
      typedef boost::shared_ptr<CC_Encoder_Custom> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of Custom::CC_Encoder_Custom.
       *
       * To avoid accidental use of raw pointers, Custom::CC_Encoder_Custom's
       * constructor is in a private implementation
       * class. Custom::CC_Encoder_Custom::make is the public interface for
       * creating new instances.
       */
      static sptr make(int constraint, int frameLength, std::vector<int> polynomial);
    };

  } // namespace Custom
} // namespace gr

#endif /* INCLUDED_CUSTOM_CC_ENCODER_CUSTOM_H */

