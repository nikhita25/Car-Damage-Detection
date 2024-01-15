**Initial Notes:**

- Create/organize repo – Lizzette
- Rohit will lead the project, has some experience
- Nikhita, Jose, and Lizzette will assist by dividing tasks, exploring the dataset, understanding the process, making suggestions, and so on
- Coordinate weekly meetings (1-2x per week)

**Meeting 04/05/23**

Discussing the basic steps before building the trained model.

_Preprocessing:_

- Data augmentation: using keras, we have 3 class–do it for each one **(rohit)**

Total: 1631 images

Training: minor: 453, moderate: 464, severe: 469

- Add 500 more to each class, about 50 more for each

- Data labeling: using labelmg,
  - Divide the labeling amongst all four members
  - Lizzette will divide the data that needs to be labeled for each member and send it to them

- 1-346 images ( **minor** ): 346 images
- 347-458 ( **minor** ), 1-235 ( **moderate** ): 346 images
- 236-464 ( **moderate** ), 1-118 ( **severe** ): 228 images, 118 images, 346 images
- 119-469 ( **severe** ): 350 images

_Building the model:_

- Build base model: object detection algorithm,
- Use imagenet to train the model, also use yolo and dectron2

**Meeting 04/10/23:**

1. Rohit will only work on the data augmentation to begin the preprocessing of the data
2. The remainder of the group will work on understanding if baseline models work for this classification problem before moving to more advanced models

  1. Do some research on this kind of problem
  2. Convert the images to csv file for baseline training/validation models

    1. Decision Tree
    2. Random Forest
    3. Logistic Regression, etc.

1. We will meet again on Wednesday to regroup and discuss our findings/results

**Meeting 04/12/23 (CANCELED) — rescheduling due to conflicts**

**Meeting 04/15/23 — Update on progress and results with image2csv method**

  **Rohit** — _included the image to csv for training dataset, data augmentation, exploring some of the baseline models_

  **Jose** — _In-depth analysis of KNN model , grid search, plots, reports (focus on improving accuracy)_

  **Nikki** — _In-depth analysis of DecisionTree model, grid search, plots, reports (focus on improving accuracy)_

  **Lizzette** — Comparison of multiple baseline models with preliminary analysis on classification metrics (reports, plots, etc)

**Meeting 04/17/23:**

Ask Prof. Grossberg:

- Currently processing data in grey scale, resize to 28x28, increased data size
- Next steps?

1. Redo the training and validation models using single csv file
2. Clean repo, remove unnecessary data — ONE .csv file (training + validation combined), have the images and other csv files in the google drive
3. Consolidate notebooks with redundant code for final version
4. Preform EDA on final csv dataset (include in final notebook version)

**In-class Meeting 04/18/23 (Feedback):**

- Instead of csv file use numpy array  numpy.save (improves efficiency), will recognize all the types (allow\_pickle)
- When dealing with complex data, choice of features is important. From individual pixels, you cant tell a lot, there isn't a lot of information,
- Build features out of it, take histograms of the bin size of RGB values, edge filters on the images, compare and see if there are discontinuities
- Statistics on the histograms:
- Feature Engineering
- PCA: dimension reduction

**In-class Meeting 04/25/23 (Feedback):**

- GENRAL FEEDBACK:
  - Feature extraction wasn't good  overfitting
  - Learn to use Wiki, issues on github
  - More graphs
  - Run models

**Meeting 04/26/23:**

**Project Lead Next Steps Discussion:**

- Project Lead (Rohit): give group members next steps, coordinate tasks, advise on what methods/experiments can work
  - NEXT STEPS:
    - Increase the size of training to 10k images
    - Data Feature extraction: visualize the features, plot the graphs
      - SIFT, histograms, edges, corners, SURF, blob (everyone look into these two feature extraction methods, understand the feature, hyperparameter tuning)
    - Run multiple models: ML models end-to-end pipeline (incorporate ML models in results)
    -

**Discussing results from EDA/FEATURE SELECTION:**

- Rohit: used histogram and SIFT to extract features, used PCA, used TSNE to plot histogram (challenge: regularize the TSNE in depth, not giving separate clusters – training accuracy: 100%, testing: 70%)
- Nikki: used SURF (giving error), edge detection (properly detecting edges), blobs (doesn't really detect anything using simple blob detector, will try to tune it)
- Jose: looked into many filters for feature extractions and ran them through the RF
- Lizzette: looking into edges and other work that uses edges on image classification problems

**Tasks for this week:**

1. Team members will look into these features assigned to them,

- Rohit: histograms/SIFT (Side task: Create requirements.txt and export his env for us to use, Increase the size of training to 10k images )
- Lizzette: Edges/HOG (side task: learn to use Wiki)
- Nikki: SURF (maybe)/Blobs/HOG
- Jose: Corner/Textures

1. Everyone will run the same ML models for results comparison
  - (MUST DO: **RF, NB, LogReg** (multi-class), if we have time we try **SVM** )
2. Create 1-2 slides on results

**Deadline for filters:** Friday night or Saturday night (flexible)

**Deadline for Models/Results** : Sunday night (FINAL!! needs to go in ppt so no excuses)

**Deadline for ppt slides:** Monday night (FINAL)

**PPT format:**

1. Background
2. What we did this week (summary: includes goals for the week, problems/challenges we're facing)
3. Methods, results, and graphs, (everyone does 1-2)
4. Goals/game plan for next week + Questions if any
5. Insights: try to breakdown work and commit the work with respect to task

**In-class Meeting 05/02/23 (Feedback):**

- GENRAL FEEDBACK:
  - CNN: Imagenet is a dataset that a lot of deep learning methods have been trained on, use the output of the
  - Take the image and feed it into the CNN

**Meeting Notes for 5/4/2023**

Project as 3 parts:

- Machine Learning,
- Machine Learning/Deep Learning
- Deep Learning.

Compare the results.

Work on the 2 methods mentioned in class (feature extraction with statistics/histograms and feature extraction with CNN)

1. Use Histogram and statistics. Run the Machine Learning Models on these features.  **(Nikhita, Jose)**
  - Use Percentages of bins to make data more significant
  - Run filters and then plot the histogram/statistics
  - Maybe Dimension Reduction
  - Run ML models
2. Use CNN (deep learning) to extract features from images and run the Machine Learning Models **(Rohit) **
  - Take the Image and feed it into CNN, take the vector for the features and then run ML Models
3. Deep Learning Models. **(Lizz )**

Aim to get most of this done by Tuesday (5/9/2023). Presentation for that class should be close to our final presentation.

New data file to use for the project: [https://drive.google.com/file/d/1OAQG2JFxcK0Fonaqa4lczifarMK10tVz/view?usp=share\_link](https://drive.google.com/file/d/1OAQG2JFxcK0Fonaqa4lczifarMK10tVz/view?usp=share_link)

**Meeting Notes 05/11/23**

To Do:
-	Create sections for report
-	Work on histogram/statics portion
-	Fix overfitting 
-	Increase the images
-	Increase the accuracy
-	Use different models for histograms/statics part
-	Use VGG and other deep learning models (using same models as CNN)
-	Print out classification reports and other plots 
-	Use output np files from VGG trained model as input for ML models
