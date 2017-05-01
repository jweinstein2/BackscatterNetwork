#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon May  1 01:29:15 2017
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

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import numbersink2
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 800000
        self.directory = directory = 0

        ##################################################
        # Blocks
        ##################################################
        self.n = self.n = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.n.AddPage(grc_wxgui.Panel(self.n), "carrier")
        self.n.AddPage(grc_wxgui.Panel(self.n), "a")
        self.n.AddPage(grc_wxgui.Panel(self.n), "ab")
        self.Add(self.n)
        self.wxgui_scopesink2_4 = scopesink2.scope_sink_f(
        	self.n.GetPage(2).GetWin(),
        	title='A+B backscatter signal',
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
        self.n.GetPage(2).Add(self.wxgui_scopesink2_4.win)
        self.wxgui_scopesink2_3 = scopesink2.scope_sink_f(
        	self.n.GetPage(2).GetWin(),
        	title='B source data',
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
        self.n.GetPage(2).Add(self.wxgui_scopesink2_3.win)
        self.wxgui_scopesink2_2 = scopesink2.scope_sink_f(
        	self.n.GetPage(1).GetWin(),
        	title='A source data',
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
        self.n.GetPage(1).Add(self.wxgui_scopesink2_2.win)
        self.wxgui_scopesink2_1 = scopesink2.scope_sink_f(
        	self.n.GetPage(0).GetWin(),
        	title='Carrier Wave',
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
        self.n.GetPage(0).Add(self.wxgui_scopesink2_1.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
        	self.n.GetPage(1).GetWin(),
        	title='A Backscatter Signal',
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
        self.n.GetPage(1).Add(self.wxgui_scopesink2_0.win)
        self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
        	self.n.GetPage(0).GetWin(),
        	unit='Units',
        	minval=-100,
        	maxval=100,
        	factor=1.0,
        	decimal_places=10,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=False,
        	avg_alpha=None,
        	label='Ivan Number Sink',
        	peak_hold=False,
        	show_gauge=True,
        )
        self.n.GetPage(0).Add(self.wxgui_numbersink2_0.win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_rms_xx_0 = blocks.rms_ff(0.0001)
        self.blocks_repeat_3 = blocks.repeat(gr.sizeof_int*1, 3)
        self.blocks_repeat_2 = blocks.repeat(gr.sizeof_int*1, 2)
        self.blocks_repeat_1 = blocks.repeat(gr.sizeof_float*1, 40960)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, 40960)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vff((2.5/11, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((1, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((.5, ))
        self.blocks_int_to_float_1 = blocks.int_to_float(1, 1)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, '/Users/jaredweinstein/Desktop/CS434Project/src/carrier', True)
        self.blocks_file_sink_4 = blocks.file_sink(gr.sizeof_float*1, '/Users/jaredweinstein/Desktop/CS434Project/output/b_srcdata', False)
        self.blocks_file_sink_4.set_unbuffered(False)
        self.blocks_file_sink_3 = blocks.file_sink(gr.sizeof_float*1, '/Users/jaredweinstein/Desktop/CS434Project/output/ab_backscatter', False)
        self.blocks_file_sink_3.set_unbuffered(False)
        self.blocks_file_sink_2 = blocks.file_sink(gr.sizeof_float*1, '/Users/jaredweinstein/Desktop/CS434Project/output/a_srcdata', False)
        self.blocks_file_sink_2.set_unbuffered(False)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_float*1, '/Users/jaredweinstein/Desktop/CS434Project/output/carrier', False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, '/Users/jaredweinstein/Desktop/CS434Project/output/a_backscatter', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.analog_random_source_x_1 = blocks.vector_source_i(map(int, numpy.random.randint(0, 2, 1000)), True)
        self.analog_random_source_x_0 = blocks.vector_source_i(map(int, numpy.random.randint(0, 2, 1000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_repeat_3, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.blocks_repeat_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_file_sink_3, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.wxgui_scopesink2_4, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_file_sink_2, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.wxgui_scopesink2_2, 0))
        self.connect((self.blocks_int_to_float_1, 0), (self.blocks_file_sink_4, 0))
        self.connect((self.blocks_int_to_float_1, 0), (self.blocks_repeat_1, 0))
        self.connect((self.blocks_int_to_float_1, 0), (self.wxgui_scopesink2_3, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_rms_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.wxgui_scopesink2_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_repeat_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.blocks_repeat_2, 0), (self.blocks_int_to_float_1, 0))
        self.connect((self.blocks_repeat_3, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.blocks_rms_xx_0, 0), (self.wxgui_numbersink2_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_scopesink2_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_scopesink2_4.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_3.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_2.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_1.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_directory(self):
        return self.directory

    def set_directory(self, directory):
        self.directory = directory


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
