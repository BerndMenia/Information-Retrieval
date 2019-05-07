### Exercise 1 (Word Embeddings Theory) (3 points)

This week,  we are going to explore word embeddings,  a state-of-the-art vector representation method for words that also captures the context in which these words occur.  This allows to not only perform retrieval tasks based on syntactic but also on semantic similarity.To get a first overview, please watch Chris Manning’s introductory lecture on distributed word vec-tor representations and word2vec (first 42 minutes of the video)1. Answer the following questions regarding distributed vector representations:

- a (1.5 points): What is the basic intuition behind word2vec and similar methods?

- b (1.5 points): How are those distributed representations of words computed?

For further information, there’s also a short talk by Tomáš Mikolov about word2vec2 and naturally,numerous blogs and articles on this topic. You might also be interested in Mikolov’s original paper: Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean. Efficient estimation of word representations in vector space.arXiv preprint arXiv:1301.3781, 2013.  URL: https://arxiv.org/abs/1301.


#### a) 
The basic intuition is to build a data structure that represents the meaning of words. According to the Webster dictionary "meaning" is: 
- the idea that is represented by a word, phrase, etc. 
- the idea that a person wants to express by using words, signs, etc. 
- the idea that is expressed in a work of writing, art, etc. 

Furthermore it is desired that things like synonyms and context of the word also get stored. For example if we google for "Dell notebook battery size" we would also want to get results for "Dell laptop battery capacity". Even though the word "size" and "capacity" are not the same, they hold the same meaning in this context. The keyword context ist important here. Depending on the sentence and paragraph a word is used two words can be related to each other or not. Looking at "size" and "capacity" again in a different context, "" and "", they are not related to each other. Therefore the meaning of a word is also represented by its neighbor words (distributional similarity). 


#### b) 
A basic approach would be to simply create a discrete representation of a word. For this a boolean vector is utilized that stores information about all words that exist in the dictionary that gets worked on. Each word in the dictionary gets assigned to a position in the vector (preferably in lexicographic order). This is called a "one-hot" representation. Hereby 0 (false) represents that the vector does not represent said word to which the position refers to and 1 (true) represents said word. 

E.g. suppose we have 3 words in our dictionary: conference, hotel and walk. To represent these words in a discrete representation we would require a boolean vector of length 3. "conference" gets assigned to position 0, "hotel" to position 1 and "walk" to position 3. Then the resulting vector representing the word "conference" would look like [1, 0, 0], "hotel" [0, 1, 0] and "conference" [0, 0, 1]. 

The obvious drawback with this format is that each vector holds a reference to all words in the dictionary, even though it only represents a single word itself. This means that the complexity to represent a dictionary with N words is N*N, which is quite bad. 

Another problem is that the amount of words increases continuously and dictionaries and such dictionaries have to be tediously expanded by hand. 

The second approach would be to utilize neighboring words as well (distributional representation). This way the context of a word gets considered as well 