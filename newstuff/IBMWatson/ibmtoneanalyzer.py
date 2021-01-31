from watson_developer_cloud import ToneAnalyzerV3
import simplejson as json
# from JSONtoTXT import cleanJSON
# import JSONtoTXT
import sqlite3

def IBMToneAnalysis(twitter,reddit,custom):
    if twitter:
        twitterAnalysis()
    if reddit:
        redditAnalysis()
    if custom !="":
        customAnalysis(custom)
def twitterAnalysis():
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        iam_apikey='oMsOr-VXaaNU9V5D9Pg0AXrC99jK1gJ4t1DGtgjfuKu7',
        url='https://gateway.watsonplatform.net/tone-analyzer/api'
    )
    text = ""
    try:
        conn = sqlite3.connect("../sentdex/twitter.db") #relative path to twitter database #TODO correct?
        c = conn.cursor()
        c.execute("SELECT tweet FROM sentiment")
        tweets = c.fetchall()  #tailor size
        for tweet in tweets:
            tweetContent=str(tweet[0])
            tweetContent=tweetContent.replace(".",";") #replacing punctuation with a semicolon
            tweetContent=tweetContent.replace("!", ";")
            tweetContent=tweetContent.replace("?", ";")
            tweetContent=tweetContent.replace("\n","")
            text += str(tweetContent + "\n") #adding to text file

    except Exception as e:
        print(str(e))

    print("printing text")
    print(text)

    tone_analysis = tone_analyzer.tone(
        {'text': text},
        'application/json'
    ).get_result()

    # jsonDict = json.dumps(tone_analysis, indent=2)
    with open("twitter.json", "w") as outfile: #writing data to twitter.json
        json.dump(tone_analysis, outfile, indent=2)

    cleanJSON("text.txt","Twitter","twitter.json")
    # print(json.dumps(tone_analysis, indent=2))

def redditAnalysis():
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        iam_apikey='oMsOr-VXaaNU9V5D9Pg0AXrC99jK1gJ4t1DGtgjfuKu7',
        url='https://gateway.watsonplatform.net/tone-analyzer/api'
    )
    text = ""
    try:
        conn = sqlite3.connect("reddit.db") #relative path to twitter database #TODO correct?
        c = conn.cursor()
        c.execute("SELECT tweet FROM sentiment") #TODO change
        posts = c.fetchall()  #tailor size
        for post in posts:
            postContent=str(tweet[0])
            postContent=postContent.replace(".",";") #replacing punctuation with a semicolon
            postContent=postContent.replace("!", ";")
            postContent=postContent.replace("?", ";")
            postContent=postContent.replace("\n","")
            text += str(postContent + "\n") #adding to text file

    except Exception as e:
        print(str(e))

    print("printing text")
    print(text)

    tone_analysis = tone_analyzer.tone(
        {'text': text},
        'application/json'
    ).get_result()

    # jsonDict = json.dumps(tone_analysis, indent=2)
    with open("reddit.json", "w") as outfile: #writing data to reddit.json
        json.dump(tone_analysis, outfile, indent=2)

    cleanJSON("findings.txt","Reddit","reddit.json")
    # print(json.dumps(tone_analysis, indent=2))

def customAnalysis(filename):
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        iam_apikey='oMsOr-VXaaNU9V5D9Pg0AXrC99jK1gJ4t1DGtgjfuKu7',
        url='https://gateway.watsonplatform.net/tone-analyzer/api'
    )
    text = ""
    try:
        c=open(filename,"r")
        lines = c.fetchall()  # tailor size #TODO change
        for line in lines:
            lineContent = str(tweet[0])
            lineContent = lineContent.replace(".", ";")  # replacing punctuation with a semicolon
            lineContent = lineContent.replace("!", ";")
            lineContent = lineContent.replace("?", ";")
            lineContent = lineContent.replace("\n", "")
            text += str(lineContent + "\n")  # adding to text file

    except Exception as e:
        print(str(e))

    print("printing text")
    print(text)

    tone_analysis = tone_analyzer.tone(
        {'text': text},
        'application/json'
    ).get_result()

    # jsonDict = json.dumps(tone_analysis, indent=2)
    with open("custom.json", "w") as outfile:  # writing data to custom.json
        json.dump(tone_analysis, outfile, indent=2)

    cleanJSON("text.txt", "Reddit", "reddit.json")
    # print(json.dumps(tone_analysis, indent=2))


def cleanJSON(outputFile,platform,filename): # json derulo a.k.a name of json file inpout
    with open(filename) as data_file:
        data = json.load(data_file)

    sentiments=dict()
    length=0
    output = open(outputFile, "w")
    output.write(platform+":\n\n")
    # output.write("Document Tones\n")
    # overallTones=[] #instantiating index of sentiments
    # tones=[] #instantiating list of each tweet sentiment
    # tweetText=[] #instantiating list of tweet content
    # counter=0 #instantiating counter
    # toneCounter=[]#instantiating list keeping track of how many tweets in each sentiment
    # tonedCounter=0 #instantiating counter of tweets with sentiment
    # toneScores=[] #instantiating list containing scores of each sentiment

    # for x in data["document_tone"]["tones"]:
    #     output.write("\t" + x["tone_name"] + ": " + str(x["score"]))
    #     output.write("\n")

    # output.write("\nIndividual Sentences with Tone Analysis\n")
    for y in data["sentences_tone"]:
        if y["tones"]:
            length+=1
        for n in y["tones"]:
            if n["tone_name"] in sentiments:
                sentiments[n["tone_name"]][y["text"]]=n["score"]
            else:
                sentiments[n["tone_name"]]=dict()
                sentiments[n["tone_name"]][y["text"]]=n["score"]
        # tones.append([]) #append a new list to tones for this tweet
        # toneScores.append([])
        # tweetText.append(str(y["text"]))#appending tweet text to list
        # if not y["tones"]: #if no sentiments for this tweet
        #     tones[counter].append("NONE") #append NONE to the tones list
        #     toneScores[counter].append("NONE")
        # else:#if sentiments attached to tweet
        #     tonedCounter = tonedCounter + 1 #add one to the tonedCounter variable
        #     for n in y["tones"]:#going through all tones
        #         if(not(n["tone_name"] in overallTones)): #if the tone doesn't appear in overallTones
        #             overallTones.append(n["tone_name"])  #appending tone name to overallTones
        #             toneCounter.append(1) #appending 1 to toneCounter list
        #
        #         tones[counter].append(n["tone_name"]) #appending the tone name to tones list
        #         toneScores[counter].append(n["score"]) #appending score to toneScores list
        #         toneCounter[overallTones.index(n["tone_name"])]=toneCounter[overallTones.index(n["tone_name"])]+1 #adding one to the appropriate toneCounter list
        #
        #         # output.write("\t" + n["tone_name"] + ": " + str(n["score"]) + "\n")
        #
        # counter+=1#adding one to counter

    #writing to file
    output.write("Number of tweets: "+str(length)+"\n") #printing number of tweets

    output.write("\nMajor Themes:\n") #writing sentiments + ratio related to all tweets
    for i in sentiments.keys():
        output.write(i +" (")
        output.write(str(round((len(sentiments[i].keys())/length)*100))+"%)\n") #printing ratio

    output.write("\n\n")
    for j in sentiments.keys():
        output.write(j+":\n")
        for each in sentiments[j].keys():
            output.write("- "+each+" ("+str(sentiments[j][each])+")\n\n")
        output.write("\n")


    #writing each tweet organized by tone
    # for each in overallTones: #going through each sentiment
    #     output.write(each+"\n")
    #     for i in range(0,len(tones)):
    #         if(each in tones[i]):#if tone in tones
    #             output.write("- " +tweetText[i]+ " ") #writing tweet content
    #             output.write("("+str(toneScores[i][tones[i].index(each)])+")\n\n") #writing score
    #     output.write("\n\n\n")






