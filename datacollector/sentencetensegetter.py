
'''This class checks and computes verbs tags in sentences'''

import os
from nltk.parse import stanford
from nltk.tag.stanford import StanfordPOSTagger

class SentenceTenseGetter:
    def  __init__(self):
       java_path = "/Library/Java/JavaVirtualMachines/jdk1.8.0_72.jdk/Contents/Home/bin/java"
       os.environ['JAVAHOME'] = java_path
       #self.grammarlocation = grammarlocation
    
    def getAllVerbs(self, sentence):
        verbTags = ["VBZ","VBP","VBD"]
        taggedVerbs = []
        path_to_model = '/Users/hospicehoungbo/Downloads/stanford-postagger-2018-10-16/models/english-bidirectional-distsim.tagger'
        path_to_jar = "/Users/hospicehoungbo/Downloads/stanford-postagger-2018-10-16/stanford-postagger-3.9.2.jar"
        tagger=StanfordPOSTagger(path_to_model, path_to_jar)
        tagger.java_options='-mx4096m'          ### Setting higher memory limit for long sentences
        tags = tagger.tag(sentence.split())
        for pair in tags:
            if pair[1] in verbTags:
                taggedVerbs.append(pair[1])
        return taggedVerbs
   
    def hasVerbs(self, taggedVerbs):
        if len(taggedVerbs)==0:
            return False
        return True
        
    def builInstance(self, sentence):
        taggedVerbs = self.getAllVerbs(sentence)
        if "VBZ" or "VBP" in taggedVerbs:# | "VBP" in taggedVerbs:
            sentence = sentence+","+"true"
        else:
            sentence = sentence+","+"false"
        if "VBD" in taggedVerbs:
            sentence = sentence+","+"true"
        else:
            sentence = sentence+","+"false"
        return sentence    

sentence =  "Microarray and other high-throughput tchnologies have led to an explosion in the rate of molecular abundance data generated in hte last decade."
def test():
    stg = SentenceTenseGetter()

    #sentList = ("Hello, My name is Melroy.", "What is your name?")

    sentParsed = stg.getAllVerbs(sentence)
    print(sentParsed)

def test1():
    stg = SentenceTenseGetter()
    #sentList = ("Hello, My name is Melroy.", "What is your name?")
    instance = stg.builInstance(sentence)
    print(instance)

if __name__ =="__main__":
    test()
    test1()

