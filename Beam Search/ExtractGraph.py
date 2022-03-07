import StringDouble
class ExtractGraph:

    # key is head word; value stores next word and corresponding probability.
    graph = {}
    sentences_add = "data/assign1_sentences.txt"

    def __init__(self):
        # Extract the directed weighted graph, and save to {head_word, {tail_word, probability}}
        self.graph={}
        
        #opening assign1_sentences.txt file and reading it line by line
        with open(self.sentences_add) as f:
            for line in f:
                line = line.replace("\n","") #replacing \n
                wordlist = line.split(" ")
                
                #since we have replaced \n with "", we have an entry with "" in our wordlist and thats why we need to remove it
                if "" in wordlist:
                    wordlist.remove("")
                    
                #for every line we are iterating to every word in it and creating/modifying dictionary entry    
                for i in range(0,len(wordlist)-1):
                    head_word = wordlist[i]
                    tail_word = wordlist[i+1]
                    if head_word in self.graph.keys():
                        tail_word_list = self.graph[head_word]
                        
                        # Case1: Head word and tail word both are in the graph
                        if tail_word in tail_word_list:
                            count = tail_word_list[tail_word]+1
                            self.graph[head_word][tail_word]=count
                        #Case2: Head word is in the graph but tail word is not
                        else:
                            self.graph[head_word][tail_word]=1
                    # Case3: Head word and tail word both are not in the graph
                    else:
                        self.graph[head_word]={}
                        self.graph[head_word][tail_word]=1
        return
            
    def getProb(self,head_word,tail_word):
        if head_word in self.graph.keys():
            tail_word_list = self.graph[head_word]
            head_word_count = 0
            if tail_word in tail_word_list.keys():  
                for word in tail_word_list:
                    head_word_count = tail_word_list[word]+head_word_count
                tail_word_count = tail_word_list[tail_word]
                prob = tail_word_count/head_word_count
                self.graph[head_word][tail_word]=prob
                return prob
            else:
                return 0.0
        else:
            return 0.0

