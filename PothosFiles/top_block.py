#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Aug 13 15:19:36 2019
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
import red_pitaya_wide
import sip
import sys
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
        self.sps = sps = 2
        self.qpsk_1 = qpsk_1 = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1,2,3]), 4, 2, 2, 1, 1).base()
        self.nfilts = nfilts = 32
        self.eb = eb = 0.22

        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 15*sps*nfilts)

        self.samp_rates = samp_rates = [2e4,5e4,1e5,2.5e5,5e5,1.25e6]
        self.samp_index = samp_index = 3
        self.qpsk = qpsk = qpsk_1
        self.taps_per_filt = taps_per_filt = len(tx_rrc_taps)/nfilts
        self.samp_rate_0 = samp_rate_0 = samp_rates[samp_index]
        self.rep = rep = 3
        self.hdr_format_count = hdr_format_count = digital.header_format_counter(digital.packet_utils.default_access_code, 3, qpsk.bits_per_symbol())
        self.taps_gain = taps_gain = 32
        self.taps_count = taps_count = 32*sps
        self.taps_bw = taps_bw = 0.35
        self.sdr = sdr = "redpitaya=10.0.0.100:1001"
        self.samp_rate = samp_rate = samp_rate_0
        self.pathr = pathr = "C:\Users\XongileN\GoogleDrive\2019\Semester2\ELEN40024012_lab_project\Lab-Project\TestSinks"
        self.pathl = pathl = "/home/xongile/Lab-Project/TestSinks/"
        self.packetLength = packetLength = 400
        self.loopBW = loopBW = 62.8e-3
        self.hdr_format_def = hdr_format_def = digital.header_format_default(digital.packet_utils.default_access_code, 0)
        self.hdr_format = hdr_format = hdr_format_count
        self.filt_delay = filt_delay = 1+(taps_per_filt-1)/2
        self.fc = fc = 1e6


        self.enc_hdr = enc_hdr = fec.repetition_encoder_make(8000, rep)


        self.bpsk = bpsk = digital.constellation_bpsk().base()


        ##################################################
        # Blocks
        ##################################################
        self.red_pitaya_wide_sink_0 = red_pitaya_wide.sink(
                addr='192.168.88.18',
                port=1001,
                freq=fc,
                rate=int(samp_rate),
                mask=1,
                corr=0,
                ptt=True
        )

        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"TX", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_rrc_taps),
        	  flt_size=nfilts)
        self.pfb_arb_resampler_xxx_0.declare_sample_delay(filt_delay)

        self._loopBW_range = Range(0, 200e-3, 10e-3, 62.8e-3, 200)
        self._loopBW_win = RangeWidget(self._loopBW_range, self.set_loopBW, "loopBW", "counter_slider", float)
        self.top_layout.addWidget(self._loopBW_win)
        self.fec_tagged_encoder_2 = fec.tagged_encoder(enc_hdr, gr.sizeof_char, gr.sizeof_char, "packet_len", 1500)
        self.fec_tagged_encoder_1 = fec.tagged_encoder( fec.dummy_encoder_make(8000), gr.sizeof_char, gr.sizeof_char, "packet_len", 1500)
        self.digital_protocol_formatter_bb_0 = digital.protocol_formatter_bb(hdr_format, "packet_len")
        self.digital_map_bb_0_0 = digital.map_bb((qpsk.pre_diff_code()))
        self.digital_map_bb_0 = digital.map_bb((qpsk.pre_diff_code()))
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
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.5, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1 , '/home/xongile/Lab-Project/TestSinks/TestData.dat', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.red_pitaya_wide_sink_0, 0))
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_map_bb_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_0, 0), (self.digital_map_bb_0_0, 0))
        self.connect((self.blocks_repack_bits_bb_0_1, 0), (self.blocks_tagged_stream_multiply_length_1_1, 0))
        self.connect((self.blocks_repack_bits_bb_0_1_0, 0), (self.blocks_tagged_stream_multiply_length_1_1_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.fec_tagged_encoder_1, 0))
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
        self.connect((self.digital_map_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.digital_map_bb_0_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))
        self.connect((self.digital_protocol_formatter_bb_0, 0), (self.blocks_repack_bits_bb_0_1, 0))
        self.connect((self.fec_tagged_encoder_1, 0), (self.blocks_repack_bits_bb_0_0, 0))
        self.connect((self.fec_tagged_encoder_1, 0), (self.digital_protocol_formatter_bb_0, 0))
        self.connect((self.fec_tagged_encoder_2, 0), (self.blocks_repack_bits_bb_0_1_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_tagged_stream_multiply_length_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_taps_count(32*self.sps)
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)
        self.blocks_tagged_stream_multiply_length_0.set_scalar(self.sps)

    def get_qpsk_1(self):
        return self.qpsk_1

    def set_qpsk_1(self, qpsk_1):
        self.qpsk_1 = qpsk_1
        self.set_qpsk(self.qpsk_1)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_taps_per_filt(len(self.tx_rrc_taps)/self.nfilts)

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb

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

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk

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

    def get_rep(self):
        return self.rep

    def set_rep(self, rep):
        self.rep = rep

    def get_hdr_format_count(self):
        return self.hdr_format_count

    def set_hdr_format_count(self, hdr_format_count):
        self.hdr_format_count = hdr_format_count
        self.set_hdr_format(self.hdr_format_count)

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
        self.red_pitaya_wide_sink_0.set_rate(int(self.samp_rate))
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_pathr(self):
        return self.pathr

    def set_pathr(self, pathr):
        self.pathr = pathr

    def get_pathl(self):
        return self.pathl

    def set_pathl(self, pathl):
        self.pathl = pathl

    def get_packetLength(self):
        return self.packetLength

    def set_packetLength(self, packetLength):
        self.packetLength = packetLength
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.packetLength)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.packetLength)

    def get_loopBW(self):
        return self.loopBW

    def set_loopBW(self, loopBW):
        self.loopBW = loopBW

    def get_hdr_format_def(self):
        return self.hdr_format_def

    def set_hdr_format_def(self, hdr_format_def):
        self.hdr_format_def = hdr_format_def

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format

    def get_filt_delay(self):
        return self.filt_delay

    def set_filt_delay(self, filt_delay):
        self.filt_delay = filt_delay

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.red_pitaya_wide_sink_0.set_freq(self.fc, 0)

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
