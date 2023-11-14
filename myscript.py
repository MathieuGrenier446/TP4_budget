import subprocess
import argparse


def shell(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except Exception as e:
        output = str(e.output)
    finished = output.split('\n')
    for line in finished:
        print(line)
    return

parser = argparse.ArgumentParser()
parser.add_argument("badhash", help="The hash of the bad commit")
parser.add_argument("goodhash", help="The hash of the good commit")

badhash = parser.parse_args().badhash
goodhash = parser.parse_args().goodhash

output_1 = shell(f'git bisect start {badhash} {goodhash}')
output_2 = shell('git bisect run manage.py test')
output_3 = shell('git bisect reset')


