from augmentations import *
import os
import random
from multiprocessing import Process

#Below test has been written to take all the files in a directory and apply all types of degradations 
#on them and create relevantly named files in the same directory. You can also apply them on single files

#Currently output file directory is './output', for changing it, change the variable 'outfile_path' in augmentations.py

path = '/path/to/data'
for root, dirs, files in os.walk(path):
    for f in files:
        current_file = os.path.join(root, f)
        #print dirs, f
        print "current file - - - - -> " + current_file
        #The below line is to ignore some file(if no file to exclude, please delete it)
        if current_file!= ("any/exception/like/Readme.txt"):
                #random_cropping(current_file, 2)
                rnd1 = random.uniform(10,20)
                p1 = Process(target = add_noise, args = (current_file, 'white-noise', rnd1))
                p1.start()
                rnd2 = random.uniform(0.1,0.5)
                p2 = Process(target = convolve, args = (current_file, 'classroom', rnd2))
                p2.start()
                rnd3 = random.uniform(0.1,0.5)
                p3 = Process(target = convolve, args = (current_file, 'smartphone_mic', rnd3))
                p3.start()
                #apply_gain(current_file, 20)
                rnd4 = random.uniform(0.7,1.3)
                p4 = Process(target = apply_rubberband, args = (current_file, rnd4, 1.0))
                p4.start()
                rnd5 = random.uniform(0.7,1.3)
                p5 = Process(target = apply_rubberband, args = (current_file, 1.0, rnd5))
                p5.start()
                rnd6 = random.randint(1,3)
                p6 = Process(target = apply_dr_compression, args = (current_file, rnd6))
                p6.start()
                #apply_eq(current_file, '500;50;10')
