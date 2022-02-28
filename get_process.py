import os
import subprocess


def get_pid_process(name):
    '''
    Function to get the pid of the name process.
    '''

    output = get_all_process()

    for line in output.splitlines():
        if name in str(line):
            pid = int(line.split(None, 1)[0])

    return pid


def get_all_process():
    '''
    Function to get all process running.
    '''

    all_process = subprocess.Popen(['ps', 'A'], stdout=subprocess.PIPE)
    output, error = all_process.communicate()

    return output
