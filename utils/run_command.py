import subprocess, sys

def run_command(command: str):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode().rstrip()
        return output
    except subprocess.CalledProcessError as e:
        print("An error occurred:")
        print(e.output)
        sys.exit()
