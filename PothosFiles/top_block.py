#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Aug 11 11:55:57 2019
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

from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from packet_tx import packet_tx  # grc-generated hier_block
import numpy
import osmosdr
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
        self.sps = sps = 4
        self.qpsk = qpsk = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1,2,3]), 4, 2, 2, 1, 1).base()
        self.taps_gain = taps_gain = 32
        self.taps_count = taps_count = 32*sps
        self.taps_bw = taps_bw = 0.35
        self.samp_rate = samp_rate = 5e5
        self.rep = rep = 3
        self.nfilts = nfilts = 32
        self.hdr_format = hdr_format = digital.header_format_counter(digital.packet_utils.default_access_code, 3, qpsk.bits_per_symbol())
        self.eb = eb = 0.220


        self.variable_dummy_encoder_def_0 = variable_dummy_encoder_def_0 = fec.dummy_encoder_make(2048)


        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 5*sps*nfilts)

        self.taps_0 = taps_0 = firdes.root_raised_cosine(taps_gain,samp_rate,sps,taps_bw,taps_count)
        self.sdr = sdr = "redpitaya=192.168.88.17:1001"
        self.scaleRX = scaleRX = 400
        self.scale = scale = 0.5

        self.rx_rrc_taps = rx_rrc_taps = firdes.root_raised_cosine(nfilts, sps*nfilts, 1.0, eb, 11*sps*nfilts)


        self.qpsk_0 = qpsk_0 = digital.constellation_qpsk().base()

        self.packetLength = packetLength = 50
        self.fc = fc = 1e6


        self.enc_hdr = enc_hdr = fec.repetition_encoder_make(8000, rep)



        self.dec_hdr = dec_hdr = fec.repetition_decoder.make(hdr_format.header_nbits(), rep, 0.5)

        self.addr = addr = "192.168.88.17"

        ##################################################
        # Blocks
        ##################################################
        self.packet_tx_0 = packet_tx(
            hdr_const=qpsk,
            hdr_enc=enc_hdr,
            hdr_format=hdr_format,
            pld_const=qpsk,
            pld_enc= fec.dummy_encoder_make(8000),
            psf_taps=tx_rrc_taps,
            sps=sps,
        )
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + sdr )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(fc, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(10, 0)
        self.osmosdr_sink_0.set_if_gain(20, 0)
        self.osmosdr_sink_0.set_bb_gain(20, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.byte_t, 'packet_len')
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, packetLength, 'packet_len')
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((scale, ))
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 100)), True)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.packet_tx_0, 'in'))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_tagged_stream_to_pdu_0, 0))
        self.connect((self.packet_tx_0, 0), (self.blocks_multiply_const_vxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_taps_count(32*self.sps)
        self.set_taps_0(firdes.root_raised_cosine(self.taps_gain,self.samp_rate,self.sps,self.taps_bw,self.taps_count))
        self.packet_tx_0.set_sps(self.sps)

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk
        self.packet_tx_0.set_hdr_const(self.qpsk)
        self.packet_tx_0.set_pld_const(self.qpsk)

    def get_taps_gain(self):
        return self.taps_gain

    def set_taps_gain(self, taps_gain):
        self.taps_gain = taps_gain
        self.set_taps_0(firdes.root_raised_cosine(self.taps_gain,self.samp_rate,self.sps,self.taps_bw,self.taps_count))

    def get_taps_count(self):
        return self.taps_count

    def set_taps_count(self, taps_count):
        self.taps_count = taps_count
        self.set_taps_0(firdes.root_raised_cosine(self.taps_gain,self.samp_rate,self.sps,self.taps_bw,self.taps_count))

    def get_taps_bw(self):
        return self.taps_bw

    def set_taps_bw(self, taps_bw):
        self.taps_bw = taps_bw
        self.set_taps_0(firdes.root_raised_cosine(self.taps_gain,self.samp_rate,self.sps,self.taps_bw,self.taps_count))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_taps_0(firdes.root_raised_cosine(self.taps_gain,self.samp_rate,self.sps,self.taps_bw,self.taps_count))
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_rep(self):
        return self.rep

    def set_rep(self, rep):
        self.rep = rep

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts

    def get_hdr_format(self):
        return self.hdr_format

    def set_hdr_format(self, hdr_format):
        self.hdr_format = hdr_format
        self.packet_tx_0.set_hdr_format(self.hdr_format)

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb

    def get_variable_dummy_encoder_def_0(self):
        return self.variable_dummy_encoder_def_0

    def set_variable_dummy_encoder_def_0(self, variable_dummy_encoder_def_0):
        self.variable_dummy_encoder_def_0 = variable_dummy_encoder_def_0

    def get_tx_rrc_taps(self):
        return self.tx_rrc_taps

    def set_tx_rrc_taps(self, tx_rrc_taps):
        self.tx_rrc_taps = tx_rrc_taps
        self.packet_tx_0.set_psf_taps(self.tx_rrc_taps)

    def get_taps_0(self):
        return self.taps_0

    def set_taps_0(self, taps_0):
        self.taps_0 = taps_0

    def get_sdr(self):
        return self.sdr

    def set_sdr(self, sdr):
        self.sdr = sdr

    def get_scaleRX(self):
        return self.scaleRX

    def set_scaleRX(self, scaleRX):
        self.scaleRX = scaleRX

    def get_scale(self):
        return self.scale

    def set_scale(self, scale):
        self.scale = scale
        self.blocks_multiply_const_vxx_0.set_k((self.scale, ))

    def get_rx_rrc_taps(self):
        return self.rx_rrc_taps

    def set_rx_rrc_taps(self, rx_rrc_taps):
        self.rx_rrc_taps = rx_rrc_taps

    def get_qpsk_0(self):
        return self.qpsk_0

    def set_qpsk_0(self, qpsk_0):
        self.qpsk_0 = qpsk_0

    def get_packetLength(self):
        return self.packetLength

    def set_packetLength(self, packetLength):
        self.packetLength = packetLength
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.packetLength)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.packetLength)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.osmosdr_sink_0.set_center_freq(self.fc, 0)

    def get_enc_hdr(self):
        return self.enc_hdr

    def set_enc_hdr(self, enc_hdr):
        self.enc_hdr = enc_hdr
        self.packet_tx_0.set_hdr_enc(self.enc_hdr)

    def get_dec_hdr(self):
        return self.dec_hdr

    def set_dec_hdr(self, dec_hdr):
        self.dec_hdr = dec_hdr

    def get_addr(self):
        return self.addr

    def set_addr(self, addr):
        self.addr = addr


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
