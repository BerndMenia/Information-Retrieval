### Exercise 2 (0.5 / 3 points)
Based on your analyses of last week, we now aim to develop a recommender system that is able to deal with (and model) sequential data as utilized in the RecSys challenge scenario. To get a first overview on how such sequence- or session-awareness could be implemented in a recommender system, please read the following paper by Massimo Quadrana et al.: Massimo Quadrana, Paolo Cremonesi, and Dietmar Jannach.  Sequence-aware recommender systems.ACM Computing Surveys (CSUR), 51(4):66, 2018. URL https://arxiv.org/pdf/1802.08452.pdfPlease answer the following questions based on the paper:
  
- [x] a (0.5 / 0.5 Points): How do the authors characterize the problem tackled by sequence-aware recommender systems?

- [x] b (0 / 0.5 Points): Give a short overview of the different tasks that can be addressed by sequence-aware recommender systems.

- [ ] c (0 / 2 Points): How do the algorithms presented solve the task of computing sequence-aware recommendations? Please shortly characterize the approaches taken.

.....................................................................................................

- a, b) The authors divide the characterization into 4 different categories: 
  - Inputs: Most often a time stamped and ordered list of user actions. Since we are dealing with sequential inputs it is not that much of a problem if the actual user is unknown (i.e. anonymous session). What's important is the sequence itself. This is different in comparison to the traditional matrix completion setup in which each action is assigned to a specific user. In other words sequence-aware systems can work well with incomplete data. 
  
    Each action that the user takes corresponds to a recommendable item from the database. Furthermore each of those items can be of different types and can hold different attributes. 
    
  - Outputs: Just like the inputs the outputs are also ordered lists of items, and are similar to those of a traditional item ranking recommendation setup. However one major difference is that sometimes the order of the output list does in fact matter. For example if a recommendation system recommends audio books than it may very well be that the recommended audio books are expected to be listened to in a specific order. Also in such a case the user should consider to look at all items in the output list because otherwise the experience would be incomplete. 
  
  - Computational Tasks: As mentioned the order of the input lists of a sequence-aware recommendation matters. A matrix based recommendation system can not distinguish between patterns in the sequence of user inputs. As the name suggests sequence-aware based recommendation systems can handle this task (after all that's part of the reason why they exist). 
  
    Though it is not always the case that the full order of the input list is relevant. Sometimes it is only relevant that we know that a pair of actions occurred together. These are known as co-occurrence patterns. 
    
    Another pattern is to look at the distance between two items in the input list, i.e. how many actions / how much time has passed between some actions. This can be used to remind the user of something through a recommendation. 
    
    
- b) The tasks that can be performed have already been described in a). To summarize sequence-aware recommendation systems can address: Patterns in the input sequence, relation between pairs of items in an input list that are next to each other, relation between pairs of items that are not next to each other (distance, time). 

- c) The authors differentiate between three algorithm types: Sequence Learning, Sequence-Aware Matrix Factorization and Hybrids. Though most algorithms are modeled after the Sequence Learning approach. 

  - Sequence Learning: Most useful when analyzed data has a sequential nature. This fits perfectly into sequence based recommender systems and therefore is also most used in that field. The methods used for Sequence learning are Frequent Pattern Mining (FPM), Sequential Pattern Mining and Contiguous Sequential Patterns (CSP). FPM is the most basic approach of thee three and focuses on if two items are present in the same transaction. Sequential Pattern Mining is equal to FPM, but with the difference that the order of the items is not neglectable. These two patterns are similar to the previously mentioned co-occurrence patterns. CSP require that two items appear adjacent to each other, which is similar to the co-occurrence pattern from before. 
  
    Another algorithm for Sequence Learning is Sequence Modeling which takes the time stamps of the items into account. This is not simply used to determine the order of the items in the sequence, but rather to determine the time span between the items / actions in the sequence. Sequence modeling methods for sequence-aware recommendation mainly belong to three categories: Markov Models, Reinforcement Learning (RL) and Recurrent Neural Networks (RNN). 
  
  Other algorithms are Distributed Item Representations and Supervised Learning with Sliding Windows
  
  - Sequence-Aware 