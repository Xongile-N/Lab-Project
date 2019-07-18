#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Jul 18 16:52:27 2019
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
from optparse import OptionParser
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
        self.PackRate = PackRate = 8
        self.FrameBits = FrameBits = 2048
        self.scale = scale = 1
        self.samp_rate = samp_rate = 125000000
        self.packetLength = packetLength = 8


        self.encoder = encoder = fec.cc_encoder_make(FrameBits*PackRate, 7, 2, ([79,109]), 0, fec.CC_TERMINATED, True)



        self.decoder = decoder = fec.cc_decoder.make(FrameBits*PackRate, 7, 2, ([79,109]), 0, -1, fec.CC_TERMINATED, True)

        self.UnpackRate = UnpackRate = 8

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0_0_0_0 = qtgui.time_sink_f(
        	10240, #size
        	samp_rate, #samp_rate
        	"Decoder Output and Encoder Input", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_0_0.set_update_time(5)
        self.qtgui_time_sink_x_0_0_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_0_0.enable_tags(-1, False)
        self.qtgui_time_sink_x_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_0_0.disable_legend()

        labels = ["Decoder Out", "Encoder In", '', '', '',
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

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_0_0_win)
        self.fec_extended_tagged_encoder_0 = fec.extended_tagged_encoder(encoder_obj_list=encoder, puncpat='11', lentagname='packet_len', mtu=1500)
        self.fec_extended_tagged_decoder_1 = self.fec_extended_tagged_decoder_1 = fec_extended_tagged_decoder_1 = fec.extended_tagged_decoder(decoder_obj_list=decoder, ann=None, puncpat='11', integration_period=10000, lentagname='packet_len', mtu=1500)
        self.digital_map_bb_0 = digital.map_bb((-1,1))
        self.blocks_unpack_k_bits_bb_0 = blocks.unpack_k_bits_bb(UnpackRate)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, packetLength, "packet_len")
        self.blocks_pack_k_bits_bb_0_0 = blocks.pack_k_bits_bb(8)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((-1, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/xongile/Lab-Project/5MB.jpg', False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/xongile/Lab-Project/TestOutput.dat', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_char_to_float_0_0_1_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0_0_1_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_xx_0 = blocks.add_vff(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0_0_0_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.fec_extended_tagged_decoder_1, 0))
        self.connect((self.blocks_char_to_float_0_0_1_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_char_to_float_0_0_1_0_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_pack_k_bits_bb_0_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_char_to_float_0_0_1_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.fec_extended_tagged_encoder_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_unpack_k_bits_bb_0, 0))
        self.connect((self.blocks_unpack_k_bits_bb_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.digital_map_bb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.fec_extended_tagged_decoder_1, 0), (self.blocks_char_to_float_0_0_1_0_0, 0))
        self.connect((self.fec_extended_tagged_decoder_1, 0), (self.blocks_pack_k_bits_bb_0_0, 0))
        self.connect((self.fec_extended_tagged_encoder_0, 0), (self.digital_map_bb_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_PackRate(self):
        return self.PackRate

    def set_PackRate(self, PackRate):
        self.PackRate = PackRate

    def get_FrameBits(self):
        return self.FrameBits

    def set_FrameBits(self, FrameBits):
        self.FrameBits = FrameBits

    def get_scale(self):
        return self.scale

    def set_scale(self, scale):
        self.scale = scale

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_0_0_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_packetLength(self):
        return self.packetLength

    def set_packetLength(self, packetLength):
        self.packetLength = packetLength
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.packetLength)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.packetLength)

    def get_encoder(self):
        return self.encoder

    def set_encoder(self, encoder):
        self.encoder = encoder

    def get_decoder(self):
        return self.decoder

    def set_decoder(self, decoder):
        self.decoder = decoder

    def get_UnpackRate(self):
        return self.UnpackRate

    def set_UnpackRate(self, UnpackRate):
        self.UnpackRate = UnpackRate


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
