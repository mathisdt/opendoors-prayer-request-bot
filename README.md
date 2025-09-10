# Open Doors Prayer Request Bot

This project extracts the prayer request of the day from [opendoors.de](https://www.opendoors.de/)
and posts it to a Signal group using [signal-cli](https://github.com/AsamK/signal-cli).

### Get started

1. If you don't run [signal-cli as **system DBus service**](https://github.com/AsamK/signal-cli/wiki/DBus-service)
   yet, set it up now.
2. Checkout this project to your computer (or just download the contents).
3. Copy `config-template.ini` to `config.ini` and edit it so it contains
   the phone number and group ID you want to use. To figure out the group ID,
   you can use e.g. `signal-cli --dbus-system -u +49... listGroups` (with
   `+49...` replaced by the phone number you use).
4. Make sure that at least Python 3.13 and the necessary libraries are installed
   (e.g. by executing `pip3 install -r requirements.txt`). You can also set up a
   [venv](https://docs.python.org/3/library/venv.html) and install the requirements
   inside it (recommended).
5. Execute `main.py` regularly, e.g. daily via cron.
