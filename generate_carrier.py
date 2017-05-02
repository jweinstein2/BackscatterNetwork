#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Generate Carrier
# Generated: Tue May  2 15:18:53 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class generate_carrier(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Generate Carrier")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.resolution = resolution = samp_rate /  1024

        ##################################################
        # Blocks
        ##################################################
        self.tx = self.tx = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.tx.AddPage(grc_wxgui.Panel(self.tx), "FFT")
        self.tx.AddPage(grc_wxgui.Panel(self.tx), "SCOPE")
        self.Add(self.tx)
        self.wxgui_scopesink2_1 = scopesink2.scope_sink_f(
        	self.tx.GetPage(1).GetWin(),
        	title='Scope After Modulation',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.tx.GetPage(1).Add(self.wxgui_scopesink2_1.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.tx.GetPage(1).GetWin(),
        	title='Scope Before Modulation',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.tx.GetPage(1).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_fftsink2_1 = fftsink2.fft_sink_f(
        	self.tx.GetPage(0).GetWin(),
        	baseband_freq=290000,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=40000,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT After Modulation',
        	peak_hold=False,
        )
        self.tx.GetPage(0).Add(self.wxgui_fftsink2_1.win)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
        	self.tx.GetPage(0).GetWin(),
        	baseband_freq=0,
        	y_per_div=10,
        	y_divs=10,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=32000,
        	fft_size=1024,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='FFT Before Modulation',
        	peak_hold=False,
        )
        self.tx.GetPage(0).Add(self.wxgui_fftsink2_0.win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_float*1, '/Users/jaredweinstein/Desktop/CS434Project/src/carrier', False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, '/Users/jaredweinstein/School/Sophomore/Networking/PS2_JaredWeinstein/tmp/unmodulated_sink', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((1.25, ))
        self.audio_source_0 = audio.source(samp_rate, '', True)
        self.analog_sig_source_x_0 = analog.sig_source_f(4096000, analog.GR_COS_WAVE, 960000, 700, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.audio_source_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.audio_source_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.audio_source_0, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.audio_source_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.wxgui_scopesink2_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_1, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_1.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.set_resolution(self.samp_rate /  1024)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_resolution(self):
        return self.resolution

    def set_resolution(self, resolution):
        self.resolution = resolution


def main(top_block_cls=generate_carrier, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
