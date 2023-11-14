import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("badhash", help="The hash of the bad commit")
parser.add_argument("goodhash", help="The hash of the good commit")

badhash = parser.parse_args().badhash
goodhash = parser.parse_args().goodhash

output_1 = subprocess.check_output(f'git bisect start {badhash} {goodhash}', shell=True)
output_2 = subprocess.check_output('git bisect run manage.py test', shell=True)
output_3 = subprocess.check_output('git bisect reset', shell=True)

print(output_1)
print(output_2)
print(output_3)
