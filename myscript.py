import os
import subprocess
# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("badhash", help="The hash of the bad commit")
# parser.add_argument("goodhash", help="The hash of the good commit")

# badhash = parser.parse_args().badhash
# goodhash = parser.parse_args().goodhash
badhash = "01c7fa9ff06348f539599aad591836c129a3ab13" 
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"

# os.system(f'git bisect start {badhash} {goodhash}')
# os.system('git bisect run manage.py test')
# os.system('git bisect reset')

output_1 = subprocess.check_output(f"git bisect start {badhash} {goodhash}", shell=True)
output_2 = subprocess.check_output("git bisect run manage.py test", shell=True)
output_3 = subprocess.check_output("git bisect reset", shell=True)

print(output_1)
print(output_2)
print(output_3)