
import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, mu=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
      
        self.mu = mu

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        output_items[0][:] = np.sign(input_items[0])*np.log(1+self.mu*np.abs(input_items[0]))/np.log(1+self.mu)
        return len(output_items[0])
