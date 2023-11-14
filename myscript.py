import os
# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("badhash", help="The hash of the bad commit")
# parser.add_argument("goodhash", help="The hash of the good commit")

# badhash = parser.parse_args().badhash
# goodhash = parser.parse_args().goodhash
badhash = "c1a4be04b972b6c17db242fc37752ad517c29402"
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

os.system(f'git bisect start {badhash} {goodhash}')
os.system('git bisect run manage.py test')