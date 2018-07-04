from sys import argv
from os.path import exists

script, from_file, to_file = argv

indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}.")
print("Ready? Hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Done.")

out_file.close()
