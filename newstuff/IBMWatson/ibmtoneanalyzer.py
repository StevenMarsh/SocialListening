from watson_developer_cloud import ToneAnalyzerV3
import simplejson as json
# from JSONtoTXT import cleanJSON
# import JSONtoTXT
import sqlite3

def main():
    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        iam_apikey='oMsOr-VXaaNU9V5D9Pg0AXrC99jK1gJ4t1DGtgjfuKu7',
        url='https://gateway.watsonplatform.net/tone-analyzer/api'
    )
    text = ""
    try:
        conn = sqlite3.connect("../sentdex/twitter.db") #relative path to twitter database
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
    with open("IBM.json", "w") as outfile: #writing data to IBM.json
        json.dump(tone_analysis, outfile, indent=2)

    cleanJSON("text.txt")
    # print(json.dumps(tone_analysis, indent=2))


def cleanJSON(outputFile): # json derulo a.k.a name of json file inpout
    with open("IBM.json") as data_file:
        data = json.load(data_file)

    output = open(outputFile, "w")
    output.write("Document Tones\n")
    overallTones=[] #instantiating index of sentiments
    tones=[] #instantiating list of each tweet sentiment
    tweetText=[] #instantiating list of tweet content
    counter=0 #instantiating counter
    toneCounter=[]#instantiating list keeping track of how many tweets in each sentiment
    tonedCounter=0 #instantiating counter of tweets with sentiment
    toneScores=[] #instantiating list containing scores of each sentiment

    for x in data["document_tone"]["tones"]:
        output.write("\t" + x["tone_name"] + ": " + str(x["score"]))
        output.write("\n")

    # output.write("\nIndividual Sentences with Tone Analysis\n")
    for y in data["sentences_tone"]:
        tones.append([]) #append a new list to tones for this tweet
        toneScores.append([])
        tweetText.append(str(y["text"]))#appending tweet text to list
        if not y["tones"]: #if no sentiments for this tweet
            tones[counter].append("NONE") #append NONE to the tones list
            toneScores[counter].append("NONE")
        else:#if sentiments attached to tweet
            tonedCounter = tonedCounter + 1 #add one to the tonedCounter variable
            for n in y["tones"]:#going through all tones
                if(not(n["tone_name"] in overallTones)): #if the tone doesn't appear in overallTones
                    overallTones.append(n["tone_name"])  #appending tone name to overallTones
                    toneCounter.append(1) #appending 1 to toneCounter list

                tones[counter].append(n["tone_name"]) #appending the tone name to tones list
                toneScores[counter].append(n["score"]) #appending score to toneScores list
                toneCounter[overallTones.index(n["tone_name"])]=toneCounter[overallTones.index(n["tone_name"])]+1 #adding one to the appropriate toneCounter list

                # output.write("\t" + n["tone_name"] + ": " + str(n["score"]) + "\n")

        counter+=1#adding one to counter

    #writing to file
    output.write("Number of tweets: "+str(tonedCounter)) #printing number of tweets

    output.write("\nOverall Tones\n")

    output.write("\nMajor Themes:\n") #writing sentiments + ratio related to all tweets
    for i in range(0,len(overallTones)):
        output.write(overallTones[i]+" (")
        output.write(str(round(toneCounter[i]/tonedCounter*100,2))+"%)\n") #printing ratio

    output.write("\n")

    #writing each tweet organized by tone
    for each in overallTones: #going through each sentiment
        output.write(each+"\n")
        for i in range(0,len(tones)):
            if(each in tones[i]):#if tone in tones
                output.write("- " +tweetText[i]+ " ") #writing tweet content
                output.write("("+str(toneScores[i][tones[i].index(each)])+")\n\n") #writing score
        output.write("\n\n\n")






main()