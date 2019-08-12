#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Aug 12 19:26:49 2019
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from packet_rx import packet_rx  # grc-generated hier_block
import numpy
import osmosdr
import sip
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################

        self.dqpsk = dqpsk = digital.constellation_dqpsk().base()

        self.qpsk = qpsk = dqpsk
        self.hdr_format_count = hdr_format_count = digital.header_format_counter(digital.packet_utils.default_access_code, 3, qpsk.bits_per_symbol())
        self.sps = sps = 4
        self.rep = rep = 3
        self.preamble_rep = preamble_rep = [0xe3, 0x8f, 0xc0, 0xfc, 0x7f, 0xc7, 0xe3, 0x81, 0xc0, 0xff, 0x80, 0x38, 0xff, 0xf0, 0x38, 0xe0, 0x0f, 0xc0, 0x03, 0x80, 0x00, 0xff, 0xff, 0xc0]
        self.preamble_dummy = preamble_dummy = [0xac, 0xdd, 0xa4, 0xe2, 0xf2, 0x8c, 0x20, 0xfc]
        self.nfilts = nfilts = 32
        self.hdr_format = hdr_format = hdr_format_count
        self.eb = eb = 0.22

        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 15*sps*nfilts)

        self.samp_rates = samp_rates = [2e4,5e4,1e5,2.5e5,5e5,1.25e6]
        self.samp_index = samp_index = 5
        self.preamble_select = preamble_select = {1: preamble_dummy, 3: preamble_rep}


        self.dec_hdr = dec_hdr = fec.repetition_decoder.make(hdr_format.header_nbits(), rep, 0.5)

        self.taps_per_filt = taps_per_filt = len(tx_rrc_taps)/nfilts
        self.samp_rate_0 = samp_rate_0 = samp_rates[samp_index]
        self.rxmod = rxmod = digital.generic_mod(qpsk, False, sps, True, eb, False, False)
        self.preamble = preamble = preamble_select[int(1.0/dec_hdr.rate())]
        self.mark_delays = mark_delays = [0, 0, 34, 56, 87, 119]
        self.variable_constellation_rect_0 = variable_constellation_rect_0 = digital.constellation_rect(([-1-1j, -1+1j, 1+1j, 1-1j]), ([0, 1, 3, 2]), 4, 2, 2, 1, 1).base()
        self.time_offset = time_offset = 1
        self.taps_gain = taps_gain = 32
        self.taps_count = taps_count = 32*sps
        self.taps_bw = taps_bw = 0.35
        self.sdr = sdr = "redpitaya=192.168.88.18:1001"
        self.samp_rate = samp_rate = samp_rate_0

        self.rx_rrc_taps = rx_rrc_taps = firdes.root_raised_cosine(nfilts, sps*nfilts, 1.0, eb, 11*sps*nfilts)

        self.qpsk_1 = qpsk_1 = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1,2,3]), 4, 2, 2, 1, 1).base()
        self.packetLength = packetLength = 200
        self.noise_volt = noise_volt = 0100e-6
        self.modulated_sync_word = modulated_sync_word = digital.modulate_vector_bc(rxmod .to_basic_block(), (preamble), ([1]))
        self.mark_delay = mark_delay = mark_delays[sps]
        self.loopBW = loopBW = 62.8e-3
        self.hdr_format_def = hdr_format_def = digital.header_format_default(digital.packet_utils.default_access_code, 0)
        self.freq_offset = freq_offset = 0
        self.filt_delay = filt_delay = 1+(taps_per_filt-1)/2
        self.fc = fc = 20e6


        self.enc_hdr = enc_hdr = fec.repetition_encoder_make(8000, rep)


        self.bpsk = bpsk = digital.constellation_bpsk().base()


        ##################################################
        # Blocks
        ##################################################
        self._time_offset_range = Range(999e-3, 1.001, 100e-6, 1, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, "time_offset", "counter_slider", float)
        self.top_layout.addWidget(self._time_offset_win)
        self.qtgui_time_sink_x_0_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"RXRP", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_rrc_taps),
        	  flt_size=nfilts)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(filt_delay)

        self.packet_rx_0 = packet_rx(
            eb=eb,
            hdr_const=qpsk,
            hdr_dec=dec_hdr,
            hdr_format=hdr_format,
            pld_const=qpsk,
            pld_dec= fec.dummy_decoder.make(8000),
            psf_taps=rx_rrc_taps,
            sps=sps,
        )
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + sdr )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(fc, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(0, 0)
        self.osmosdr_source_0.set_iq_balance_mode(1, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(10, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + sdr )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(fc, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self._noise_volt_range = Range(0, 1, 100e-6, 0100e-6, 200)
        self._noise_volt_win = RangeWidget(self._noise_volt_range, self.set_noise_volt, "noise_volt", "counter_slider", float)
        self.top_layout.addWidget(self._noise_volt_win)
        self._loopBW_range = Range(0, 200e-3, 10e-3, 62.8e-3, 200)
        self._loopBW_win = RangeWidget(self._loopBW_range, self.set_loopBW, "loopBW", "counter_slider", float)
        self.top_layout.addWidget(self._loopBW_win)
        self._freq_offset_range = Range(-100e-3, 100e-3, 1e-3, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, "freq_offset", "counter_slider", float)
        self.top_layout.addWidget(self._freq_offset_win)
        self.fec_tagged_encoder_2 = fec.tagged_encoder(enc_hdr, gr.sizeof_char, gr.sizeof_char, "packet_len", 1500)
        self.fec_tagged_encoder_1 = fec.tagged_encoder( fec.dummy_encoder_make(8000), gr.sizeof_char, gr.sizeof_char, "packet_len", 1500)
        self.fec_generic_decoder_0_0 = fec.decoder(dec_hdr, gr.sizeof_float, gr.sizeof_char)
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(hdr_format, "packet_len")
        self.digital_map_bb_0_0 = digital.map_bb((qpsk.pre_diff_code()))
        self.digital_map_bb_0 = digital.map_bb((qpsk.pre_diff_code()))
        self.digital_fll_band_edge_cc_0_0 = digital.fll_band_edge_cc(sps, eb, 44, 0.05)
        self.digital_crc32_bb_0 = digital.crc32_bb(False, "packet_len", True)
        self.digital_costas_loop_cc_0_0_1 = digital.costas_loop_cc(6.28/200.0, qpsk.arity(), False)
        self.digital_constellation_soft_decoder_cf_0_0_0 = digital.constellation_soft_decoder_cf(qpsk)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((qpsk.points()), 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((qpsk.points()), 1)
        self.digital_burst_shaper_xx_0 = digital.burst_shaper_cc((firdes.window(firdes.WIN_HANN, 20, 0)), 0, filt_delay, True, "packet_len")
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_gr_complex*1, "packet_len", 0)
        self.blocks_tagged_stream_multiply_length_1_1_0 = blocks.tagged_stream_multiply_length(gr.sizeof_char*1, 'packet_len', 0.125)
        self.blocks_tagged_stream_multiply_length_1_1 = blocks.tagged_stream_multiply_length(gr.sizeof_char*1, 'packet_len', 8)
        self.blocks_tagged_stream_multiply_length_1_0 = blocks.tagged_stream_multiply_length(gr.sizeof_gr_complex*1, 'packet_len', 8/qpsk.bits_per_symbol())
        self.blocks_tagged_stream_multiply_length_1 = blocks.tagged_stream_multiply_length(gr.sizeof_gr_complex*1, 'packet_len', 8/qpsk.bits_per_symbol())
        self.blocks_tagged_stream_multiply_length_0 = blocks.tagged_stream_multiply_length(gr.sizeof_gr_complex*1, "packet_len", sps)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, packetLength, "packet_len")
        self.blocks_repack_bits_bb_0_1_0 = blocks.repack_bits_bb(1, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_1 = blocks.repack_bits_bb(8, 1, "", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0_0 = blocks.repack_bits_bb(8, qpsk.bits_per_symbol(), "", False, gr.GR_MSB_FIRST)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, qpsk.bits_per_symbol(), "", False, gr.GR_MSB_FIRST)
        self.blocks_pdu_to_tagged_stream_0_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'packet_len')
        self.blocks_pack_k_bits_bb_1_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_const_vxx_0_1_0_0 = blocks.multiply_const_vcc((2, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.5, ))
        self.blocks_message_debug_2 = blocks.message_debug()
        self.blocks_file_sink_1_0_0_0_1_0_1 = blocks.file_sink(gr.sizeof_char*1, '/home/xongile/Lab-Project/TestSinks/QPSKRandSyncWHeaders.dat', False)
        self.blocks_file_sink_1_0_0_0_1_0_1.set_unbuffered(False)
        self.blocks_file_sink_1_0_0_0_1 = blocks.file_sink(gr.sizeof_char*1, '/home/xongile/Lab-Project/TestSinks/QPSKRandSyncW.dat', False)
        self.blocks_file_sink_1_0_0_0_1.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/xongile/Lab-Project/TestSinks/OrigRand.dat', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 255, 200)), True)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.packet_rx_0, 'pkt out'), (self.blocks_message_debug_2, 'print_pdu'))
        self.msg_connect((self.packet_rx_0, 'pkt out'), (self.blocks_pdu_to_tagged_stream_0_0, 'pdus'))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_multiply_const_vxx_0_1_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1_0_0, 0), (self.packet_rx_0, 0))
        self.connect((self.blocks_pack_k_bits_bb_1_0, 0), (self.blocks_file_sink_1_0_0_0_1_0_1, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0, 0), (self.blocks_file_sink_1_0_0_0_1, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_1, 0), (self.blocks_tagged_stream_multiply_length_1_1, 0))
        self.connect((self.blocks_repack_bits_bb_0_1_0, 0), (self.blocks_tagged_stream_multiply_length_1_1_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_crc32_bb_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_1, 0), (self.blocks_tagged_stream_mux_0, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_1_0, 0), (self.blocks_tagged_stream_mux_0, 1))
        self.connect((self.blocks_tagged_stream_multiply_length_1_1, 0), (self.fec_tagged_encoder_2, 0))
        self.connect((self.blocks_tagged_stream_multiply_length_1_1_0, 0), (self.blocks_repack_bits_bb_0, 0))
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_burst_shaper_xx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.digital_burst_shaper_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_tagged_stream_multiply_length_1, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_tagged_stream_multiply_length_1_0, 0))
        self.connect((self.digital_constellation_soft_decoder_cf_0_0_0, 0), (self.fec_generic_decoder_0_0, 0))
        self.connect((self.digital_costas_loop_cc_0_0_1, 0), (self.digital_constellation_soft_decoder_cf_0_0_0, 0))
        self.connect((self.digital_crc32_bb_0, 0), (self.fec_tagged_encoder_1, 0))
        self.connect((self.digital_fll_band_edge_cc_0_0, 0), (self.qtgui_time_sink_x_0_0_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_repack_bits_bb_0_1, 0))
        self.connect((self.fec_generic_decoder_0_0, 0), (self.blocks_pack_k_bits_bb_1_0, 0))
        self.connect((self.fec_tagged_encoder_1, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.fec_tagged_encoder_1, 0), (self.digital_protocol_formatter_bb_0, 0))
        self.connect((self.fec_tagged_encoder_2, 0), (self.blocks_repack_bits_bb_0_1_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.digital_fll_band_edge_cc_0_0, 0))
        self.connect((self.packet_rx_0, 0), (self.digital_costas_loop_cc_0_0_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_tagged_stream_multiply_length_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_dqpsk(self):
        return self.dqpsk

    def set_dqpsk(self, dqpsk):
        self.dqpsk = dqpsk
        self.set_qpsk(self.dqpsk)

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk
        self.set_rxmod(digital.generic_mod(self.qpsk, False, self.sps, True, self.eb, False, False))
        self.packet_rx_0.set_hdr_const(self.qpsk)
        self.packet_rx_0.set_pld_const(self.qpsk)

    def get_hdr_format_count(self):
        return self.hdr_format_count

    def set_hdr_format_count(self, hdr_format_count):
        self.hdr_format_count = hdr_format_count
        self.set_hdr_format(self.hdr_format_count)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_taps_count(32*self.sps)
        self.set_rxmod(digital.generic_mod(self.qpsk, False, self.sps, True, self.eb, False, False))
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)
        self.packet_rx_0.set_sps(self.sps)
        self.set_mark_delay(self.mark_delays[self.sps])
        self.blocks_tagged_stream_multiply_length_0.set_scalar(self.sps)

    def get_rep(self):
        return self.rep

    def set_rep(self, rep):
        self.rep = rep

    def get_preamble_rep(self):
        return self.preamble_rep

    def set_preamble_rep(self, preamble_rep):
        self.preamble_rep = preamble_rep
        self.set_preamble_select({1: self.preamble_dummy, 3: self.preamble_rep})

    def get_preamble_dummy(self):
        return self.preamble_dummy

    def set_preamble_dummy(self, preamble_dummy):
        self.preamble_dummy = preamble_dummy
        self.set_preamble_select({1: self.preamble_dummy, 3: self.preamble_rep})

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_taps_per_filt(len(self.tx_rrc_taps)/self.nfilts)

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format
        self.packet_rx_0.set_hdr_format(self.hdr_format)

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.set_rxmod(digital.generic_mod(self.qpsk, False, self.sps, True, self.eb, False, False))
        self.packet_rx_0.set_eb(self.eb)

    def get_tx_rrc_taps(self):
        return self.tx_rrc_taps

    def set_tx_rrc_taps(self, tx_rrc_taps):
        self.tx_rrc_taps = tx_rrc_taps
        self.set_taps_per_filt(len(self.tx_rrc_taps)/self.nfilts)
        self.pfb_arb_resampler_xxx_0.set_taps((self.tx_rrc_taps))

    def get_samp_rates(self):
        return self.samp_rates

    def set_samp_rates(self, samp_rates):
        self.samp_rates = samp_rates
        self.set_samp_rate_0(self.samp_rates[self.samp_index])

    def get_samp_index(self):
        return self.samp_index

    def set_samp_index(self, samp_index):
        self.samp_index = samp_index
        self.set_samp_rate_0(self.samp_rates[self.samp_index])

    def get_preamble_select(self):
        return self.preamble_select

    def set_preamble_select(self, preamble_select):
        self.preamble_select = preamble_select
        self.set_preamble(self.preamble_select[int(1.0/dec_hdr.rate())])

    def get_dec_hdr(self):
        return self.dec_hdr

    def set_dec_hdr(self, dec_hdr):
        self.dec_hdr = dec_hdr
        self.packet_rx_0.set_hdr_dec(self.dec_hdr)

    def get_taps_per_filt(self):
        return self.taps_per_filt

    def set_taps_per_filt(self, taps_per_filt):
        self.taps_per_filt = taps_per_filt
        self.set_filt_delay(1+(self.taps_per_filt-1)/2)

    def get_samp_rate_0(self):
        return self.samp_rate_0

    def set_samp_rate_0(self, samp_rate_0):
        self.samp_rate_0 = samp_rate_0
        self.set_samp_rate(self.samp_rate_0)

    def get_rxmod(self):
        return self.rxmod

    def set_rxmod(self, rxmod):
        self.rxmod = rxmod

    def get_preamble(self):
        return self.preamble

    def set_preamble(self, preamble):
        self.preamble = preamble

    def get_mark_delays(self):
        return self.mark_delays

    def set_mark_delays(self, mark_delays):
        self.mark_delays = mark_delays
        self.set_mark_delay(self.mark_delays[self.sps])

    def get_variable_constellation_rect_0(self):
        return self.variable_constellation_rect_0

    def set_variable_constellation_rect_0(self, variable_constellation_rect_0):
        self.variable_constellation_rect_0 = variable_constellation_rect_0

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset

    def get_taps_gain(self):
        return self.taps_gain

    def set_taps_gain(self, taps_gain):
        self.taps_gain = taps_gain

    def get_taps_count(self):
        return self.taps_count

    def set_taps_count(self, taps_count):
        self.taps_count = taps_count

    def get_taps_bw(self):
        return self.taps_bw

    def set_taps_bw(self, taps_bw):
        self.taps_bw = taps_bw

    def get_sdr(self):
        return self.sdr

    def set_sdr(self, sdr):
        self.sdr = sdr

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_0_0.set_samp_rate(self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_rx_rrc_taps(self):
        return self.rx_rrc_taps

    def set_rx_rrc_taps(self, rx_rrc_taps):
        self.rx_rrc_taps = rx_rrc_taps
        self.packet_rx_0.set_psf_taps(self.rx_rrc_taps)

    def get_qpsk_1(self):
        return self.qpsk_1

    def set_qpsk_1(self, qpsk_1):
        self.qpsk_1 = qpsk_1

    def get_packetLength(self):
        return self.packetLength

    def set_packetLength(self, packetLength):
        self.packetLength = packetLength
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.packetLength)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.packetLength)

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt

    def get_modulated_sync_word(self):
        return self.modulated_sync_word

    def set_modulated_sync_word(self, modulated_sync_word):
        self.modulated_sync_word = modulated_sync_word

    def get_mark_delay(self):
        return self.mark_delay

    def set_mark_delay(self, mark_delay):
        self.mark_delay = mark_delay

    def get_loopBW(self):
        return self.loopBW

    def set_loopBW(self, loopBW):
        self.loopBW = loopBW

    def get_hdr_format_def(self):
        return self.hdr_format_def

    def set_hdr_format_def(self, hdr_format_def):
        self.hdr_format_def = hdr_format_def

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset

    def get_filt_delay(self):
        return self.filt_delay

    def set_filt_delay(self, filt_delay):
        self.filt_delay = filt_delay

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.osmosdr_source_0.set_center_freq(self.fc, 0)
        self.osmosdr_sink_0.set_center_freq(self.fc, 0)

    def get_enc_hdr(self):
        return self.enc_hdr

    def set_enc_hdr(self, enc_hdr):
        self.enc_hdr = enc_hdr

    def get_bpsk(self):
        return self.bpsk

    def set_bpsk(self, bpsk):
        self.bpsk = bpsk


def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
