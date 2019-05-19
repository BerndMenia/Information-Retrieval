- a) (3 Points): Please read the following introductory article to Matrix Factorization:
Yehuda Koren, Robert Bell, and Chris Volinsky. Matrix factorization techniques for recommender systems.Computer, (8):30–37, 2009.  URLhttp://www.inf.unibz.it/~ricci/ISR/papers/ieeecomputer.pdf
... answer the following questions:1
  
  - i (1 Point): What is the basic idea of matrix factorization and how does it contribute to recommender system performance? 

  - ii (1 Point): How does matrix factorization work? 

  - iii (1 Point): Which learning algorithms are proposed in the paper and how do those work in principle? 


- b) (1 Point): Based on the Surprise library, we can easily also compute SVD recommendations. What is the difference between matrix factorization and SVD? How do the results compare to the results of the rather simple KNN recommender algorithm of the previous exercise? 

.....................................................................................................

- a) There are two main approaches for recommender systems: Explicit and implicit feedback. Explicit feedback is data given by the user in form of a rating system, e.g. rate a product from 1 (bad) up to 5 (good). Many companies like amazon or Netflix use this type of feedback system. 
  
  The other one is implicit feedback. The difference to explicit feedback is that now there are only binary ratings, e.g. thumbs up or thumbs down like YouTube does. 
  
  Keeping that in mind "Collaborative Filtering" is used in unison with the feedback. It models relationships between users of a platform and makes it possible to recommend products to a user. 
  
  Keeping that in mind there are two other user-oriented systems that get used in unison with the feedback. The first one is "user-oriented neighborhood". It filters content based on what similar users like (think of amazon's "users who bought this product also bought ..."). The second one is the latent factor model. It takes into account both users and items and models them like a plot with N factors. 
  
- i: Matrix factorization is often used with the latent factor model. Each of the N factors corresponds to a vector in the matrix and is created from the ratings of the corresponding factor. Research has shown that they tend to have good scalability and accuracy for recommender systems. These matrices can be used either with implicit or explicit feedback for the vector creation. 
 
- ii: Basically each user is represented by its vector (from the matrix) and from there on relationships to other users get created by calculating an N-dimensional vectors to them via the dot product. Matrix factorization is similar to Singular Value Decomposition (SVD). The advantage over SVD is that matrix factorization can work well with incomplete data, which is often the case when working with recommender systems. 

- iii: 
  - Stochastic Gradient Descent (SGD): In machine learning Gradient Descent (GD) is an algorithm that predicts data points by taking sample points as input and approximates a function out of them. This is done by calculating the intercept and slope of each sample point and combining it to find the most fitting function for each step. After the calculation the algorithm takes the new results and repeats the same process until a good approximation of the function has been found. The problem is that for big sample data and dimensions gradient descent is almost impossible to calculate in reasonable time. Imagine that we have 20000 sample points and 7 dimensions (like in last weeks exercise). For each step we would have to perform 7 * 20 000 = 140 000 calculations. This doesn't seem to much, but ramp up the dimensions to 10000 and we would have to perform already 10 000 * 20 000 = 200 000 000 which is massive. Keep in mind that this process then gets repeated multiple times. So for large data sets Gradient Descent is impractical. 
  
  To solve this problem SGD can be used. Instead of taking all data points in each step it randomly selects one and performs the calculations with it. So the order of magnitude that gets lowered is equal to the number of data points when compared to Gradient Descent, which would be 20 000 in our example. Another advantage of SGD over GD is that it disregards redundancies. If a lot of sample points are closely clusteered together then GD would still take each of them into account and perform the calculations even though they more or less result in the same value. SGD disregards this problem for the most part by randomly selecting just one point. 
  
  It is also possible to use SGD with more than just one sample point per step. If kept low the calculation time doesn't increase by much, but the accuracy of the resulting function increases noticeably. In other words this version of SGD combines the positive effects of both GD and SGD with just one sample point per step. 
  
  Also it is easily possible to add new data points to SGD and simply perform a step with the new sample point. For GD we would have to start the whole caclulation process from scratch. 
  
  - Alternating Least Squares (ALS): As we know it is likely that there is incomplete information in our calculations. "However, if we fix one of the unknowns, the op-timization problem becomes quadratic and can be solved optimally." 
  The major disadvantage of ALS over SGD is that it is slower and more complex. However ALS can be parallelized and can therefore have better computation time than SGD when properly used. Another advantage of ALS over GD (not SGD) is if the sample data is implicit. In that case looping over all sample points is expensive for GD, but not so much for ALS. Allthough this second advantage can be neglected when regarding SGD instead of GD. 

- b 