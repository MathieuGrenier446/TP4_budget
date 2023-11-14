import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("badhash", help="The hash of the bad commit")
parser.add_argument("goodhash", help="The hash of the good commit")

badhash = parser.parse_args().badhash
goodhash = parser.parse_args().goodhash

os.system(f'git bisect start {badhash} {goodhash}')
os.system('git bisect run manage.py test')
os.system('git bisect reset')