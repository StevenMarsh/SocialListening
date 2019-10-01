from textblob import TextBlob


analysis = TextBlob("TextBlob sure looks like it has some interesting features!")
print(dir(analysis))
#translate to spanish
print(analysis.translate(to='es'))
print(analysis.tags)
print(analysis.sentiment)



pos_count = 0
pos_correct = 0

#positive.txt not encoded in utf 8
import io
with io.open("positive.txt","r",encoding='latin-1') as f:
#with open("positive.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity > 0:
            pos_correct += 1
        pos_count +=1


neg_count = 0
neg_correct = 0

with io.open("negative.txt","r",encoding='latin-1') as f:
#with open("negative.txt","r") as f:
    for line in f.read().split('\n'):
        analysis = TextBlob(line)
        if analysis.sentiment.polarity <= 0:
            neg_correct += 1
        neg_count +=1

print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))
#Positive accuracy = 71.11777944486121% via 5332 samples
#Negative accuracy = 55.8702175543886% via 5332 samples
