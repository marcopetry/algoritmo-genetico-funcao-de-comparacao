LICENSE:
  MIT License. Permission is hereby granted, free of charge, to any person obtaining a copy of this Software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
  
  All available material can be used in other works with the reference:
      ORTONCELLI, A. R.; BELLON, O. R. P; SILVA, L. Summarizing driving school practical lessons by prioritizing the stress level of motorists. IEEE Transactions on Intelligent Transportation. 2020.


INSTRUCTIONS:

    Each driving activity has an id between 1 and 60.
    The dataset is organized as follows:

  - Heart Rate:
    In the folder "HeartRate" there are 60 files (.txt): one for each driving activity. The file names refer a driving activity id.
    The heart-rate was measured by the number of contractions of the heart per minute (Beats Per Minute - BPM).
    Each file line has a BPM value and the time (HH: MM: SS) at which that BPM was collected.

  - Labeled Events:
    In the folder "Data Labeled" there are 60 files (.txt): one for each driving activity. The file names refer a driving activity id.
    Each file line has a labeled event, the initial frame and the final frame of this event.
    The first line identifies the total number of frames in the video. The videos were recorded at a rate of 60 frames per second.
    The following events it was labeled:
        *RTF = rubbing parts of the face/hair
        *AU28 = Action Unit 28
        *AU19 = Action Unit 19 
        
        
    - Priorities:
      The priority of driving activities is available in the file priorities.txt.
      The higher the numerical value assigned to the priority, the higher the priority.
      

  - Trained Models:

      An Artificial Neural Network based on Numerical Regression (ANN-NR) was trained to prioritize pairs of activities
      The ANN-NR is a Multi-Layer Perceptron with two hidden layers with 50 and 30 neurons, respectively. The following parameters it used to train ANN-NR: RELU activation function, ADAM optimizer, learning rage 0,001 (adaptive), momentum 0,9, and 1000 sessions.
      
      The trained models as in the folder Models. The trained models are in subfolders identified by the training parameters:
         The algorithm shows how to use the trained models: 5 minutes, 10 minutes, 15 minutes, 20 minutes, 25 minutes, 30 minutes, and the full size of the video.
         Training set size: 10, 15, 20, 30, 35, 40, 45, and 50.

      The file sets.txt (also in the folder Models) as the driving activities used to create the training and test sets. These sets were randomly created.

  - Feature extracted and algorithms:
    The algorithm used to compute the accuracy of the comparative function as in the folder "Code".
      The algorithm shows how to use the trained models.


