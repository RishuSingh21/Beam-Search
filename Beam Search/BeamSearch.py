import StringDouble
import ExtractGraph
import math
import Beam

class BeamSearch:

    graph = []
    best_string = ""
    def __init__(self, input_graph):
        self.graph = input_graph
        return

    def prob_fn(self,head_word):
        prob_list = []
        tail_word_list = self.graph.graph[head_word[-1]]
        for word in tail_word_list.keys():
            prob = self.graph.getProb(head_word[-1],word)
            prob_list.append((prob,word))
        return prob_list

    def beamSearchV1(self, pre_words, beamK, maxToken):
    	# Basic beam search.
        #basic beam search is a normalization search with parameter lambda value =0
        return self.beamSearchV2(pre_words,beamK,0,maxToken)

    def beamSearchV2(self, pre_words, beamK, param_lambda, maxToken):
    	# Beam search with sentence length normalization.
        prev_beam = Beam.Beam(beamK)
        #prev_beam.add(math.log(1.0), False, ['<s>'])
        word_list = pre_words.split(" ")
        list=[]
        #Creating a list to store the words from pre_words
        for words in word_list:
            list.append(words)
        prev_beam.add(math.log(1.0), False, list) #appending prev_beam with the words of pre_wpords
        while True:
            curr_beam = Beam.Beam(beamK)
            #Add complete sentences that do not yet have the best probability to the current beam, the rest prepare to add more words to them.
            for (prefix_prob, complete, prefix) in prev_beam:
                #print(prefix_prob)
                if complete == True:
                    curr_beam.add(prefix_prob, True, prefix)
                else:
                    #prob_fn is a function to create a list of all the tail words along with their probabilities of apprearing next to a given head word
                    for (next_prob, next_word) in self.prob_fn(prefix):
                        if next_word == '</s>':  # if next word is the end token then mark prefix as complete and leave out the end token
                            prefix_prob = (prefix_prob + math.log(next_prob))/math.pow(len(prefix)+1, param_lambda)
                            curr_beam.add(prefix_prob, True, prefix)
                        else:  # if next word is a non-end token then mark prefix as incomplete
                            prefix_prob = (prefix_prob + math.log(next_prob))/math.pow(len(prefix)+1, param_lambda)
                            curr_beam.add(prefix_prob, False, prefix + [next_word])
            (best_prob, best_complete, best_prefix) = max(curr_beam)
            if best_complete == True or len(best_prefix) - 1 == maxToken:  # if most probable prefix is a complete sentence or has a length that exceeds the maxToken (ignoring the start token) then return it
                best_string = ""
                for word in best_prefix[1:]:
                    best_string = best_string+" "+word
                t = StringDouble.StringDouble(best_string,best_prob)  # return best sentence without the start token and together with its probability
                return(t)
            prev_beam = curr_beam
