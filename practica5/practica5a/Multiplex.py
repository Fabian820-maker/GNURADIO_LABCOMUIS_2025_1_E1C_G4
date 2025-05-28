#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Multiplex
# GNU Radio version: v3.10.11.0-89-ga17f69e7

from PyQt5 import Qt
from gnuradio import qtgui
import os
import sys
import logging as log

def get_state_directory() -> str:
    oldpath = os.path.expanduser("~/.grc_gnuradio")
    try:
        from gnuradio.gr import paths
        newpath = paths.persistent()
        if os.path.exists(newpath):
            return newpath
        if os.path.exists(oldpath):
            log.warning(f"Found persistent state path '{newpath}', but file does not exist. " +
                     f"Old default persistent state path '{oldpath}' exists; using that. " +
                     "Please consider moving state to new location.")
            return oldpath
        # Default to the correct path if both are configured.
        # neither old, nor new path exist: create new path, return that
        os.makedirs(newpath, exist_ok=True)
        return newpath
    except (ImportError, NameError):
        log.warning("Could not retrieve GNU Radio persistent state directory from GNU Radio. " +
                 "Trying defaults.")
        xdgstate = os.getenv("XDG_STATE_HOME", os.path.expanduser("~/.local/state"))
        xdgcand = os.path.join(xdgstate, "gnuradio")
        if os.path.exists(xdgcand):
            return xdgcand
        if os.path.exists(oldpath):
            log.warning(f"Using legacy state path '{oldpath}'. Please consider moving state " +
                     f"files to '{xdgcand}'.")
            return oldpath
        # neither old, nor new path exist: create new path, return that
        os.makedirs(xdgcand, exist_ok=True)
        return xdgcand

sys.path.append(os.environ.get('GRC_HIER_PATH', get_state_directory()))

from ModulacionPAM import ModulacionPAM  # grc-generated hier_block
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
from gnuradio.fft import window
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import sip
import threading



class Multiplex(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Multiplex", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Multiplex")
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

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Multiplex")

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
        self.samp_rate = samp_rate = 100000
        self.fs = fs = 1e3
        self.fm = fm = 100
        self.D5 = D5 = 0
        self.D4 = D4 = 0
        self.D3 = D3 = 0
        self.D2 = D2 = 0
        self.D1 = D1 = 0
        self.D = D = 10
        self.Am = Am = 1

        ##################################################
        # Blocks
        ##################################################

        self._fs_range = qtgui.Range(0, 10e3, 1, 1e3, 200)
        self._fs_win = qtgui.RangeWidget(self._fs_range, self.set_fs, "Frecuencia Pulsos", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fs_win)
        self._fm_range = qtgui.Range(0, 10e3, 10, 100, 200)
        self._fm_win = qtgui.RangeWidget(self._fm_range, self.set_fm, "Frecuencia mensaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._fm_win)
        self._D5_range = qtgui.Range(0, 100, 1, 0, 200)
        self._D5_win = qtgui.RangeWidget(self._D5_range, self.set_D5, "sinc", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D5_win)
        self._D4_range = qtgui.Range(0, 100, 1, 0, 200)
        self._D4_win = qtgui.RangeWidget(self._D4_range, self.set_D4, "RETARDO3", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D4_win)
        self._D3_range = qtgui.Range(0, 100, 1, 0, 200)
        self._D3_win = qtgui.RangeWidget(self._D3_range, self.set_D3, "RETARDO3", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D3_win)
        self._D2_range = qtgui.Range(0, 100, 1, 0, 200)
        self._D2_win = qtgui.RangeWidget(self._D2_range, self.set_D2, "RETARDO2", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D2_win)
        self._D1_range = qtgui.Range(0, 100, 1, 0, 200)
        self._D1_win = qtgui.RangeWidget(self._D1_range, self.set_D1, "RETARDO1", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D1_win)
        self._D_range = qtgui.Range(0, 50, 1, 10, 200)
        self._D_win = qtgui.RangeWidget(self._D_range, self.set_D, "Ancho Pulso", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._D_win)
        self._Am_range = qtgui.Range(0, 10, 100e-3, 1, 200)
        self._Am_win = qtgui.RangeWidget(self._Am_range, self.set_Am, "Amplitud mensaje", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._Am_win)
        self.qtgui_time_sink_x_2 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_2.set_update_time(0.10)
        self.qtgui_time_sink_x_2.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_2.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_2.enable_tags(True)
        self.qtgui_time_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_2.enable_autoscale(False)
        self.qtgui_time_sink_x_2.enable_grid(False)
        self.qtgui_time_sink_x_2.enable_axis_labels(True)
        self.qtgui_time_sink_x_2.enable_control_panel(False)
        self.qtgui_time_sink_x_2.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
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


        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_2.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_2.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_2.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_2_win = sip.wrapinstance(self.qtgui_time_sink_x_2.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_2_win)
        self.qtgui_time_sink_x_1 = qtgui.time_sink_f(
            1024, #size
            samp_rate, #samp_rate
            "", #name
            5, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1.enable_tags(True)
        self.qtgui_time_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1.enable_grid(False)
        self.qtgui_time_sink_x_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
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


        for i in range(5):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            2000, #size
            samp_rate, #samp_rate
            "", #name
            6, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
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


        for i in range(6):
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
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.low_pass_filter_0 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                100,
                fs,
                window.WIN_HAMMING,
                6.76))
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/com1_E1C_G4/GNURADIO_LABCOMUIS_2025_1_E1C_G4/practica5a/bone.wav', True)
        self.blocks_delay_3 = blocks.delay(gr.sizeof_float*1, D5)
        self.blocks_delay_2_1 = blocks.delay(gr.sizeof_float*1, D4)
        self.blocks_delay_2_0_0 = blocks.delay(gr.sizeof_float*1, D4)
        self.blocks_delay_2_0 = blocks.delay(gr.sizeof_float*1, D3)
        self.blocks_delay_2 = blocks.delay(gr.sizeof_float*1, D3)
        self.blocks_delay_1_0 = blocks.delay(gr.sizeof_float*1, D1)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_float*1, D1)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, D2)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, D2)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_sig_source_x_0_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SAW_WAVE, fm, Am, 0, 0)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(samp_rate, analog.GR_SQR_WAVE, fm, Am, 0, 0)
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_TRI_WAVE, fm, Am, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, fm, Am, 0, 0)
        self.ModulacionPAM_3_0_0 = ModulacionPAM(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModulacionPAM_3_0 = ModulacionPAM(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModulacionPAM_3 = ModulacionPAM(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModulacionPAM_2 = ModulacionPAM(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModulacionPAM_1 = ModulacionPAM(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )
        self.ModulacionPAM_0 = ModulacionPAM(
            D=D,
            fs=fs,
            samp_rate=samp_rate,
        )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.ModulacionPAM_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.ModulacionPAM_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.ModulacionPAM_0, 1), (self.qtgui_time_sink_x_1, 0))
        self.connect((self.ModulacionPAM_1, 0), (self.blocks_delay_1, 0))
        self.connect((self.ModulacionPAM_1, 1), (self.blocks_delay_1_0, 0))
        self.connect((self.ModulacionPAM_2, 0), (self.blocks_delay_0, 0))
        self.connect((self.ModulacionPAM_2, 1), (self.blocks_delay_0_0, 0))
        self.connect((self.ModulacionPAM_3, 0), (self.blocks_delay_2, 0))
        self.connect((self.ModulacionPAM_3, 1), (self.blocks_delay_2_0, 0))
        self.connect((self.ModulacionPAM_3_0, 1), (self.blocks_delay_2_0_0, 0))
        self.connect((self.ModulacionPAM_3_0, 0), (self.blocks_delay_2_1, 0))
        self.connect((self.ModulacionPAM_3_0_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.ModulacionPAM_3_0_0, 0), (self.qtgui_time_sink_x_2, 0))
        self.connect((self.ModulacionPAM_3_0_0, 1), (self.qtgui_time_sink_x_2, 2))
        self.connect((self.analog_sig_source_x_0, 0), (self.ModulacionPAM_0, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.ModulacionPAM_1, 0))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.ModulacionPAM_2, 0))
        self.connect((self.analog_sig_source_x_0_0_0_0, 0), (self.ModulacionPAM_3, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_delay_3, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_time_sink_x_0, 5))
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.blocks_delay_0, 0), (self.qtgui_time_sink_x_0, 2))
        self.connect((self.blocks_delay_0_0, 0), (self.qtgui_time_sink_x_1, 2))
        self.connect((self.blocks_delay_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_delay_1, 0), (self.qtgui_time_sink_x_0, 1))
        self.connect((self.blocks_delay_1_0, 0), (self.qtgui_time_sink_x_1, 1))
        self.connect((self.blocks_delay_2, 0), (self.blocks_add_xx_0, 3))
        self.connect((self.blocks_delay_2, 0), (self.qtgui_time_sink_x_0, 3))
        self.connect((self.blocks_delay_2_0, 0), (self.qtgui_time_sink_x_1, 3))
        self.connect((self.blocks_delay_2_0_0, 0), (self.qtgui_time_sink_x_1, 4))
        self.connect((self.blocks_delay_2_1, 0), (self.blocks_add_xx_0, 4))
        self.connect((self.blocks_delay_2_1, 0), (self.qtgui_time_sink_x_0, 4))
        self.connect((self.blocks_delay_3, 0), (self.ModulacionPAM_3_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.ModulacionPAM_3_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.qtgui_time_sink_x_2, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "Multiplex")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.ModulacionPAM_0.set_samp_rate(self.samp_rate)
        self.ModulacionPAM_1.set_samp_rate(self.samp_rate)
        self.ModulacionPAM_2.set_samp_rate(self.samp_rate)
        self.ModulacionPAM_3.set_samp_rate(self.samp_rate)
        self.ModulacionPAM_3_0.set_samp_rate(self.samp_rate)
        self.ModulacionPAM_3_0_0.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.samp_rate)
        self.analog_sig_source_x_0_0_0_0.set_sampling_freq(self.samp_rate)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 100, self.fs, window.WIN_HAMMING, 6.76))
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_2.set_samp_rate(self.samp_rate)

    def get_fs(self):
        return self.fs

    def set_fs(self, fs):
        self.fs = fs
        self.ModulacionPAM_0.set_fs(self.fs)
        self.ModulacionPAM_1.set_fs(self.fs)
        self.ModulacionPAM_2.set_fs(self.fs)
        self.ModulacionPAM_3.set_fs(self.fs)
        self.ModulacionPAM_3_0.set_fs(self.fs)
        self.ModulacionPAM_3_0_0.set_fs(self.fs)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 100, self.fs, window.WIN_HAMMING, 6.76))

    def get_fm(self):
        return self.fm

    def set_fm(self, fm):
        self.fm = fm
        self.analog_sig_source_x_0.set_frequency(self.fm)
        self.analog_sig_source_x_0_0.set_frequency(self.fm)
        self.analog_sig_source_x_0_0_0.set_frequency(self.fm)
        self.analog_sig_source_x_0_0_0_0.set_frequency(self.fm)

    def get_D5(self):
        return self.D5

    def set_D5(self, D5):
        self.D5 = D5
        self.blocks_delay_3.set_dly(int(self.D5))

    def get_D4(self):
        return self.D4

    def set_D4(self, D4):
        self.D4 = D4
        self.blocks_delay_2_0_0.set_dly(int(self.D4))
        self.blocks_delay_2_1.set_dly(int(self.D4))

    def get_D3(self):
        return self.D3

    def set_D3(self, D3):
        self.D3 = D3
        self.blocks_delay_2.set_dly(int(self.D3))
        self.blocks_delay_2_0.set_dly(int(self.D3))

    def get_D2(self):
        return self.D2

    def set_D2(self, D2):
        self.D2 = D2
        self.blocks_delay_0.set_dly(int(self.D2))
        self.blocks_delay_0_0.set_dly(int(self.D2))

    def get_D1(self):
        return self.D1

    def set_D1(self, D1):
        self.D1 = D1
        self.blocks_delay_1.set_dly(int(self.D1))
        self.blocks_delay_1_0.set_dly(int(self.D1))

    def get_D(self):
        return self.D

    def set_D(self, D):
        self.D = D
        self.ModulacionPAM_0.set_D(self.D)
        self.ModulacionPAM_1.set_D(self.D)
        self.ModulacionPAM_2.set_D(self.D)
        self.ModulacionPAM_3.set_D(self.D)
        self.ModulacionPAM_3_0.set_D(self.D)
        self.ModulacionPAM_3_0_0.set_D(self.D)

    def get_Am(self):
        return self.Am

    def set_Am(self, Am):
        self.Am = Am
        self.analog_sig_source_x_0.set_amplitude(self.Am)
        self.analog_sig_source_x_0_0.set_amplitude(self.Am)
        self.analog_sig_source_x_0_0_0.set_amplitude(self.Am)
        self.analog_sig_source_x_0_0_0_0.set_amplitude(self.Am)




def main(top_block_cls=Multiplex, options=None):

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
