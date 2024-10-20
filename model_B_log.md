# Iter 1
## Enviroment
EPOCH = 5
LEARNING_RATE = 0.001
CATEGORIES = 10
shuffle = False
sin dropout
sin inception
sin scheduler
## Results
Evaluating model B (Raw)
Accuracy of the model on the test images: 30.30%

Evaluating model B (Bilateral)
Accuracy of the model on the test images: 39.39%

Evaluating model B (Canny)
Accuracy of the model on the test images: 42.42%


# Iter 2
## Enviroment
EPOCH = 20
LEARNING_RATE = 0.001
CATEGORIES = 10
shuffle = False
sin dropout
sin inception
sin scheduler
## Results
Evaluating model B (Raw)
Accuracy of the model on the test images: 86.36%

Evaluating model B (Bilateral)
Accuracy of the model on the test images: 81.82%

Evaluating model B (Canny)
Accuracy of the model on the test images: 71.21%


# Iter 3
## Enviroment
EPOCH = 20
LEARNING_RATE = 0.0005
CATEGORIES = 10
shuffle = False
sin dropout
sin inception
sin scheduler
## Results
Evaluating model B (Raw)
Accuracy of the model on the test images: 87.88%

Evaluating model B (Bilateral)
Accuracy of the model on the test images: 89.39%

Evaluating model B (Canny)
Accuracy of the model on the test images: 66.67%


# Iter 4
## Enviroment
EPOCH = 20
LEARNING_RATE = 0.0005
CATEGORIES = 3
shuffle = False
sin dropout
sin inception
sin scheduler
## Results
Evaluating model B (Raw)
Accuracy of the model on the test images: 81.82%

Evaluating model B (Bilateral)
Accuracy of the model on the test images: 81.82%

Evaluating model B (Canny)
Accuracy of the model on the test images: 72.73%


# Iter 5
## Enviroment
EPOCH = 20
LEARNING_RATE = 0.0005
CATEGORIES = 3
shuffle = True
sin dropout
sin inception
sin scheduler
## Results
Evaluating model B (Raw)
Accuracy of the model on the test images: 87.88%

Evaluating model B (Bilateral)
Accuracy of the model on the test images: 89.39%

Evaluating model B (Canny)
Accuracy of the model on the test images: 84.85%


# Iter 6
## Enviroment
EPOCH = 20
LEARNING_RATE = 0.0005
CATEGORIES = 3
shuffle = True
con dropout
sin inception
sin scheduler
## Results
Evaluating model B (Raw)
Accuracy of the model on the test images: 84.85%

Evaluating model B (Bilateral)
Accuracy of the model on the test images: 92.42%

Evaluating model B (Canny)
Accuracy of the model on the test images: 78.79%


# Iter 7
## Enviroment
EPOCH = 20
LEARNING_RATE = 0.0005
CATEGORIES = 3
shuffle = True
con dropout
con inception
sin scheduler
## Results
Evaluating model B (Raw)
Accuracy of the model on the test images: 86.36%

Evaluating model B (Bilateral)
Accuracy of the model on the test images: 84.85%

Evaluating model B (Canny)
Accuracy of the model on the test images: 84.85%


# Iter 8
## Enviroment
EPOCH = 20
LEARNING_RATE = 0.001
CATEGORIES = 3
shuffle = True
con dropout
con inception
con scheduler factor=0.5, patience=2
## Results
Evaluating model B Raw
Accuracy of the model on the test images: 86.36%

Evaluating model B Bilateral
Accuracy of the model on the test images: 84.85%

Evaluating model B Canny
Accuracy of the model on the test images: 77.27%