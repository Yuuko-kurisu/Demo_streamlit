''' 

目前的组件
    - note
待定
    - button
    - sidebar

'''



import streamlit as st

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.markdown("# Note")

st.markdown("## 折叠笔记")

with st.expander("See notes"):

    st.markdown("""
A Q-transform plot shows how a signal’s frequency changes with time.

 * The x-axis shows time
 * The y-axis shows frequency

The color scale shows the amount of “energy” or “signal power” in each time-frequency pixel.

A parameter called “Q” refers to the quality factor.  A higher quality factor corresponds to a larger number of cycles in each time-frequency pixel.  

For gravitational-wave signals, binary black holes are most clear with lower Q values (Q = 5-20), where binary neutron star mergers work better with higher Q values (Q = 80 - 120).

See also:

 * [GWpy q-transform](https://gwpy.github.io/docs/stable/examples/timeseries/qscan.html)
 * [Reading Time-frequency plots](https://labcit.ligo.caltech.edu/~jkanner/aapt/web/math.html#tfplot)
 * [Shourov Chatterji PhD Thesis](https://dspace.mit.edu/handle/1721.1/34388)
""")
    
st.markdown("# Button")


st.markdown("# Sidebar")