# import os


# os.system(f'git bisect start {badhash} {goodhash}')
# os.system('git bisect run manage.py test')
# os.system('git bisect reset')

import subprocess


badhash = "01c7fa9ff06348f539599aad591836c129a3ab13" 
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

output_1 = subprocess.run(f"git bisect start {badhash} {goodhash}", shell=True, check=False).stdout
output_2 = subprocess.run("git bisect run manage.py test", shell=True, check=False).stdout
output_3 = subprocess.run("git bisect reset", shell=True, check=False).stdout

print(output_1)
print(output_2)
print(output_3)

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("badhash", help="The hash of the bad commit")
# parser.add_argument("goodhash", help="The hash of the good commit")

# badhash = parser.parse_args().badhash
# goodhash = parser.parse_args().goodhash

