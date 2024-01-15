## Notes on SURF

4/22/2023 
Nikhita 

 - SURF or Speeded Up Robust Features is an algorithm for image comparison.
 - It has 2 steps: Feature Extraction and Feature Description
 - Uses Hessian matrix 

### Hessian matrix

 - A Hessian matrix belongs to a class of mathematical structures that involve second order derivatives. 
 - In the case of image processing, it has good performance and accuracy
 - The determinant of the matrix is used for both the location and scale of the image. Each pixel is given a Hessian. 
 - 

SURF descriptors has 2 steps: 
1) Fix a orientation based on information from a circular region
2) Construct a square region aligned to the selected orientation


SURF is implemented using opencv


Sources: 

https://medium.com/data-breach/introduction-to-surf-speeded-up-robust-features-c7396d6e7c4e

https://en.wikipedia.org/wiki/Hessian_matrix

SURF_create gives error for opencv with version 4.2.7. 
