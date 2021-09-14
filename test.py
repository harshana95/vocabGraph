import plotly.io as pio
pio.renderers.default = "browser"
import numpy as np
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[ 1, 2, 3],
    y=[2,3,4],
    text=['asd','sdf','ert'],
    hovertext=['234','ert','ghgf']
))
fig.show()