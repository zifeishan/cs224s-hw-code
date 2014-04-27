import os, sys

def Train(feature_set = None):

    # open the feature file
    f_handle = open('feats/train.lsvm', 'r')
    lines = f_handle.readlines()
    f_handle.close()

    # rewrite the features to the same file (overwrite)
    fout = open('feats/train_formatted.lsvm', 'w')

    for i, line in enumerate(lines):
        if i <= 105: # anger
            label = 1
        elif i <= 262: # despair
            label = 2
        elif i <= 408: # happiness
            label = 3
        elif i <= 463: # neutral
            label = 4
        else:
            label = 5
        
        features = line[1:].strip().split(' ')
        # print features[193]
        used_features = []
        for f in features:
            # print f.split(':'), feature_set
            if feature_set == None or int(f.split(':')[0]) in feature_set:
                used_features.append(f)

        # print used_features

        fout.write(str(label) + ' ' + ' '.join([str(x) for x in used_features]) +'\n')

        # f.write(str(label) + line[1:])
        # ' '.join()

    fout.close()

def Test():

    # open the feature file
    f_handle = open('feats/test.lsvm', 'r')
    lines = f_handle.readlines()
    f_handle.close()

    # rewrite the features to the same file (overwrite)
    fout = open('feats/test_formatted.lsvm', 'w')
    for i, line in enumerate(lines):
        if i <= 35: # anger
            label = 1
        elif i <= 70: # despair
            label = 2
        elif i <= 105: # happiness
            label = 3
        elif i <= 130: # neutral
            label = 4
        else:
            label = 5

        fout.write(str(label) + line[1:])

    fout.close()

def ForwardSearch(feature_all):

  feature_set = set()
  fout = open('forward-features.txt', 'w')
  while len(feature_set) < len(feature_all):
    maxscore = 0.0
    maxi = -1
    for i in feature_all:
      if i in feature_set: continue
      fs = feature_set.union([i])
      # print fs
      Train( fs )
      os.system("./classifier/train -q feats/train_formatted.lsvm emotion.model")
      Test()
      os.system("./classifier/predict feats/test_formatted.lsvm emotion.model results.txt >output.txt")
      lines = open('output.txt').readlines()
      if len(lines) > 0:
        score = lines[0].lstrip('Accuracy =').split('%')[0]
        score = float(score)
        
        if score > maxscore:
          maxscore = score
          print '  -', i, score
          maxi = i

    if maxi == -1:
      break
    else:
      feature_set.add(maxi)
      print maxi, maxscore
      print >>fout, maxi, maxscore
      fout.flush()


if __name__ == '__main__':
  ForwardSearch(range(1,385))
    