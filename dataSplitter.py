import os
import sys
import random

# creates new test, train, and validation files
# 70/20/10 split
def splitter(source):
    """Split single-source data file into test and train"""
    directory = os.fsencode(source)
    
	# ensure valid directory
    if not os.path.exists('directory'):
        sys.exit('invalid directory path')
    
	# create new directories for storage
    if not os.path.exists('TrainingData'):
        os.makedirs('TrainingData')
    if not os.path.exists('TestingData'):
        os.makedirs('TestingData')
    if not os.path.exists('ValidationData'):
        os.makedirs('ValidationData')

	# maintain data counts
    train_count = 0
    test_count = 0
    valid_count = 0
    class_count = 0
    
	# for each file in source (for each class)
    for cl in os.listdir(directory):
        classname = os.fsencode(cl)
        print(os.fsdecode(classname))

        # make each class folder
        for dataFile in ['TrainingData', 'TestingData', 'ValidationData']:
            makeFile = os.path.join(os.fsencode(dataFile), classname)
            if not os.path.exists(makeFile):
                os.makedirs(makeFile)

        # navigate into class
        curClass = os.path.join(directory, classname)

        # go through pics
        for pic in os.listdir(curClass):
            picname = os.fsencode(pic)
            curPath = os.path.join(curClass, picname)

            # 70% chance of train
            if random.random() < .70: 
                newPath = 'TrainingData'
                train_count += 1
                
            # 20% chance of test
            elif random.random() < .67:
                newPath = 'TestingData'
                test_count += 1
                
            # 10% chance of validation
            else:
                newPath = 'ValidationData'
                valid_count += 1
            
            os.rename(curPath, os.path.join(os.path.join(os.fsencode(newPath), classname), picname))
        class_count += 1
                
    print('Found', class_count, 'classes.')
    print('Found', train_count+test_count+valid_count, 'files.')
    print(train_count, 'training files.')
    print(test_count, 'testing files.')
    print(valid_count, 'validation files.')

# run the splitter from the command line
if len(sys.argv) != 1:
    sys.exit("Usage: python dataSplitter.py 'filePath'")

splitter(sys.argv[0])