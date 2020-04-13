#!/usr/bin/env python3

import argparse, configparser

# global variables
path = "/tmp/tali.ini"
config = configparser.ConfigParser()

def write_config_file():
  with open('/tmp/tali.ini', 'w+') as config_file:
    config.write(config_file)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--step", default=0)
  args = parser.parse_args()

  config.read(path)

  if args.step != 0: # if a step was passed as an argument, use it
    config["DEFAULT"] = { 'Step': args.step }
    write_config_file()

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
