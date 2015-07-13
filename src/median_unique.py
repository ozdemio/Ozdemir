import os

#-----------------------------------------------------------------------------#
# GLOBAL VARIABLES                                                            #
#-----------------------------------------------------------------------------#
DataFile       = "tweet_input" + os.sep + "tweets.txt"
OutputFileName = "tweet_output" + os.sep + "ft2.txt"

#-----------------------------------------------------------------------------#
# FUNCTION 2 : Calculate the median number of unique words per tweet and,     #
#              update this median as tweets come in.                          #
#-----------------------------------------------------------------------------#

def MedianUnique():
    """
    Count the number of words in tweets.txt
    """
    file = open(DataFile,"r+")
    wordcount = {}  # <-- this is a dictionary (key->value pairs)
    rawData  = file.read() # one big string of data
    rawLines = rawData.split("\n") # list of lines 

    #---------------------------------------#
    # Iterate line by line (tweet-by-tweet) #
    #---------------------------------------#
    outputLines  = [] # for capturing strings to be written
    nUniqueWords = [] # list of number of unique words (per tweet)
    for ctr, tweet in enumerate(rawLines):
        uniqueWordsInTweet = {} # create a new empty dict. for each tweet

        #-------------------------------------------------------------#
        # iterate through all of the words, identify unique instances #
        #-------------------------------------------------------------#
        for word in tweet.split():
            # the value doesn't matter we just need to keep track of
            # all the unique keys of the key->value pairs.
            uniqueWordsInTweet[word] = None

        listOfWords = uniqueWordsInTweet.keys()
        uniqueCount = len(listOfWords)
        nUniqueWords.append(uniqueCount)

        #----------------------------------#
        # sort the numbers of unique words #
        #----------------------------------#
        nUniqueWords.sort()

        #---------------------------------------------------------#
        # Calculate the updated median value                      #
        #---------------------------------------------------------#
        # First determine if there are an even or odd # of values #
        #---------------------------------------------------------#
        isOdd = False
        if len(nUniqueWords)%2 == 1:
            # if dividing by two has a remainder then this is an odd # of tweets
            isOdd = True

        median = 0.0
        if ctr == 0:
            median = uniqueCount
        elif isOdd:
            # the resulting value will be an average of the two middle numbers
            ind0 = int(len(nUniqueWords)/2)
            ind1 = ind0 + 1
            median = (nUniqueWords[ind0] + nUniqueWords[ind1])/2.0
        else:
            ind0 = int(len(nUniqueWords)/2)
            median = nUniqueWords[ind0]           
            
        nextLine = "%s\n" % (median)
        outputLines.append(nextLine) # add the line to the list



    print(os.getcwd())
    outputFile = open(OutputFileName, "w+")
    outputFile.writelines(outputLines)
    outputFile.close()
      

def main():
    MedianUnique()

#-----------------------------------------------------------------------------#
# code execution will start by calling the main funcion on the following line #
#-----------------------------------------------------------------------------#
main()
