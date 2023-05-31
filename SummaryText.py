import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
import string
import matplotlib.pyplot as plt
import sklearn.feature_extraction
from sklearn.feature_extraction.text import TfidfVectorizer
import rouge
from rouge import Rouge

def calculate_tfidf_scores(texts):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray()
    return feature_names, tfidf_scores

def sentence_scoring(text):
    sentences = sent_tokenize(text)
    word_scores = {}

    # Compute TF-IDF scores for words
    feature_names, tfidf_scores = calculate_tfidf_scores([text])
    for word, score in zip(feature_names, tfidf_scores[0]):
        word_scores[word] = score

    sentence_scores = {}

    # Compute scores for each sentence
    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        score = sum(word_scores.get(word, 0) for word in words) / len(words)
        sentence_scores[sentence]=score

    # Sort sentences based on scores in descending order
#     sentence_scores.sort(key=lambda x: x[1], reverse=True)

    return sentence_scores

#function to find key from dictvalue
def findkey(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None  # Value not found

text='''Incorporating cloud computing into heterogeneous networks, the heterogeneous cloud radio access network (H-CRAN) has been proposed as a promising paradigm to enhance both spectral and energy efficiencies. Developing interference suppression strategies is critical for suppressing the inter-tier interference between remote radio heads (RRHs) and a macro base station (MBS) in H-CRANs. In this paper, inter-tier interference suppression techniques are considered in the contexts of collaborative processing and cooperative radio resource allocation (CRRA). In particular, interference collaboration (IC) and beamforming (BF) are proposed to suppress the inter-tier interference, and their corresponding performance is evaluated. Closed-form expressions for the overall outage probabilities, system capacities, and average bit error rates under these two schemes are derived. Furthermore, IC- and BF-based CRRA optimization models are presented to maximize the RRH-accessed users' sum rates via power allocation, which is solved with convex optimization. Simulation results demonstrate that the derived expressions for these performance metrics for IC and BF are accurate, and the relative performance between IC and BF schemes depends on system parameters such as the number of antennas at the MBS, the number of RRHs, and the target signal-to-interference-plus-noise ratio threshold. Furthermore, it is seen that the sum rates of IC and BF schemes increase almost linearly with the transmit power threshold under the proposed CRRA optimization solution.
'''
text=text.lower()
text = ' '.join([word for word in text.split() if word not in (stopwords.words('english'))])

text=text.lower()
text = ' '.join([word for word in text.split() if word not in (stopwords.words('english'))])
sents=sent_tokenize(text)

freqdict=sentence_scoring(text)

scoreset=[]
for sent in sents:
    scoreset.append(freqdict[sent])
scoreset=sorted(scoreset,reverse=True)

summaryset=[]
for i in scoreset:
    summaryset.append(findkey(freqdict,i))
summaryfinal=' '.join(summaryset)

rouge=Rouge()
scores=rouge.get_scores(text,summaryfinal)

print("original abstract:  "+text+'\n')
print("summarized :  "+summaryfinal+'\n')
print("rouge scores:  ")
print(scores)

