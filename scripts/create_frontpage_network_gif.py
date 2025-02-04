#!/usr/bin/env python

# adapted from https://jonescompneurolab.github.io/hnn-core/stable/auto_examples/howto/plot_hnn_animation.html#sphx-glr-auto-examples-howto-plot-hnn-animation-py

from hnn_core import jones_2009_model, simulate_dipole, read_params
from hnn_core.network_models import add_erp_drives_to_jones_model
from hnn_core.viz import NetworkPlotter

net = jones_2009_model(mesh_shape=(5, 5))

# Note that we move the cells further apart to allow better visualization of
# the network (default inplane_distance=1.0 µm).
net.set_cell_positions(inplane_distance=300)

add_erp_drives_to_jones_model(net)
dpl = simulate_dipole(net, tstop=170, record_vsec='all')

net_plot = NetworkPlotter(net, bg_color='white')

print(net_plot._bg_color)

fps = 15
net_plot.export_movie('frontpage-network-animation.gif',
                      dpi=100,
                      fps=fps,
                      frame_start=795,
                      frame_stop=1495,
                      )
# normal at 15 fps is 680 frames = 45 seconds
# "frames" becomes a bunch up to around 6795

