from subprocess import check_output

def run_command(command: str):
    output = check_output(command, shell=True, stderr=subprocess.STDOUT).decode().rstrip()
    return output
