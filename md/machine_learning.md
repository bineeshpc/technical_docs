Syllabus from different universities
====================================

1 Introduction, linear classification, perceptron update rule 2
Perceptron convergence, generalization 3 Maximum margin classification 4
Classification errors, regularization, logistic regression Problem set 1
out 5 Linear regression, estimator bias and variance, active learning 6
Active learning (cont.), non-linear predictions, kernals Problem set 1
due 7 Kernal regression, kernels Problem set 2 out 8 Support vector
machine (SVM) and kernels, kernel optimization 9 Model selection Problem
set 2 due 10 Model selection criteria Midterm 11 Description length,
feature selection Problem set 3 out 3 days before Lec \#11 12 Combining
classifiers, boosting 13 Boosting, margin, and complexity

14 Margin and generalization, mixture models 15 Mixtures and the
expectation maximization (EM) algorithm 16 EM, regularization,
clustering Problem set 4 due 17 Clustering 18 Spectral clustering,
Markov models Problem set 5 out 19 Hidden Markov models (HMMs) 20 HMMs
(cont.) 21 Bayesian networks 22 Learning Bayesian networks Problem set 5
due 23 Probabilistic inference 24 Current problems in machine learning,
wrap up Exams back

read data files of various formats and visualize characteristics of the
data, perform statistical analyses on multivariate data, develop and
apply pattern classification algorithms to classify multivariate data,
develop and apply regression algorithms for finding relationships
between data variables, develop and apply reinforcement learning
algorithms for learning to control complex systems, write scientific
reports on computational machine learning methods, results and
conclusions.

Algorithmic models of learning. Learning classifiers, functions,
relations, grammars, probabilistic models, value functions, behaviors
and programs from experience. Bayesian, maximum a posteriori, and
minimum description length frameworks. Parameter estimation, sufficient
statistics, decision trees, neural networks, support vector machines,
Bayesian networks, bag of words classifiers, N-gram models; Markov and
Hidden Markov models, probabilistic relational models, association
rules, nearest neighbor classifiers, locally weighted regression,
ensemble classifiers. Computational learning theory, mistake bound
analysis, sample complexity analysis, VC dimension, Occam learning,
accuracy and confidence boosting. Dimensionality reduction, feature
selection and visualization. Clustering, mixture models, k-means
clustering, hierarchical clustering, distributional clustering.
Reinforcement learning; Learning from heterogeneous, distributed, data
and knowledge. Selected applications in data mining, automated knowledge
acquisition, pattern recognition, program synthesis, text and language
processing, internet-based information systems, human-computer
interaction, semantic web, and bioinformatics and computational biology.

Introduction: machine learning problems, types of learning, designing a
learning system Inductive learning: introducing basic concepts by
example (learning semantic networks), general setting for induction
Languages for learning: propositional (attribute-value), relational,
Prolog Hypothesis space: version space learning Divide and conquer
approaches: induction of decision trees, OneR, ID3 Covering strategies:
least general generalization approaches Searching the
generalization/specialization graph Relational Learning and Inductive
Logic Programming Evaluating hypotheses: error-based and MDL evaluation
Bayesian learning Bayesian belief networks Instance-based learning
Analytical (Explanation-Based) Learning Unsupervised learning:
clustering

1\. Introductory Topics 2. Linear Regression and Feature Selection 3.
Linear Classification 4. Support Vector Machines and Artificial Neural
Networks 5. Bayesian Learning and Decision Trees 6. Evaluation Measures
7. Hypothesis Testing 8. Ensemble Methods 9. Clustering 10. Graphical
Models 11. Learning Theory and Expectation Maximization 12. Introduction
to Reinforcement Learning

Gatech university
=================

<http://www.cc.gatech.edu/~simpkins/teaching/gatech/cs4641/summer2012/cs4641-syllabus.html>
This has nice ppts for me

Andrew Ng notes
===============

<http://cs229.stanford.edu/materials.html>

Other notes collection
======================

<http://www.cs.cmu.edu/~yandongl/mlnotes.html>

Data sets
=========

UCI Repository: hmp://www.ics.uci.edu/\~mlearn/MLRepository.html

UCI KDD Archive: hmp://kdd.ics.uci.edu/summary.data.applicaOon.html

Statlib: hmp://lib.stat.cmu.edu/

Delve: hmp://www.cs.utoronto.ca/\~delve/

[DONE]{.done .DONE} Precision and recall and F value {#precision-and-recall-and-f-value}
====================================================

SCHEDULED: &lt;2017-05-09 Tue&gt; This is not correct improve it
tomorrow

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
import random


def simple_criminal_data(total, percentage):
    criminal_number = 0
    for i in range(total):
        value = random.random()
        actual_percentage = float(percentage) / 100
        #print value, actual_percentage, value < actual_percentage
        if value < actual_percentage:
            criminal_number += 1
    return total, criminal_number


def find_criminal_number(total, percentage):
    return total, float(percentage) / 100 * total


if __name__ == '__main__':
    total = 10000
    percentage = 2
    total, criminal_number = simple_criminal_data(total, percentage)
    total, predicted_criminal_number = find_criminal_number(total, percentage)
    print total, criminal_number, predicted_criminal_number
    true_negative = total - criminal_number
    false_positive = 
    false_negative =
    true_positive =


```

What I learned?
===============

Introduction
------------

Supervised learning
-------------------

Bayesian decision theory
------------------------

Non parameteric methods
-----------------------

Decision trees
--------------

ML experiments
--------------

Linear discrimination
---------------------

Multilayer perceptron
---------------------

Parametric and multivariate
---------------------------

Dimensionality reduction
------------------------

Clustering
----------

Kernel machines
---------------

Combining learners
------------------

Reinforcement learning
----------------------

Hidden markov chain
-------------------

Cosine similarity
=================

<http://blog.christianperone.com/2013/09/machine-learning-cosine-similarity-for-vector-space-models-part-iii/>

Model build
===========

TFIDF
=====

[DONE]{.done .DONE} Learn TFIDF {#learn-tfidf}
-------------------------------

SCHEDULED: &lt;2017-10-13 Fri&gt;

What is TFIDF?
<https://stanford.edu/~rjweiss/public_html/IRiSS2013/text2/notebooks/tfidf.html>

We need to start thinking about how to translate collections of texts
into quantifiable phenomena. The easiest way to start is to think about
word frequencies.

Compute Word frequency
----------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
mydoclist = ['Julie loves me more than Linda loves me',
'Jane likes me more than Julie loves me',
'He likes basketball more than baseball']

#mydoclist = ['sun sky bright', 'sun sun bright']

from collections import Counter

for doc in mydoclist:
    tf = Counter()
    for word in doc.split():
        tf[word] +=1
    print tf.items()
```

Making all the vectors in the same vector space
-----------------------------------------------

Let's call this a first stab at representing documents quantitatively,
just by their word counts. But for those of you who are already tipped
off by the "vector" in the vector space model, these aren't really
comparable. This is because they're not in the same vocabulary space.

What we really want is for every document to be the same length, where
length is determined by the total vocabulary of our corpus.

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}

import string #allows for format()

mydoclist = ['Julie loves me more than Linda loves me',
'Jane likes me more than Julie loves me',
'He likes basketball more than baseball']

def build_lexicon(corpus):
    lexicon = set()
    for doc in corpus:
        lexicon.update([word for word in doc.split()])
    return lexicon

def tf(term, document):
  return freq(term, document)

def freq(term, document):
  return document.split().count(term)

vocabulary = build_lexicon(mydoclist)

doc_term_matrix = []
print 'Our vocabulary vector is [' + ', '.join(list(vocabulary)) + ']'

for doc in mydoclist:
    print 'The doc is "' + doc + '"'
    tf_vector = [tf(word, doc) for word in vocabulary]
    tf_vector_string = ', '.join(format(freq, 'd') for freq in tf_vector)
    print "tf_vector in detail", zip(tf_vector, vocabulary)
    print 'The tf vector for Document %d is [%s]' % ((mydoclist.index(doc)+1), tf_vector_string)
    doc_term_matrix.append(tf_vector)

    # here's a test: why did I wrap mydoclist.index(doc)+1 in parens?  it returns an int...
    # try it!  type(mydoclist.index(doc) + 1)

print 'All combined, here is our master document term matrix: '
print doc_term_matrix
```

Normalizing vectors to L2 Norm = 1
----------------------------------

Okay, that seems reasonable enough. If any of you have any experience
with machine learning, what you've just seen is the creation of a
feature space. Now every document is in the same feature space, meaning
that we can represent the entire corpus in the same dimensional space
without having lost too much information. Normalizing vectors to L2 Norm
= 1

Once you've got your data in the same feature space, you can start
applying some machine learning methods; classifying, clustering, and so
on. But actually, we've got a few problems. Words aren't all equally
informative.

If words appear too frequently in a single document, they're going to
muck up our analysis. We want to perform some scaling of each of these
term frequency vectors into something a bit more representative. In
other words, we need to do some vector normalizing.

We don't really have the time to go into the intense math of this. Just
accept for now that we need to ensure that the L2 norm of each vector is
equal to 1. Here's some code that shows how this is done.

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}

import math
import numpy as np

doc_term_matrix = [[2, 0, 1, 0, 0, 2, 0, 1, 0, 1, 1], [2, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1]]  # computed in blocks before

def l2_normalizer(vec):
    denom = np.sum([el**2 for el in vec])
    return [(el / math.sqrt(denom)) for el in vec]

doc_term_matrix_l2 = []
for vec in doc_term_matrix:
    doc_term_matrix_l2.append(l2_normalizer(vec))

print 'A regular old document term matrix: ' 
print np.matrix(doc_term_matrix)
print '\nA document term matrix with row-wise L2 norms of 1:'
print np.matrix(doc_term_matrix_l2)

# if you want to check this math, perform the following:
# from numpy import linalg as la
# la.norm(doc_term_matrix[0])
# la.norm(doc_term_matrix_l2[0])


```

IDF Frequency weighting
-----------------------

Not bad. Without getting too deeply mired into the linear algebra, you
can see immediately that we've scaled down vectors such that each
element is between \[0, 1\], without losing too much valuable
information. You see how it's no longer the case that a term count of 1
is the same value in one vector as another?

Why would we care about this kind of normalizing? Think about it this
way; if you wanted to make a document seem more related to a particular
topic than it actually was, you might try boosting the likelihood of its
inclusion into a topic by repeating the same word over and over and over
again. Frankly, at a certain point, we're getting a diminishing return
on the informative value of the word. So we need to scale down words
that appear too frequently in a document.

IDF frequency weighting

But we're still not there yet. Just as all words aren't equally valuable
within a document, not all words are valuable across all documents. We
can try reweighting every word by its inverse document frequency. Let's
see what's involved in that.

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}

import numpy as np

mydoclist = ['Julie loves me more than Linda loves me',
'Jane likes me more than Julie loves me',
'He likes basketball more than baseball']

def build_lexicon(corpus):
    lexicon = set()
    for doc in corpus:
        lexicon.update([word for word in doc.split()])
    return lexicon

def tf(term, document):
  return freq(term, document)

def freq(term, document):
  return document.split().count(term)

vocabulary = build_lexicon(mydoclist)


def numDocsContaining(word, doclist):
    doccount = 0
    for doc in doclist:
        if freq(word, doc) > 0:
            doccount +=1
    return doccount 

def idf(word, doclist):
    n_samples = len(doclist)
    df = numDocsContaining(word, doclist)
    return np.log(n_samples / 1+df)

my_idf_vector = [idf(word, mydoclist) for word in vocabulary]

print 'Our vocabulary vector is [' + ', '.join(list(vocabulary)) + ']'
print 'The inverse document frequency vector is [' + ', '.join(format(freq, 'f') for freq in my_idf_vector) + ']'


```

TF \* IDF
---------

Now we have a general sense of information values per term in our
vocabulary, accounting for their relative frequency across the entire
corpus. Recall that this is an inverse! The more negative a term, the
more frequent it is.

We're almost there. To get TF-IDF weighted word vectors, you have to
perform the simple calculation of tf \* idf.

Time to take a step back. Recall from linear algebra that if you
multiply a vector of A x B by a vector of A x B, you're going to get a
vector of size A x A, or a scalar. This won't do, since what we want is
a term vector of the same dimensions (1 x number of terms), where each
element has been scaled by this idf weighting. How do we do that in
Python?

We could write the whole function out here, but instead we're going to
show a brief introduction into numpy.

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}

import numpy as np

def build_idf_matrix(idf_vector):
    idf_mat = np.zeros((len(idf_vector), len(idf_vector)))
    np.fill_diagonal(idf_mat, idf_vector)
    return idf_mat

my_idf_vector = [1.609438, 1.386294, 1.609438, 1.386294, 1.609438, 1.609438, 1.386294, 1.386294, 1.386294, 1.791759, 1.791759]
my_idf_matrix = build_idf_matrix(my_idf_vector)

print my_idf_matrix

```

L2 norm = 1
-----------

Awesome! Now we have converted our IDF vector into a matrix of size BxB,
where the diagonal is the IDF vector. That means we can perform now
multiply every term frequency vector by the inverse document frequency
matrix. Then to make sure we are also accounting for words that appear
too frequently within documents, we'll normalize each document such that
the L2 norm = 1. In \[6\]:

doc~termmatrixtfidf~ = \[\]

\#performing tf-idf matrix multiplication for tf~vector~ in
doc~termmatrix~: doc~termmatrixtfidf~.append(np.dot(tf~vector~,
my~idfmatrix~))

\#normalizing doc~termmatrixtfidfl2~ = \[\] for tf~vector~ in
doc~termmatrixtfidf~:
doc~termmatrixtfidfl2~.append(l2~normalizer~(tf~vector~))

print vocabulary print np.matrix(doc~termmatrixtfidfl2~) \# np.matrix()
just to make it easier to look at

set(\['me', 'basketball', 'Julie', 'baseball', 'likes', 'loves', 'Jane',
'Linda', 'He', 'than', 'more'\]) \[\[ 0.57211257 0. 0.28605628 0. 0.
0.57211257

1.  0.24639547 0. 0.31846153 0.31846153\]

\[ 0.62558902 0. 0.31279451 0. 0.31279451 0.31279451 0.26942653 0. 0.
0.34822873 0.34822873\] \[ 0. 0.36063612 0. 0.36063612 0.41868557 0. 0.

1.  0.36063612 0.46611542 0.46611542\]\]

2

Use scikit learn instead of computing this ourselves
----------------------------------------------------

Awesome! You've just seen an example of how to tediously construct a
TF-IDF weighted document term matrix.

Here comes the best part: you don't even have to do this by hand.

Remember that everything in Python is an object, objects take up memory
(and performing actions take up time). Using scikits-learn ensures that
you don't have to worry about the efficiency of all the previous steps.

NOTE: The values you get from the TfidfVectorizer/TfidfTransformer will
be different than what we have computed by hand. This is because
scikits-learn uses an adapted version of Tfidf to deal with
divide-by-zero errors. There is a more in-depth discussion here. In
\[7\]:

from sklearn.feature~extraction~.text import CountVectorizer

count~vectorizer~ = CountVectorizer(min~df~=1) term~freqmatrix~ =
count~vectorizer~.fit~transform~(mydoclist) print "Vocabulary:",
count~vectorizer~.vocabulary\_

from sklearn.feature~extraction~.text import TfidfTransformer

tfidf = TfidfTransformer(norm="l2") tfidf.fit(term~freqmatrix~)

tf~idfmatrix~ = tfidf.transform(term~freqmatrix~) print
tf~idfmatrix~.todense()

Vocabulary: {u'me': 8, u'basketball': 1, u'julie': 4, u'baseball': 0,
u'likes': 5, u'loves': 7, u'jane': 3, u'linda': 6, u'more': 9, u'than':
10, u'he': 2} \[\[ 0. 0. 0. 0. 0.28945906 0. 0.38060387 0.57891811
0.57891811 0.22479078 0.22479078\] \[ 0. 0. 0. 0.41715759 0.3172591
0.3172591

1.  0.3172591 0.6345182 0.24637999 0.24637999\]

\[ 0.48359121 0.48359121 0.48359121 0. 0. 0.36778358

1.  1.  1.  0.28561676 0.28561676\]\]

In fact, you can do this just by combining the steps into one: the
TfidfVectorizer In \[8\]:

from sklearn.feature~extraction~.text import TfidfVectorizer

tfidf~vectorizer~ = TfidfVectorizer(min~df~ = 1) tfidf~matrix~ =
tfidf~vectorizer~.fit~transform~(mydoclist)

print tfidf~matrix~.todense()

\[\[ 0. 0. 0. 0. 0.28945906 0. 0.38060387 0.57891811 0.57891811
0.22479078 0.22479078\] \[ 0. 0. 0. 0.41715759 0.3172591 0.3172591

1.  0.3172591 0.6345182 0.24637999 0.24637999\]

\[ 0.48359121 0.48359121 0.48359121 0. 0. 0.36778358

1.  1.  1.  0.28561676 0.28561676\]\]

And we can fit new observations into this vocabulary space like so: In
\[9\]:

new~docs~ = \['He watches basketball and baseball', 'Julie likes to play
basketball', 'Jane loves to play baseball'\] new~termfreqmatrix~ =
tfidf~vectorizer~.transform(new~docs~) print
tfidf~vectorizer~.vocabulary\_ print new~termfreqmatrix~.todense()

{u'me': 8, u'basketball': 1, u'julie': 4, u'baseball': 0, u'likes': 5,
u'loves': 7, u'jane': 3, u'linda': 6, u'more': 9, u'than': 10, u'he': 2}
\[\[ 0.57735027 0.57735027 0.57735027 0. 0. 0. 0.

1.  1.  1.  1.  \]

\[ 0. 0.68091856 0. 0. 0.51785612 0.51785612

1.  1.  1.  1.  1.  \]

\[ 0.62276601 0. 0. 0.62276601 0. 0. 0. 0.4736296 0. 0. 0. \]\]

Note that we didn't get words like 'watches' in the new~termfreqmatrix~.
That's because we trained the object on the documents in mydoclist, and
that word doesn't appear in the vocabulary from that corpus. In other
words, it's out of the lexicon. Back to the Amazon review texts!
Exercise 2

Apply what you learned by doing it on amazon reviews
----------------------------------------------------

Now it's time for you to try applying what you've learned. Try building
a TF-IDF weighted document term matrix from the list of Amazon
review~text~ strings using the TfidfVectorizer. In \[10\]:

import os import csv

\#os.chdir('*Users/rweiss/Dropbox/presentations/IRiSS2013/text1/fileformats*')

with open('amazon/sociology~2010~.csv', 'rb') as csvfile: amazon~reader~
= csv.DictReader(csvfile, delimiter=',') amazon~reviews~ =
\[row\['review~text~'\] for row in amazon~reader~\]

\#your code here!!!

Centroid
========

Cluster
=======
