# weatherdisplaymqttconditions
Script to read the MQTT feed from Weather Display and Convert/Publish to a text string based on conditions.

Useful for Scrolling Displays/eink Devices/Home Assistant or Headers on Web Pages.

The text output can be expanded/edited accordingly, based on adding other elements from the ClientRaw Feed. 

Example output -

From:

b'wdwf12345 0.6 0.0 304 14.6 93.70 1013.8 0.0 16.2 157.6 0.00 0.00 21.3 59 100.0 19 14.6 0 0 0.0 14.6 27.3 11.8 14.6 -100.0 -100.0 94 -100 -100 08 45 30 mystation-8:45:30_AM 0 42 19 8 0.00 0.00 100 100 100 100 100 14.6 17.7 15.9 14.6 19 Cloudy/Dry 0.1 0 1 1 1 0 1 1 0 0 0 0 0 1 1 2 2 1 1 0 0 10.0 13.6 413.6 8/19/2021 19.0 17.6 15.9 14.6 0.6 1 2 0 2 2 1 0 1 2 1 15.0 15.0 14.9 14.8 14.8 14.7 14.6 14.6 14.6 14.6 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 15.9 14.6 14.6 8.2 0 15:30:37 2021/18/05 304 0 0 -100.0 -100.0 94 -100 -100 -100 -100 97.0 21.8 20.9 18.0 1014.5 1013.4 7 7:50_AM 6:33_AM 18.1 13.2 13.7 13.3 2 2021 -17.8 -1 1 -1 274 294 297 302 291 54 349 81 267 169 0.0 255.0 0.9 14.0 56.00000 -0.10000 0.0 94 86 0.0 8:25_AM 0.0 0.0 0.0 0.0 0.0 0.0 38.2 12:04_AM 8:25_AM 255 !!C10.37S125!! '

To:

The Weather is Partly Cloudy, 14.6 Degrees Centigrade & Falling, Pressure: 1013.8 Mb & Steady, Wind North West 0.9 Mph


We use it on an LED Scrolling Matrix Display, on Home Assistant and to show conditions on an eink Screen.
