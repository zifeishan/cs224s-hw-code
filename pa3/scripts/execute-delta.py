#! /usr/bin/python
import sys, os, random

tot_args = [[100,200],
[300,800,1200]]

used_argmap = set()
lengths = [len(a) for a in tot_args]

fout = open('runall-delta.sh', 'w')
for i in range(6):
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
  print >>fout, 'bash run-args-delta-only.sh ' + ' '.join([str(x) for x in args]) + ' >results-delta/'+filename
  
  # os.system('bash run-args.sh ' + ' '.join([str(x) for x in args]) + ' > results/'+filename)
fout.close()