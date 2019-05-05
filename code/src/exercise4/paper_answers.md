### Exercise 1  (Text Classification) [4 Points]
In this tutorial, we will deal with a further text retrieval task:  text classification. Particularly, we will look into classifying the author of a given text—the so-called authorship attribution-task. To get a first understanding of authorship attribution, please read the following paper on authorship attribution:

Efstathios Stamatatos.  A survey of modern authorship attribution methods.Journal of the American Society for Information Science and Technology, 60(3):538–556, 2009.  doi:10.1002/asi.21001.URL https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.21001

Please answer the following questions:

- a) (1.5 Points) 

    What are the main feature groups and most widely used features for authorship attribution?
    
    - "The most straightforward approach to represent texts is by vectors of word frequencies. The vast majority of authorship attribution  studies  are  (at  least  partially)  based  on  lexical features  to  represent  the  style.  This  is  also  the  traditional bag-of-words text representation followed by researchers in topic-based text classification (Sebastiani, 2002)".
    
    - "A simple and very successful method to define a lexical feature set for authorship attribution is to extract the most frequent words found in the available corpus (comprising all the texts of the candidate authors)".
    
    - 


- b) 2. (1.5 Points) 

    What are the main approaches for instance-based authorship attribution? Please also discuss the pros and cons of these approaches. 
    
    | Profile-Based | Instance-Based | 
    |:----------------------------------------------------------|:----------------------------------------------------|
    | "All training texts of an author are combined into one big text and then extract cumulative information out of it. The result is called the profile of the author". | "All training texts of an author are regarded as separate instances, each represented by a vector. A classification algorithm is then trained on these instances to develop an attribution model". 
    
    - Con: Needs special treatment if there are few instances: "Note that such classification algorithms require multiple training instances per class for extracting a reliable model.Therefore, according to instance-based approaches, in case we have only one, but a quite long, training text for a particular  candidate  author  (e.g.,  an  entire  book),  this  should be segmented into multiple parts, probably of equal length."
    
    - Con: The length of the training texts need to be normalized. To achieve this the training texts are split up into small chunks of text. There are different opinions on the chunk size, 200, 500 and 1000 character chunks have been considered. Though no matter which size is chosen it needs to be big enough so that the text can adequately represent the style of the author. 
    
    <!-- https://meta.stackexchange.com/questions/73566/is-there-markdown-to-create-tables#comment353305_73567 -->
    |                      | Profile-based approaches                   | Instance-based approaches                           |
    |:---------------------|:-------------------------------------------|:----------------------------------------------------|
    | Text representation  | One cumulative representation for all the  | Each training text is represented individually.     |
    |                      | training texts per author                  | Text segmentation may be required.                  |
    |                                                                                                                         |
    | Stylometric features | Difficult to combine different features.   | Different features can be combined easily.          |
    |                                                                                                                         |
    | Classification       | Generative (e.g., Bayesian) models,        | Discriminative models, Powerful machine learning    |
    |                      | Similarity-based methods                   | algorithms (e.g., SVM), similarity-based methods    |
    |                                                                                                                         |
    | Training time cost   | Low                                        | Relatively high (low for compression-based methods) | 
    |                                                                                                                         | 
    | Running time cost    | Low (relatively high for compression-based | Low (very high for compression-based methods)       |
    |                      | methods)                                   |                                                     |
    |                                                                                                                         |
    | Class imbalance      | Depends on the length of training texts    | Depends mainly on the amount of training texts      |
    

### c) 3. (1 Point) 
Stamatatos also discusses the evaluation of authorship attribution approaches. How can such an evaluation be performed and what are crucial aspects to ensure a fair evaluation?

- Before any evaluations are made the genre and topic of the unseen text should be taken into account. "That way, 
authorship would be the most important discriminatory factor between the  texts."

- Numerous meta data about the author like age, sex, education, nationality and the such should be taken into 
account to reduce the likelihood that the stylistic choices of a given author are characteristic of a broad group 
of people rather than strictly personal. 

- All training texts of an author should be written in the same time period. People may change over time and with 
that the stylistic choices of an author may change as well. 

- Most important evaluation parameters according to Stamatos et al.: 
    - Training corpus size, in terms of both the amount and length of training texts.
    - Test corpus size (in terms of text length of the unseen texts).
    - Number of candidate authors.
    - Distribution of the training corpus over the authors (balanced or imbalanced).
    
- The more equal the amount of training texts per author is the better. 