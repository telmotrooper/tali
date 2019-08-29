# ANSI escape codes for formatting in the terminal
cyan_code = "\u001b[36m"
green_code = "\u001b[32m"
yellow_code = "\u001b[33m"
reset = "\u001b[0m"

def cyan(text):
  return cyan_code + text + reset

def green(text):
  return green_code + text + reset

def yellow(text):
  return yellow_code + text + reset
