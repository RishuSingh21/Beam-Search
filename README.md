# Beam-Search
The goal of this project is to implement beam search algorithm. First extract a directed weighted graph from a corpus and then perform beam search on this graph to generate the  sentence with highest score.

This project is divided into following 3 tasks:
Task 1: Extract graph from a set of sentences
Task 2: Implement Beam Search on the graph to generate the sentences with max score
Task 3: Discuss the effect of length-normalization module

Tasks in details:

Task 1: Extract graph from a set of sentences.
ExtractGraph.py is used for this task
The sentence dataset locates in “assign1_sentences.txt”. Each line of file is one sentence, 
starting with “<s>”, and end with “</s>”. Punctuations include only “,” and “.” It is easy to obtain 
the words simply by splitting the sentence with white space. Please keep the original lowercase 
and uppercase.
The codes will extract a directed weighted graph from this dataset in the ExtractGraph 
initialization step. Each node represents a word; each edge connecting a head word and a tail 
word means the tail word is the next word of the head word; the edge weight is the probability of 
the next word appearing after head word.
getProb(): This function reads the graph and return the probability of 
the next word appearing after head word.

Task 2: Implement Beam Search on the graph to generate the sentences with max score.
BeamSearch.py is used for this task.
beamSearchV1() implements basic beam search
Pre_words is the existing words in the sentence, and the code will predict next and following 
words to finish the sentence. 
beamK is width of beam.
maxToken is the maximum words of a valid sentence, including the pre_words.
Searched/generated sentence with its score is returned in form of StringDouble. The 
score is defined as:
score(y)  =  logP(y|x) ,
Where y is the sentence, and x is the Pre_words. P(y|x) is the probability of the sentence given 
input Pre_words. I have used Log function to keep the accuracy of computation by replacing 
probability multiplication with log probability sum.


