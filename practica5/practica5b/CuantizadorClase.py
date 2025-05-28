#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Cuantizador No uniforme UIS
# Author: EFREN
# GNU Radio version: v3.10.11.0-89-ga17f69e7

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
import CuantizadorClase_epy_block_0 as epy_block_0  # embedded python block
import math
import numpy
import sip
import threading



class CuantizadorClase(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Cuantizador No uniforme UIS", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Cuantizador No uniforme UIS")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "CuantizadorClase")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 88200
        self.noise = noise = 0
        self.n = n = 6
        self.fcut = fcut = 16000
        self.amplitude = amplitude = 1
        self.U = U = 32

        ##################################################
        # Blocks
        ##################################################

        self.tab_source = Qt.QTabWidget()
        self.tab_source_widget_0 = Qt.QWidget()
        self.tab_source_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_source_widget_0)
        self.tab_source_grid_layout_0 = Qt.QGridLayout()
        self.tab_source_layout_0.addLayout(self.tab_source_grid_layout_0)
        self.tab_source.addTab(self.tab_source_widget_0, 'Source Controls')
        self.top_grid_layout.addWidget(self.tab_source, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.tab_channel = Qt.QTabWidget()
        self.tab_channel_widget_0 = Qt.QWidget()
        self.tab_channel_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_channel_widget_0)
        self.tab_channel_grid_layout_0 = Qt.QGridLayout()
        self.tab_channel_layout_0.addLayout(self.tab_channel_grid_layout_0)
        self.tab_channel.addTab(self.tab_channel_widget_0, 'Channel Controls')
        self.top_grid_layout.addWidget(self.tab_channel, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.tab_Quantizer = Qt.QTabWidget()
        self.tab_Quantizer_widget_0 = Qt.QWidget()
        self.tab_Quantizer_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_Quantizer_widget_0)
        self.tab_Quantizer_grid_layout_0 = Qt.QGridLayout()
        self.tab_Quantizer_layout_0.addLayout(self.tab_Quantizer_grid_layout_0)
        self.tab_Quantizer.addTab(self.tab_Quantizer_widget_0, 'Quantizer Controls')
        self.top_grid_layout.addWidget(self.tab_Quantizer, 0, 2, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._noise_range = qtgui.Range(0, 0.5, 0.01, 0, 200)
        self._noise_win = qtgui.RangeWidget(self._noise_range, self.set_noise, "Noise voltage", "counter_slider", float, QtCore.Qt.Horizontal)
        self.tab_channel_grid_layout_0.addWidget(self._noise_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.tab_channel_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_channel_grid_layout_0.setColumnStretch(c, 1)
        self._n_range = qtgui.Range(1, 12, 1, 6, 200)
        self._n_win = qtgui.RangeWidget(self._n_range, self.set_n, "# bit", "eng_slider", float, QtCore.Qt.Horizontal)
        self.tab_Quantizer_grid_layout_0.addWidget(self._n_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.tab_Quantizer_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tab_Quantizer_grid_layout_0.setColumnStretch(c, 1)
        self._fcut_range = qtgui.Range(0, 22050, 100, 16000, 200)
        self._fcut_win = qtgui.RangeWidget(self._fcut_range, self.set_fcut, "cutoff frequency", "counter_slider", float, QtCore.Qt.Horizontal)
        self.tab_channel_grid_layout_0.addWidget(self._fcut_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.tab_channel_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_channel_grid_layout_0.setColumnStretch(c, 1)
        self._amplitude_range = qtgui.Range(0, 10, 0.1, 1, 200)
        self._amplitude_win = qtgui.RangeWidget(self._amplitude_range, self.set_amplitude, "Amplitude", "eng_slider", float, QtCore.Qt.Horizontal)
        self.tab_source_grid_layout_0.addWidget(self._amplitude_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.tab_source_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_source_grid_layout_0.setColumnStretch(c, 1)
        self._U_range = qtgui.Range(1, 256, 1, 32, 200)
        self._U_win = qtgui.RangeWidget(self._U_range, self.set_U, "U law Constant", "counter_slider", float, QtCore.Qt.Horizontal)
        self.tab_Quantizer_grid_layout_0.addWidget(self._U_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.tab_Quantizer_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_Quantizer_grid_layout_0.setColumnStretch(c, 1)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
            ",".join(("", '')),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
            "",
        )
        self.uhd_usrp_sink_0.set_samp_rate((int(25e6/64)))
        self.uhd_usrp_sink_0.set_time_now(uhd.time_spec(time.time()), uhd.ALL_MBOARDS)

        self.uhd_usrp_sink_0.set_center_freq(200000000, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_sink_0.set_gain(20, 0)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=(int(25e6/64)),
                decimation=int(samp_rate),
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=int(samp_rate),
                decimation=44100,
                taps=[],
                fractional_bw=0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            20000, #size
            samp_rate, #samp_rate
            "Time", #name
            4, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Source', 'Channel', 'Companding', 'Quantization Noise', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(4):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 3, 2, 4, 2)
        for r in range(3, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_0_0 = qtgui.histogram_sink_f(
            8192,
            10000,
            (-1.1),
            1.1,
            "Histogram Source Vs Companding",
            2,
            None # parent
        )

        self.qtgui_histogram_sink_x_0_0.set_update_time(0.10)
        self.qtgui_histogram_sink_x_0_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0_0.enable_accumulate(True)
        self.qtgui_histogram_sink_x_0_0.enable_grid(True)
        self.qtgui_histogram_sink_x_0_0.enable_axis_labels(True)


        labels = ['Source', 'Companding', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 3, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers= [-1, 2, -1, -1, -1,
            -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_0_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_histogram_sink_x_0_0_win, 9, 0, 2, 2)
        for r in range(9, 11):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_histogram_sink_x_0 = qtgui.histogram_sink_f(
            8192,
            10000,
            (-0.02),
            0.02,
            "Histogram Noise Q",
            1,
            None # parent
        )

        self.qtgui_histogram_sink_x_0.set_update_time(0.10)
        self.qtgui_histogram_sink_x_0.enable_autoscale(True)
        self.qtgui_histogram_sink_x_0.enable_accumulate(True)
        self.qtgui_histogram_sink_x_0.enable_grid(True)
        self.qtgui_histogram_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers= [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_histogram_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_histogram_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_histogram_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_histogram_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_histogram_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_histogram_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_histogram_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_histogram_sink_x_0_win = sip.wrapinstance(self.qtgui_histogram_sink_x_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_histogram_sink_x_0_win, 9, 2, 6, 2)
        for r in range(9, 15):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_f(
            16384, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Frequency", #name
            4,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-100), (-30))
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(0.2)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['Source', 'Channel', 'Companding', 'Quantization Noise', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(4):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 3, 0, 4, 2)
        for r in range(3, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.low_pass_filter_0 = filter.interp_fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                fcut,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.epy_block_0 = epy_block_0.blk(mu=U)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/com1_E1C_G4/GNURADIO_LABCOMUIS_2025_1_E1C_G4/practica5a/bone.wav', True)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_float*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_ff(.250)
        self.blocks_multiply_const_vxx_0_1 = blocks.multiply_const_ff(amplitude)
        self.blocks_multiply_const_vxx_0_0 = blocks.multiply_const_ff((amplitude/math.pow(2,n)))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff((math.pow(2,n)/amplitude))
        self.blocks_float_to_short_0 = blocks.float_to_short(1, 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise, 0)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_float_to_short_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.qtgui_histogram_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_multiply_const_vxx_0_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.qtgui_freq_sink_x_0, 3))
        self.connect((self.blocks_sub_xx_0, 0), (self.qtgui_histogram_sink_x_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_multiply_const_vxx_0_1, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.epy_block_0, 0), (self.qtgui_freq_sink_x_0, 2))
        self.connect((self.epy_block_0, 0), (self.qtgui_histogram_sink_x_0_0, 1))
        self.connect((self.epy_block_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.low_pass_filter_0, 0), (self.epy_block_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_freq_sink_x_0, 1))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.uhd_usrp_sink_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "CuantizadorClase")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.fcut, 1000, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.analog_noise_source_x_0.set_amplitude(self.noise)

    def get_n(self):
        return self.n

    def set_n(self, n):
        self.n = n
        self.blocks_multiply_const_vxx_0.set_k((math.pow(2,self.n)/self.amplitude))
        self.blocks_multiply_const_vxx_0_0.set_k((self.amplitude/math.pow(2,self.n)))

    def get_fcut(self):
        return self.fcut

    def set_fcut(self, fcut):
        self.fcut = fcut
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.fcut, 1000, window.WIN_HAMMING, 6.76))

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude
        self.blocks_multiply_const_vxx_0.set_k((math.pow(2,self.n)/self.amplitude))
        self.blocks_multiply_const_vxx_0_0.set_k((self.amplitude/math.pow(2,self.n)))
        self.blocks_multiply_const_vxx_0_1.set_k(self.amplitude)

    def get_U(self):
        return self.U

    def set_U(self, U):
        self.U = U
        self.epy_block_0.mu = self.U




def main(top_block_cls=CuantizadorClase, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
