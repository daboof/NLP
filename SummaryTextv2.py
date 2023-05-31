import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

text = """Farming efficiency is one of the most important factors determining profitability and viability in general of the agribusiness. The aim of this paper is to analyze the dynamics of efficiency in Lithuanian family farms by the means of the bootstrapped Data Envelopment Analysis in order to propose certain guidelines for inefficiency mitigation. Stochastic kernels are then employed to estimate densities of the efficiency scores for different farming types. The research covers years 2004– 2009 and is based on farm-level Farm Accountancy Data Network (FADN) data. The stochastic kernel for livestock farms exhibited a small range of efficiency scores. Therefore, these farms achieved a higher convergence as well as a higher average TE from the standpoint of the analyzed farming types. The mixed farms, though, were peculiar both a sort of bi-modal distribution of their efficiency scores. """

stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

freqTable = dict()

for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

average = int(sumValues / len(sentenceValue))

summary = ''

for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence

print(summary)


