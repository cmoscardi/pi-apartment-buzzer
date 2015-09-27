# Buzzer
This repo contains the code for an apartment buzzer that buzzes people who send the correct text message to a number.

# Installation Instructions
You should be on a Raspberry Pi with GPIO pins.

You have to be root user to use the RPi.GPIO library, or do some fancy SUID things (this being a raspberry pi, I didn't delve into the security concerns as a borked system is basically just an hour of annoyance).

Copy `config.py.sample` to `config.py`

pip install from `requirements.txt`

Try `python app.py` - that's it!
