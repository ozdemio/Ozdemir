import os

#-----------------------------------------------------------------------------#
# GLOBAL VARIABLES                                                            #
#-----------------------------------------------------------------------------#
#DataFile       = "C:\\Python34\HW1\Ozdemir\\tweets.txt"
DataFile       = "tweet_input" + os.sep + "tweets.txt"
OutputFileName = "tweet_output" + os.sep + "ft1.txt"

#-----------------------------------------------------------------------------#
# FUNCTION 1 :Calculate the total number of times each word has been tweeted. #
#-----------------------------------------------------------------------------#
def WordsTweeted():
    """
    Count the number of words in tweets.txt
    """
    file = open(DataFile,"r+")
    wordcount = {}  # <-- this is a dictionary (key->value pairs)
    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    #------------------------------------------------------------#
    # Loop through all of the words to identify the longest word #
    #------------------------------------------------------------#
    maxWordLen = 0
    for word, count in wordcount.items():
        thisWordLen = len(word)
        if maxWordLen < thisWordLen:
            maxWordLen = thisWordLen

    #--------------------------------------------------------------#
    # Loop through all of the words to identify the longest number #
    #--------------------------------------------------------------#
    maxNumberLen = 0
    for word, count in wordcount.items():
        thisNumberLen = len("%s" % count)
        if maxNumberLen < thisNumberLen:
            maxNumberLen = thisNumberLen

    #--------------------------------------------------------------#
    # Create a list of the words (for sorting purposes)            #
    #--------------------------------------------------------------#
    allWords = [] # this will be a list
    for word in wordcount.keys():
        # iterate over all of the words in the (word->count) dictionary
        allWords.append(word)
    allWords.sort() # this should sort this list in place

    outputLines = []
    for word in allWords:
        count = wordcount[word] # get count associated with each word

        nextLine = "%-*s  % *s\n" % (maxWordLen, word, maxNumberLen, count)
        outputLines.append(nextLine)


    print(os.getcwd())
    outputFile = open(OutputFileName, "w+")
    outputFile.writelines(outputLines)
    outputFile.close()

def main():
    WordsTweeted()
    
#-----------------------------------------------------------------------------#
# code execution will start by calling the main funcion on the following line #
#-----------------------------------------------------------------------------#
main()
