#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon May  1 22:02:33 2017
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import numbersink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")

        ##################################################
        # Variables
        ##################################################
        self.samples_per_bit = samples_per_bit = 40960
        self.samp_rate = samp_rate = 32000
        self.b_power = b_power = 1
        self.a_power = a_power = .5

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_numbersink2_3 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit='',
        	minval=-100,
        	maxval=100,
        	factor=1.0,
        	decimal_places=10,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=False,
        	avg_alpha=.001,
        	label='Neither',
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_3.win)
        self.wxgui_numbersink2_2 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit='',
        	minval=-100,
        	maxval=100,
        	factor=1.0,
        	decimal_places=10,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=False,
        	avg_alpha=.001,
        	label='B',
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_2.win)
        self.wxgui_numbersink2_1 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit='',
        	minval=-100,
        	maxval=100,
        	factor=1.0,
        	decimal_places=10,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=False,
        	avg_alpha=.001,
        	label='A',
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_1.win)
        self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
        	self.GetWin(),
        	unit='',
        	minval=-100,
        	maxval=100,
        	factor=1.0,
        	decimal_places=10,
        	ref_level=0,
        	sample_rate=samp_rate,
        	number_rate=15,
        	average=False,
        	avg_alpha=.001,
        	label='A + B',
        	peak_hold=False,
        	show_gauge=True,
        )
        self.Add(self.wxgui_numbersink2_0.win)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate,True)
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((b_power, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((a_power, ))
        self.blocks_moving_average_xx_3 = blocks.moving_average_ff(samples_per_bit, 1, 4000)
        self.blocks_moving_average_xx_2 = blocks.moving_average_ff(samples_per_bit, 1, 4000)
        self.blocks_moving_average_xx_1 = blocks.moving_average_ff(samples_per_bit, 1, 4000)
        self.blocks_moving_average_xx_0 = blocks.moving_average_ff(samples_per_bit, 1, 4000)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, '/Users/jaredweinstein/Desktop/CS434Project/src/carrier', True)
        self.blocks_file_sink_3 = blocks.file_sink(gr.sizeof_float*1, '/Users/jaredweinstein/Desktop/CS434Project/output/avg_b', False)
        self.blocks_file_sink_3.set_unbuffered(False)
        self.blocks_file_sink_2 = blocks.file_sink(gr.sizeof_float*1, '/Users/jaredweinstein/Desktop/CS434Project/output/avg_both', False)
        self.blocks_file_sink_2.set_unbuffered(False)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_float*1, '/Users/jaredweinstein/Desktop/CS434Project/output/avg_a', False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, '/Users/jaredweinstein/Desktop/CS434Project/output/avg_neither', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blocks_divide_xx_0 = blocks.divide_ff(1)
        self.blocks_add_xx_2 = blocks.add_vff(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_abs_xx_0 = blocks.abs_ff(1)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, samples_per_bit)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_divide_xx_0, 1))
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_add_xx_2, 1))
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_moving_average_xx_3, 0))
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_abs_xx_0, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_moving_average_xx_1, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.blocks_add_xx_2, 0), (self.blocks_moving_average_xx_2, 0))
        self.connect((self.blocks_divide_xx_0, 0), (self.blocks_abs_xx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_divide_xx_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_moving_average_xx_1, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.blocks_moving_average_xx_1, 0), (self.wxgui_numbersink2_1, 0))
        self.connect((self.blocks_moving_average_xx_2, 0), (self.blocks_file_sink_3, 0))
        self.connect((self.blocks_moving_average_xx_2, 0), (self.wxgui_numbersink2_2, 0))
        self.connect((self.blocks_moving_average_xx_3, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_moving_average_xx_3, 0), (self.wxgui_numbersink2_3, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_2, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_file_sink_2, 0))
        self.connect((self.blocks_throttle_0, 0), (self.wxgui_numbersink2_0, 0))

    def get_samples_per_bit(self):
        return self.samples_per_bit

    def set_samples_per_bit(self, samples_per_bit):
        self.samples_per_bit = samples_per_bit
        self.blocks_moving_average_xx_3.set_length_and_scale(self.samples_per_bit, 1)
        self.blocks_moving_average_xx_2.set_length_and_scale(self.samples_per_bit, 1)
        self.blocks_moving_average_xx_1.set_length_and_scale(self.samples_per_bit, 1)
        self.blocks_moving_average_xx_0.set_length_and_scale(self.samples_per_bit, 1)
        self.analog_const_source_x_0.set_offset(self.samples_per_bit)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_b_power(self):
        return self.b_power

    def set_b_power(self, b_power):
        self.b_power = b_power
        self.blocks_multiply_const_vxx_1.set_k((self.b_power, ))

    def get_a_power(self):
        return self.a_power

    def set_a_power(self, a_power):
        self.a_power = a_power
        self.blocks_multiply_const_vxx_0.set_k((self.a_power, ))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
