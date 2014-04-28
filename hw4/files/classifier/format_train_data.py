# Class: CS224S
# Assignment: HW4
# Author: Frank Liu
#
# Formats the training data for use in the classifier.

def Train(feature_set = None):

    # open the feature file
    f_handle = open('feats/train.lsvm', 'r')
    lines = f_handle.readlines()
    f_handle.close()

    # rewrite the features to the same file (overwrite)
    fout = open('feats/train_formatted.lsvm', 'w')

    # used_ids = set([s.split(' ')[0] for s in open('weights.txt').readlines()])
    # used_ids = set([s.split(' ')[0] for s in open('weights.txt').readlines() if abs(float(s.split(' ')[1])) > 0.2])
    # used_ids = set([s.split(' ')[0] for s in open('forward-features-7004.txt').readlines()][:57]) %70%
    
    used_ids = set([s.split(' ')[0] for s in open('forward-features-7205.txt').readlines()][:173])


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
            # if feature_set == None or f.split(':')[0] in feature_set:
            #     used_features.append(f)
            if f.split(':')[0] in used_ids:
                used_features.append(f)

        # print len(used_features)
        # print used_features
        # raw_input()

        fout.write(str(label) + ' ' + ' '.join([str(x) for x in used_features]) +'\n')

        # f.write(str(label) + line[1:])
        # ' '.join()

    fout.close()

if __name__ == '__main__':
    Train()