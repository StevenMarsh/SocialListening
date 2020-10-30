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
            tweetContent=tweetContent.replace(".",";")
            tweetContent=tweetContent.replace("!", ";")
            tweetContent=tweetContent.replace("?", ";")
            tweetContent=tweetContent.replace("\n","")
            text += str(tweetContent + "\n") #tweets array possible TODO changing delimitter

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
    overallTones=[]
    tones=[]
    tweetText=[]
    counter=0
    toneCounter=[]
    tonedCounter=0

    for x in data["document_tone"]["tones"]:
        output.write("\t" + x["tone_name"] + ": " + str(x["score"]))
        output.write("\n")

    # output.write("\nIndividual Sentences with Tone Analysis\n")
    for y in data["sentences_tone"]:
        tones.append([])
        tweetText.append(str(y["text"]))
        # output.write(str(y["sentence_id"] + 1) + ". " + y["text"] + "\n")
        if not y["tones"]:
            tones[counter].append("NONE")
        else:
            for n in y["tones"]:
                tonedCounter=tonedCounter+1
                if(not(n["tone_name"] in overallTones)):
                    overallTones.append(n["tone_name"])
                    toneCounter.append(1)

                tones[counter].append(n["tone_name"])
                toneCounter[overallTones.index(n["tone_name"])]=toneCounter[overallTones.index(n["tone_name"])]+1

                # output.write("\t" + n["tone_name"] + ": " + str(n["score"]) + "\n")

        counter+=1
    output.write("\nOverall Tones\n")

    output.write("\nMajor Themes:\n")
    for i in range(0,len(overallTones)):
        output.write(overallTones[i]+" (")
        output.write(str(round(toneCounter[i]/tonedCounter*100,2))+"%)\n")

    output.write("\n")


    for each in overallTones:
        output.write(each+"\n")
        for i in range(0,len(tones)):
            if(each in tones[i]):
                output.write(tweetText[i]+"\n")
        output.write("\n")






main()