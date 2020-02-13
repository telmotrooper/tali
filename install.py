#!/usr/bin/env python3

import configparser

# global variables
path = "/tmp/tali.ini"
config = configparser.ConfigParser()

def write_config_file():
  with open('/tmp/tali.ini', 'w+') as config_file:
    config.write(config_file)

def main():
  config.read(path)

  if config.read(path) == []: # no config file found
    config["DEFAULT"] = { 'Step': '1' }
    write_config_file()

  step = int(config["DEFAULT"]["Step"])

  if step == 1:
    import steps.step1
    config["DEFAULT"] = { 'Step': '2' }
    write_config_file()
    
  elif step == 2:
    import steps.step2
    config["DEFAULT"] = { 'Step': '3' }
    write_config_file()
  
  elif step == 3:
    import steps.step3

if __name__ == "__main__":
  main()
