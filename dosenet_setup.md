# SSH name and password
serving...?
pi@192.168.4.1
piistasty!

Go to dosenet-raspberrypi/ and do `git pull`.

# How-to
### SCP: secure copy for remote stuff (copy like ssh).
---
```
scp config.csv pi@[...]:/home/pi/config/config.csv
sudo shutdown now
```

### Configure WiFi
`/etc/network/interfaces` contains network stuff.
Configure static IP there if not using WiFi.
Configure `/etc/wpa_supplicant/wpa_supplicant.conf` for
WiFi.
`ssid`: name of network
`password`: password
If it is open WiFi, then only change interfaces, but not
`wpa_supplicant.conf`.

Run the following to connect to WiFi (to use new settings):
```
sudo ifup --force wlan1
```

# At DPS Ruby Park
1. Copy over the config the file sent by Dr. Hanks.
2. Set up the WiFi at DPS Ruby Park.

