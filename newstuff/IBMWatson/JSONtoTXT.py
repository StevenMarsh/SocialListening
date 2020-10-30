import json as json
# from pprint import pprint

def cleanJSON(outputFile): # json derulo a.k.a name of json file inpout
    with open("IBM.json") as data_file:
        data = json.load(data_file)

    output = open(outputFile, "w")
    output.write("Document Tones\n")
    for x in data["document_tone"]["tones"]:
        output.write("\t" + x["tone_name"] + ": " + str(x["score"]))
        output.write("\n")

    output.write("\nIndividual Sentences with Tone Analysis\n")
    for y in data["sentences_tone"]:
        output.write(str(y["sentence_id"] + 1) + ". " + y["text"] + "\n")
        for n in y["tones"]:
            output.write("\t" + n["tone_name"] + ": " + str(n["score"]) + "\n")
tuple

