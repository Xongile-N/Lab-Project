#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "DiffDecoderFlush_impl.h"

namespace gr {
  namespace Custom {

    DiffDecoderFlush::sptr
    DiffDecoderFlush::make(int modulus, bool flush, int flushLength)
    {
      return gnuradio::get_initial_sptr
        (new DiffDecoderFlush_impl(modulus, flush, flushLength));
    }

    /*
     * The private constructor
     */
    DiffDecoderFlush_impl::DiffDecoderFlush_impl(int modulus, bool flush, int flushLength)
      : gr::sync_block("DiffDecoderFlush",
              io_signature::make(1, 1, sizeof(unsigned char)),
              io_signature::make(1, 1, sizeof(unsigned char))),
              toFlush(flush),
              _modulus(modulus),
              _flushLength(flushLength),
              procCount(0)
      {
            set_history(2); // need to look at two inputs

      }

    /*
     * Our virtual destructor.
     */
    DiffDecoderFlush_impl::~DiffDecoderFlush_impl()
    {
    }

    int
    DiffDecoderFlush_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const unsigned char* in = (const unsigned char*)input_items[0];
      unsigned char* out = (unsigned char*)output_items[0];
      unsigned char*tempBuffer=new unsigned char[noutput_items];
      int offset=0;
      in += 1; // ensure that in[-1] is valid
      unsigned modulus = _modulus;
      int outCount=noutput_items;
      for (int i = 0; i < noutput_items; i++) {
          unsigned char curr=in[i];
          unsigned char prev=in[i-1];
          if(toFlush&&procCount==_flushLength){
            procCount=0;
            prev=0
          }
          procCount++;
          out[i]=(curr-prev)% modulus;
        }
      return outCount;
    }

  } /* namespace Custom */
} /* namespace gr */

