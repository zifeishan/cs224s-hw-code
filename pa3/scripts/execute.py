#! /usr/bin/python
import sys, os, random

# tot_args = [[50,100],
# [15,20,50],
# [500,700,1000],
# [1.0,1.25,1.35],
# [1,2,3,4],
# [4]]

# tot_args = [[50],
# [30,50],
# [500],
# [1.0,1.25],
# [1,2,3,4],
# [4]]

# tot_args = [[50],
# [50],
# [500],
# [1.2],
# [2],
# [1,2,3,4],
# [0],
# [0],
# [0]]

tot_args = [[10],
[8],
[100],
[1],
[0],
[1,2,3,4],
[0],
[0],
[0]]

used_argmap = set()
lengths = [len(a) for a in tot_args]

fout = open('runall.sh', 'w')
for i in range(4):
  while True:
    pair = tuple([random.randint(0, l - 1) for l in lengths])
    # print pair
    if pair not in used_argmap:
      used_argmap.add( pair )
      break
  
  args = [tot_args[j][pair[j]] for j in range(len(tot_args))]
  # print args
  filename = '-'.join([str(y) for y in args])
  # print 'save to:',filename

  print >>fout, 'echo "executing args:',args,'"'
  print >>fout, 'bash run-args.sh ' + ' '.join([str(x) for x in args]) + ' >results/'+filename
  
  # os.system('bash run-args.sh ' + ' '.join([str(x) for x in args]) + ' > results/'+filename)
fout.close()