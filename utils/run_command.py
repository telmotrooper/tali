import subprocess

def run_command(command: str):
    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode().rstrip()
    return output
