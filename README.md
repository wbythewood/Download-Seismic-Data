# Download-Seismic-Data

This code allows a user to download seismic data based on event times or lengths of time.

Most tunable parameters are in the config.py file. Start there, and set everything the way you want. 

Some additional parameters are left in the code. Since this is a notebook, it should be relatively easy to change those, too. 

Event download is based on event times, which the code searches through a catalogue to determine which events fit your parameters, and saves those event start times. 

Noise download can either be based on these event times (e.g., if you want to correct event data with some amount of noise data from before the event), or day-long files for a specified period of time.

Based on codes fetch_EVENTS and fetch_NOISE from Josh Russell.
