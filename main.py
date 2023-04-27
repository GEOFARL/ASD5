import sys

input_file = sys.argv[1]

with open(input_file) as f:
  A = [int(l.strip()) for l in f.readlines()][1:]
