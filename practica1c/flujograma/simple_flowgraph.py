#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Simple flowgraph to test GNU Radio
# Author: Oscar Reyes / Efrén Acevedo
# GNU Radio version: v3.10.11.0-89-ga17f69e7

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from PyQt5.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import numpy as np
import sip
import threading



class simple_flowgraph(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Simple flowgraph to test GNU Radio", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Simple flowgraph to test GNU Radio")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "simple_flowgraph")

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
        self.waveform = waveform = 102
        self.source_type = source_type = 1
        self.samp_rate = samp_rate = 20e3
        self.phase = phase = 0
        self.offset = offset = 0
        self.noise = noise = 0
        self.frequency = frequency = 1e3
        self.fc = fc = 100
        self.amplitude = amplitude = 1
        self.GTX = GTX = 30

        ##################################################
        # Blocks
        ##################################################

        self.tab_usrp = Qt.QTabWidget()
        self.tab_usrp_widget_0 = Qt.QWidget()
        self.tab_usrp_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_usrp_widget_0)
        self.tab_usrp_grid_layout_0 = Qt.QGridLayout()
        self.tab_usrp_layout_0.addLayout(self.tab_usrp_grid_layout_0)
        self.tab_usrp.addTab(self.tab_usrp_widget_0, 'USRP Controls')
        self.top_grid_layout.addWidget(self.tab_usrp, 0, 3, 3, 1)
        for r in range(0, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.tab_source = Qt.QTabWidget()
        self.tab_source_widget_0 = Qt.QWidget()
        self.tab_source_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_source_widget_0)
        self.tab_source_grid_layout_0 = Qt.QGridLayout()
        self.tab_source_layout_0.addLayout(self.tab_source_grid_layout_0)
        self.tab_source.addTab(self.tab_source_widget_0, 'Source Controls')
        self.top_grid_layout.addWidget(self.tab_source, 0, 0, 3, 2)
        for r in range(0, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.tab_channel = Qt.QTabWidget()
        self.tab_channel_widget_0 = Qt.QWidget()
        self.tab_channel_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tab_channel_widget_0)
        self.tab_channel_grid_layout_0 = Qt.QGridLayout()
        self.tab_channel_layout_0.addLayout(self.tab_channel_grid_layout_0)
        self.tab_channel.addTab(self.tab_channel_widget_0, 'Channel Controls')
        self.top_grid_layout.addWidget(self.tab_channel, 0, 2, 3, 1)
        for r in range(0, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 3):
            self.top_grid_layout.setColumnStretch(c, 1)
        # Create the options list
        self._waveform_options = [100, 101, 102, 103, 104, 105]
        # Create the labels list
        self._waveform_labels = ['Constant', 'Sine', 'Cosine', 'Square', 'Triangle', 'Saw Tooth']
        # Create the combo box
        self._waveform_tool_bar = Qt.QToolBar(self)
        self._waveform_tool_bar.addWidget(Qt.QLabel("Waveform" + ": "))
        self._waveform_combo_box = Qt.QComboBox()
        self._waveform_tool_bar.addWidget(self._waveform_combo_box)
        for _label in self._waveform_labels: self._waveform_combo_box.addItem(_label)
        self._waveform_callback = lambda i: Qt.QMetaObject.invokeMethod(self._waveform_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._waveform_options.index(i)))
        self._waveform_callback(self.waveform)
        self._waveform_combo_box.currentIndexChanged.connect(
            lambda i: self.set_waveform(self._waveform_options[i]))
        # Create the radio buttons
        self.tab_source_grid_layout_0.addWidget(self._waveform_tool_bar, 0, 1, 1, 1)
        for r in range(0, 1):
            self.tab_source_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tab_source_grid_layout_0.setColumnStretch(c, 1)
        # Create the options list
        self._source_type_options = [0, 1]
        # Create the labels list
        self._source_type_labels = ['Complex', 'Float']
        # Create the combo box
        self._source_type_tool_bar = Qt.QToolBar(self)
        self._source_type_tool_bar.addWidget(Qt.QLabel("Source Type" + ": "))
        self._source_type_combo_box = Qt.QComboBox()
        self._source_type_tool_bar.addWidget(self._source_type_combo_box)
        for _label in self._source_type_labels: self._source_type_combo_box.addItem(_label)
        self._source_type_callback = lambda i: Qt.QMetaObject.invokeMethod(self._source_type_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._source_type_options.index(i)))
        self._source_type_callback(self.source_type)
        self._source_type_combo_box.currentIndexChanged.connect(
            lambda i: self.set_source_type(self._source_type_options[i]))
        # Create the radio buttons
        self.tab_source_grid_layout_0.addWidget(self._source_type_tool_bar, 0, 0, 1, 1)
        for r in range(0, 1):
            self.tab_source_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_source_grid_layout_0.setColumnStretch(c, 1)
        self._phase_range = qtgui.Range(0, 2*np.pi, 0.1, 0, 200)
        self._phase_win = qtgui.RangeWidget(self._phase_range, self.set_phase, "Phase Rad", "counter_slider", float, QtCore.Qt.Horizontal)
        self.tab_source_grid_layout_0.addWidget(self._phase_win, 2, 1, 1, 1)
        for r in range(2, 3):
            self.tab_source_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tab_source_grid_layout_0.setColumnStretch(c, 1)
        self._offset_range = qtgui.Range(-5, 5, 0.1, 0, 200)
        self._offset_win = qtgui.RangeWidget(self._offset_range, self.set_offset, "Offset", "counter_slider", float, QtCore.Qt.Horizontal)
        self.tab_source_grid_layout_0.addWidget(self._offset_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.tab_source_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tab_source_grid_layout_0.setColumnStretch(c, 1)
        self._noise_range = qtgui.Range(0, 5, 0.01, 0, 200)
        self._noise_win = qtgui.RangeWidget(self._noise_range, self.set_noise, "Noise voltage", "counter_slider", float, QtCore.Qt.Horizontal)
        self.tab_channel_grid_layout_0.addWidget(self._noise_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.tab_channel_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_channel_grid_layout_0.setColumnStretch(c, 1)
        self._frequency_range = qtgui.Range(0, 1e4, 100, 1e3, 200)
        self._frequency_win = qtgui.RangeWidget(self._frequency_range, self.set_frequency, "Frequency in Hz", "counter_slider", float, QtCore.Qt.Horizontal)
        self.tab_source_grid_layout_0.addWidget(self._frequency_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.tab_source_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_source_grid_layout_0.setColumnStretch(c, 1)
        self._fc_range = qtgui.Range(50, 2200, 0.1, 100, 200)
        self._fc_win = qtgui.RangeWidget(self._fc_range, self.set_fc, "Carrier Frequency in MHz", "counter_slider", float, QtCore.Qt.Horizontal)
        self.tab_usrp_grid_layout_0.addWidget(self._fc_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.tab_usrp_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_usrp_grid_layout_0.setColumnStretch(c, 1)
        self._amplitude_range = qtgui.Range(0, 5, 0.1, 1, 200)
        self._amplitude_win = qtgui.RangeWidget(self._amplitude_range, self.set_amplitude, "Amplitude", "counter_slider", float, QtCore.Qt.Horizontal)
        self.tab_source_grid_layout_0.addWidget(self._amplitude_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.tab_source_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_source_grid_layout_0.setColumnStretch(c, 1)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            1, #number of inputs
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


        labels = ['Real', 'Imag', 'Signal 3', 'Signal 4', 'Signal 5',
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


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win, 3, 0, 6, 2)
        for r in range(3, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_RECTANGULAR, #wintype
            0, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(True)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 3, 2, 6, 2)
        for r in range(3, 9):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(2, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.channels_channel_model_0 = channels.channel_model(
            noise_voltage=noise,
            frequency_offset=0,
            epsilon=1.0,
            taps=[1.0],
            noise_seed=0,
            block_tags=False)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_gr_complex*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_selector_0 = blocks.selector(gr.sizeof_gr_complex*1,source_type,0)
        self.blocks_selector_0.set_enabled(True)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, waveform, frequency, amplitude, offset, phase)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, waveform, frequency, amplitude, offset, phase)
        self._GTX_range = qtgui.Range(0, 30, 1, 30, 200)
        self._GTX_win = qtgui.RangeWidget(self._GTX_range, self.set_GTX, "Tx gain in dB", "counter_slider", float, QtCore.Qt.Horizontal)
        self.tab_usrp_grid_layout_0.addWidget(self._GTX_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.tab_usrp_grid_layout_0.setRowStretch(r, 1)
        for c in range(0, 1):
            self.tab_usrp_grid_layout_0.setColumnStretch(c, 1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_selector_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_selector_0, 1))
        self.connect((self.blocks_selector_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.blocks_throttle2_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "simple_flowgraph")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_waveform(self):
        return self.waveform

    def set_waveform(self, waveform):
        self.waveform = waveform
        self._waveform_callback(self.waveform)
        self.analog_sig_source_x_0.set_waveform(self.waveform)
        self.analog_sig_source_x_0_0.set_waveform(self.waveform)

    def get_source_type(self):
        return self.source_type

    def set_source_type(self, source_type):
        self.source_type = source_type
        self._source_type_callback(self.source_type)
        self.blocks_selector_0.set_input_index(self.source_type)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        self.phase = phase
        self.analog_sig_source_x_0.set_phase(self.phase)
        self.analog_sig_source_x_0_0.set_phase(self.phase)

    def get_offset(self):
        return self.offset

    def set_offset(self, offset):
        self.offset = offset
        self.analog_sig_source_x_0.set_offset(self.offset)
        self.analog_sig_source_x_0_0.set_offset(self.offset)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.channels_channel_model_0.set_noise_voltage(self.noise)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.analog_sig_source_x_0.set_frequency(self.frequency)
        self.analog_sig_source_x_0_0.set_frequency(self.frequency)

    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc

    def get_amplitude(self):
        return self.amplitude

    def set_amplitude(self, amplitude):
        self.amplitude = amplitude
        self.analog_sig_source_x_0.set_amplitude(self.amplitude)
        self.analog_sig_source_x_0_0.set_amplitude(self.amplitude)

    def get_GTX(self):
        return self.GTX

    def set_GTX(self, GTX):
        self.GTX = GTX




def main(top_block_cls=simple_flowgraph, options=None):

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
