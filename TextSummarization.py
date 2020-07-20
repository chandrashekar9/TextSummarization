import spacy
from spacy.lang.en.stop_words import STOP_WORDS
document1="'Web development is the work involved in developing a web site for the Internet (World Wide Web) or an intranet (a private network).[1] Web development can range from developing a simple single static page of plain text to complex web-based internet applications (web apps), electronic businesses, and social network services. A more comprehensive list of tasks to which web development commonly refers, may include web engineering, web design, web content development, client liaison, client-side/server-side scripting, web server and network security configuration, and e-commerce development.Among web professionals, web development usually refers to the main non-design aspects of building web sites: writing markup and coding.[2] Web development may use content management systems (CMS) to make content changes easier and available with basic technical skills.For larger organizations and businesses, web development teams can consist of hundreds of people (web developers) and follow standard methods like Agile methodologies while developing websites. Smaller organizations may only require a single permanent or contracting developer, or secondary assignment to related job positions such as a graphic designer or information systems technician. Web development may be a collaborative effort between departments rather than the domain of a designated department. There are three kinds of web developer specialization: front-end developer, back-end developer, and full-stack developer. Front-end developers responsible for behavior and visuals that run in the user browser, while back-end developers deal with the servers."
print(document1)
stopwords = list(STOP_WORDS)
print(stopwords)
len(stopwords)
nlp = spacy.load('en')
docx= nlp(document1)
for token in docx:
    print(token.text)
word_frequencies = {}
for word in docx:
    if word.text not in word_frequencies.keys():
        word_frequencies[word.text] = 1
        
    else:
            word_frequencies[word.text]+=1
word_frequencies
maximum_frequency = max(word_frequencies.values())
maximum_frequency
sentence_list = [sentence for sentence in docx.sents]
sentence_scores = {}
for sent in sentence_list:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if len(sent.text.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]
 sentence_scores
 ### find top N sentences with largest score
from heapq import nlargest
summarized_sentences = nlargest(5,sentence_scores,key=sentence_scores.get)
summarized_sentences
final_sentences = [ w.text for w in summarized_sentences ]
summary = ' '.join(final_sentences)
summary
len(document1)
len(summary)
