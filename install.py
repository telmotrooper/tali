#!/usr/bin/env python3

import configparser

path = "/tmp/tali.ini"

config = configparser.ConfigParser()

config.read(path)

if config.read(path) == []: # no config file found
  config["DEFAULT"] = { 'Step': '1' }

  with open('/tmp/tali.ini', 'w') as config_file:
    config.write(config_file)

step = int(config["DEFAULT"]["Step"])

if step == 1:
  import steps.step1
elif step == 2:
  import steps.step2
elif step == 3:
  import steps.step3
