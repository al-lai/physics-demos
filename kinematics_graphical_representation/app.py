import streamlit as st
import numpy as np
import pandas as pd

# Interactive Streamlit elements, like these sliders, return their value.
# This gives you an extremely simple interaction model.
acceleration = st.sidebar.slider("Acceleration", -10, 10, 0, 1)
initial_velocity = st.sidebar.slider("Initial Velocity", -20, 20, 0, 1)

time_steps = 100
t = np.linspace(0., 10., time_steps)

velocity = initial_velocity + acceleration * t
displacement = initial_velocity * t + 0.5 * acceleration * t**2

data = pd.DataFrame(
    {'time': t,
     'velocity': velocity,
     'displacement': displacement,
     'acceleration': [acceleration]*time_steps}
)

st.title('Kinematics - Graphical Representation')
# create s ~ t, v ~ t, a ~ t graphs
st.line_chart(data, x='time', y='displacement', use_container_width=True)
st.line_chart(data, x='time', y='velocity', use_container_width=True)
st.line_chart(data, x='time', y='acceleration', use_container_width=True)
# fig = px.line(x=t, y=displacement, labels={'x': 'time / s', 'y': 'displacement /m'})
# st.plotly_chart(fig, use_container_width=True)