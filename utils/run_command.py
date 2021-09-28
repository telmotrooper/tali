import subprocess, sys

def run_command(command: str):
    try:
        output = subprocess.check_output(command, shell=True).decode().rstrip()
        return output
    except subprocess.CalledProcessError as e:
        print("An error occurred:")
        print(e.output)
        sys.exit()

def run_and_print_command(command: str):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)

    for line in iter(process.stdout.readline, ""):
        yield line
    
    process.stdout.close()

    return_code = process.wait()

    if return_code:
        raise subprocess.CalledProcessError(return_code, command)
