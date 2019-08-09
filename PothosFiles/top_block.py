#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Aug  9 23:38:12 2019
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
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
from packet_rx import packet_rx  # grc-generated hier_block
from packet_tx import packet_tx  # grc-generated hier_block
import numpy
import sip
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
        self.sps = sps = 3
        self.taps_gain = taps_gain = 32
        self.taps_count = taps_count = 32*sps
        self.taps_bw = taps_bw = 0.35
        self.samp_rate = samp_rate = 32000
        self.packetLength = packetLength = 100
        self.nfilts = nfilts = 32
        self.eb = eb = 0.35
        self.HeaderLength = HeaderLength = 16


        self.variable_dummy_encoder_def_0 = variable_dummy_encoder_def_0 = fec.dummy_encoder_make(2048)


        self.tx_rrc_taps = tx_rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0, eb, 5*sps*nfilts)

        self.time_offset = time_offset = 1
        self.taps_0 = taps_0 = firdes.root_raised_cosine(taps_gain,samp_rate,sps,taps_bw,taps_count)

        self.rx_rrc_taps = rx_rrc_taps = firdes.root_raised_cosine(nfilts, sps*nfilts, 1.0, eb, 11*sps*nfilts)


        self.qpsk_0 = qpsk_0 = digital.constellation_qpsk().base()

        self.qpsk = qpsk = digital.constellation_rect(([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j]), ([0, 1,2,3]), 4, 2, 2, 1, 1).base()
        self.noise_volt = noise_volt = 0100e-6
        self.loopBW = loopBW = 62.8e-3
        self.freq_offset = freq_offset = 0
        self.RecdPackLength = RecdPackLength = sps*(4*HeaderLength+4*packetLength+21+(5*sps-1)/2)

        ##################################################
        # Blocks
        ##################################################
        self._time_offset_range = Range(999e-3, 1.001, 100e-6, 1, 200)
        self._time_offset_win = RangeWidget(self._time_offset_range, self.set_time_offset, "time_offset", "counter_slider", float)
        self.top_layout.addWidget(self._time_offset_win)
        self.qtgui_time_sink_x_1_0_0_0_0_2 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"Internal Polyphase", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0_0_0_2.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0_0_0_0_2.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_1_0_0_0_0_2.set_y_label('TX', "")

        self.qtgui_time_sink_x_1_0_0_0_0_2.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0_0_0_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0_0_0_2.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_0_0_0_2.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0_0_0_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0_0_0_2.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0_0_0_2.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0_0_0_0_2.disable_legend()

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
                    self.qtgui_time_sink_x_1_0_0_0_0_2.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_0_0_0_0_2.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_0_0_0_0_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0_0_0_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0_0_0_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0_0_0_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0_0_0_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0_0_0_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_0_0_2_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0_0_0_2.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_0_0_0_2_win)
        self.qtgui_time_sink_x_1_0_0_0_0_1_1 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"Payload", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0_0_0_1_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0_0_0_0_1_1.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_1_0_0_0_0_1_1.set_y_label('TX', "")

        self.qtgui_time_sink_x_1_0_0_0_0_1_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0_0_0_0_1_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0_0_0_1_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1_0_0_0_0_1_1.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0_0_0_1_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0_0_0_1_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0_0_0_1_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0_0_0_0_1_1.disable_legend()

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
                    self.qtgui_time_sink_x_1_0_0_0_0_1_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_0_0_0_0_1_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_0_0_0_0_1_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_0_0_1_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0_0_0_1_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_0_0_0_1_1_win)
        self.qtgui_time_sink_x_1_0_0_0_0_1_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"Header", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0_0_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0_0_0_0_1_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_1_0_0_0_0_1_0.set_y_label('TX', "")

        self.qtgui_time_sink_x_1_0_0_0_0_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0_0_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0_0_0_1_0.enable_autoscale(True)
        self.qtgui_time_sink_x_1_0_0_0_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0_0_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0_0_0_1_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0_0_0_1_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0_0_0_0_1_0.disable_legend()

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
                    self.qtgui_time_sink_x_1_0_0_0_0_1_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_0_0_0_0_1_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_0_0_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_0_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_0_0_0_1_0_win)
        self.qtgui_time_sink_x_1_0_0_0_0_1 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"Internal Correlator", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0_0_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0_0_0_0_1.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_1_0_0_0_0_1.set_y_label('TX', "")

        self.qtgui_time_sink_x_1_0_0_0_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0_0_0_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0_0_0_1.enable_autoscale(True)
        self.qtgui_time_sink_x_1_0_0_0_0_1.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0_0_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0_0_0_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0_0_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0_0_0_0_1.disable_legend()

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
                    self.qtgui_time_sink_x_1_0_0_0_0_1.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_0_0_0_0_1.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_0_0_0_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0_0_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_0_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0_0_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_0_0_0_1_win)
        self.qtgui_time_sink_x_1_0_0_0_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	'TX', #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0_0_0_0_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_1_0_0_0_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_0_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0_0_0_0_0.disable_legend()

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
                    self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_0_0_0_0_win)
        self.qtgui_time_sink_x_1_0_0_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"Internal Polyphase", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0_0_0_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_1_0_0_0_0.set_y_label('TX', "")

        self.qtgui_time_sink_x_1_0_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0_0_0_0.disable_legend()

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
                    self.qtgui_time_sink_x_1_0_0_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_1_0_0_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_1_0_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_0_0_0_win)
        self.qtgui_time_sink_x_1_0_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"Internal Checker1", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_1_0_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_1_0_0_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_1_0_0_0.set_y_label('TX', "")

        self.qtgui_time_sink_x_1_0_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_1_0_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1_0_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_1_0_0_0.enable_grid(False)
        self.qtgui_time_sink_x_1_0_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_0_0_0.enable_control_panel(False)
        self.qtgui_time_sink_x_1_0_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_1_0_0_0.disable_legend()

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

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_0_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_0_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_0_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_0_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_0_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_0_0_0_win)
        self.qtgui_const_sink_x_0_0_2_0 = qtgui.const_sink_c(
        	1024, #size
        	"Internal Costas", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_2_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_2_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_2_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_2_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_2_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_2_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0_2_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_2_0.disable_legend()

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
                self.qtgui_const_sink_x_0_0_2_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_2_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_2_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_2_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_2_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_2_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_2_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_2_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_2_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_2_0_win)
        self.qtgui_const_sink_x_0_0_2 = qtgui.const_sink_c(
        	1024, #size
        	"Internal Polyphase", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0_2.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0_2.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_2.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0_2.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0_2.enable_grid(False)
        self.qtgui_const_sink_x_0_0_2.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0_2.disable_legend()

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
                self.qtgui_const_sink_x_0_0_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0_2.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0_2.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0_2.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0_2.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0_2.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0_2.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_2_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0_2.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_2_win)
        self.packet_tx_0 = packet_tx(
            hdr_const=qpsk,
            hdr_enc= fec.dummy_encoder_make(8000),
            hdr_format=digital.header_format_default(digital.packet_utils.default_access_code, 0),
            pld_const=qpsk,
            pld_enc= fec.dummy_encoder_make(8000),
            psf_taps=tx_rrc_taps,
            sps=sps,
        )
        self.packet_rx_0 = packet_rx(
            eb=eb,
            hdr_const=qpsk,
            hdr_dec= fec.dummy_decoder.make(8000),
            hdr_format=digital.header_format_default(digital.packet_utils.default_access_code, 0),
            pld_const=qpsk,
            pld_dec= fec.dummy_decoder.make(8000),
            psf_taps=taps_0,
            sps=sps,
        )
        self._noise_volt_range = Range(0, 1, 100e-6, 0100e-6, 200)
        self._noise_volt_win = RangeWidget(self._noise_volt_range, self.set_noise_volt, "noise_volt", "counter_slider", float)
        self.top_layout.addWidget(self._noise_volt_win)
        self._loopBW_range = Range(0, 200e-3, 10e-3, 62.8e-3, 200)
        self._loopBW_win = RangeWidget(self._loopBW_range, self.set_loopBW, "loopBW", "counter_slider", float)
        self.top_layout.addWidget(self._loopBW_win)
        self._freq_offset_range = Range(-100e-3, 100e-3, 1e-3, 0, 200)
        self._freq_offset_win = RangeWidget(self._freq_offset_range, self.set_freq_offset, "freq_offset", "counter_slider", float)
        self.top_layout.addWidget(self._freq_offset_win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_char*1, samp_rate,True)
        self.blocks_tagged_stream_to_pdu_0 = blocks.tagged_stream_to_pdu(blocks.byte_t, 'packet_len')
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_gr_complex * 1, False)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, packetLength, 'packet_len')
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.float_t, "payload symbols")
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 100)), True)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_tagged_stream_to_pdu_0, 'pdus'), (self.packet_tx_0, 'in'))
        self.msg_connect((self.packet_rx_0, 'pkt out'), (self.blocks_pdu_to_tagged_stream_0, 'pdus'))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.qtgui_time_sink_x_1_0_0_0, 0))
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.blocks_tagged_stream_to_pdu_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.packet_rx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))
        self.connect((self.packet_rx_0, 3), (self.qtgui_const_sink_x_0_0_2, 0))
        self.connect((self.packet_rx_0, 2), (self.qtgui_const_sink_x_0_0_2_0, 0))
        self.connect((self.packet_rx_0, 3), (self.qtgui_time_sink_x_1_0_0_0_0, 0))
        self.connect((self.packet_rx_0, 4), (self.qtgui_time_sink_x_1_0_0_0_0_1, 0))
        self.connect((self.packet_rx_0, 0), (self.qtgui_time_sink_x_1_0_0_0_0_1_0, 0))
        self.connect((self.packet_rx_0, 1), (self.qtgui_time_sink_x_1_0_0_0_0_1_1, 0))
        self.connect((self.packet_rx_0, 2), (self.qtgui_time_sink_x_1_0_0_0_0_2, 0))
        self.connect((self.packet_tx_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.packet_tx_0, 0), (self.qtgui_time_sink_x_1_0_0_0_0_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_taps_0(firdes.root_raised_cosine(self.taps_gain,self.samp_rate,self.sps,self.taps_bw,self.taps_count))
        self.set_taps_count(32*self.sps)
        self.packet_tx_0.set_sps(self.sps)
        self.packet_rx_0.set_sps(self.sps)
        self.set_RecdPackLength(self.sps*(4*self.HeaderLength+4*self.packetLength+21+(5*self.sps-1)/2))

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
        self.qtgui_time_sink_x_1_0_0_0_0_2.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0_0_0_0_1_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0_0_0_0_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0_0_0_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0_0_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0_0_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1_0_0_0.set_samp_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_packetLength(self):
        return self.packetLength

    def set_packetLength(self, packetLength):
        self.packetLength = packetLength
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.packetLength)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.packetLength)
        self.set_RecdPackLength(self.sps*(4*self.HeaderLength+4*self.packetLength+21+(5*self.sps-1)/2))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts

    def get_eb(self):
        return self.eb

    def set_eb(self, eb):
        self.eb = eb
        self.packet_rx_0.set_eb(self.eb)

    def get_HeaderLength(self):
        return self.HeaderLength

    def set_HeaderLength(self, HeaderLength):
        self.HeaderLength = HeaderLength
        self.set_RecdPackLength(self.sps*(4*self.HeaderLength+4*self.packetLength+21+(5*self.sps-1)/2))

    def get_variable_dummy_encoder_def_0(self):
        return self.variable_dummy_encoder_def_0

    def set_variable_dummy_encoder_def_0(self, variable_dummy_encoder_def_0):
        self.variable_dummy_encoder_def_0 = variable_dummy_encoder_def_0

    def get_tx_rrc_taps(self):
        return self.tx_rrc_taps

    def set_tx_rrc_taps(self, tx_rrc_taps):
        self.tx_rrc_taps = tx_rrc_taps
        self.packet_tx_0.set_psf_taps(self.tx_rrc_taps)

    def get_time_offset(self):
        return self.time_offset

    def set_time_offset(self, time_offset):
        self.time_offset = time_offset

    def get_taps_0(self):
        return self.taps_0

    def set_taps_0(self, taps_0):
        self.taps_0 = taps_0
        self.packet_rx_0.set_psf_taps(self.taps_0)

    def get_rx_rrc_taps(self):
        return self.rx_rrc_taps

    def set_rx_rrc_taps(self, rx_rrc_taps):
        self.rx_rrc_taps = rx_rrc_taps

    def get_qpsk_0(self):
        return self.qpsk_0

    def set_qpsk_0(self, qpsk_0):
        self.qpsk_0 = qpsk_0

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk
        self.packet_tx_0.set_hdr_const(self.qpsk)
        self.packet_tx_0.set_pld_const(self.qpsk)
        self.packet_rx_0.set_hdr_const(self.qpsk)
        self.packet_rx_0.set_pld_const(self.qpsk)

    def get_noise_volt(self):
        return self.noise_volt

    def set_noise_volt(self, noise_volt):
        self.noise_volt = noise_volt

    def get_loopBW(self):
        return self.loopBW

    def set_loopBW(self, loopBW):
        self.loopBW = loopBW

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset

    def get_RecdPackLength(self):
        return self.RecdPackLength

    def set_RecdPackLength(self, RecdPackLength):
        self.RecdPackLength = RecdPackLength


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
