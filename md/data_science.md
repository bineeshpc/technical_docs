---
startup: inlineimages 
---

Data science
============

General Plan
------------

<https://datascience.stackexchange.com/questions/6937/what-courses-subjects-are-most-important-to-the-field-of-data-science>
<https://github.com/mjbahmani/10-steps-to-become-a-data-scientist>

Fundamentals
------------

### Matrices and linear algebra fundamentals

<file:mathematics.org>

### Hash functions Binary Tree O(n)

### Relational algebra, DB basics

expand on this. joins division etc

``` {.bash}
binisearch.py -o 'relational algebra'
```

### Inner outer cross Theta join

### Cap theorem

### Tabular data

### Entropy

<https://towardsdatascience.com/demystifying-entropy-f2c3221e2550>

``` {.bash}
binisearch.py -o 'entropy data science'
binisearch.py -o 'entropy information theory'
```

### Data frames and series

### Sharding

``` {.bash}
binisearch.py -o 'sharding'
```

### Online analytical processing OLAP

<https://en.wikipedia.org/wiki/Online_analytical_processing>

``` {.bash}
binisearch.py -o 'OLAP data science'
```

### Multidimensional data model

``` {.bash}
binisearch.py -o 'Multidimensional data model'
```

A multidimensional database (MDB) is a type of database that is
optimized for data warehouse and online analytical processing (OLAP)
applications. Multidimensional databases are frequently created using
input from existing relational databases. Whereas a relational database
is typically accessed using a Structured Query Language (SQL) query, a
multidimensional database allows a user to ask questions like "How many
Aptivas have been sold in Nebraska so far this year?" and similar
questions related to summarizing business operations and trends. An OLAP
application that accesses data from a multidimensional database is known
as a MOLAP (multidimensional OLAP) application.

### ETL

``` {.bash}
binisearch.py -o ETL
```

### Reporting vs BI vs Analytics

``` {.bash}
binisearch.py -o Reporting
binisearch.py -o 'Business intelligence'
binisearch.py -o Analytics
```

### JSON and XML

``` {.bash}
binisearch.py -o json
binisearch.py -o xml

```

### NOSQL

``` {.bash}
binisearch.py -o nosql


```

### Regex

``` {.bash}
binisearch.py -o 'regular expression'
```

### Vendor landscape

``` {.bash}
binisearch.py -o 'vendor landscape'
```

### Environment setup

Statistics
----------

<file:DataScience/statistics.org>

### Pick a data set(UCI repo)

``` {.bash}
binisearch.py -o 'datasets for data science'
```

### Descriptive statistics[]{.tag data-tag-name="drill"}

SCHEDULED: &lt;2018-12-08 Sat&gt;

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}

import sys
sys.path.append('/home/bineesh/problemsolving/problemsolving/bin')
from binisearch import Research

s = """Mean
median
Range
Standard Deviation
variance"""


for i in s.split('\n'):
    r = Research(i, '')
    r.openbrowser()

```

1.  Mean

    Average

    ``` {.python}
    import numpy as np

    values = range(1, 11)
    num_values = len(values)
    mean = float(sum(values)) / num_values
    print(values)
    print(num_values)
    print(sum(values))
    print(mean)


    def get_mean(values):
        num_values = len(values)
        mean = float(sum(values)) / num_values
        return mean



    def test_get_mean():
        epsilon = 0.0000001
        assert (np.mean(values) - get_mean(values)) < epsilon

    test_get_mean()
    ```

2.  Median

    Arrange everything in sorted order if len(s) is odd then the middle
    item

    if len(s) is even then the mean of two middle items

    ``` {.python}


    def get_mean(values):
        num_values = len(values)
        mean = float(sum(values)) / num_values
        return mean


    def get_median(values):
        num_values = len(values)
        values_sorted = sorted(values)
        middle = int(num_values / 2)
        if num_values == 0:
            return None
        if num_values == 1:
            return values[0]

        if num_values % 2 == 0:
            return get_mean([values[middle], values[middle-1]])
        else:
            return values[middle]



    even_length_values = range(3, 4)
    odd_length_values = range(1, 3)

    print(get_median(even_length_values))
    print(get_median(odd_length_values))
    ```

3.  Mode

    The value that appears most often

    ``` {.python .rundoc-block rundoc-language="python" rundoc-results="output" rundoc-exports="both"}
    import sys

    def get_mode(values):
        """ return multiple modes in the values iterable """
        count_dict = {}
        for i in values:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        modes = []
        max_value = -sys.maxsize # -infinity
        for i in count_dict:
            count = count_dict[i]
            if count > max_value:
                max_value = count

        for key in count_dict:
            count = count_dict[key]
            if count == max_value:
                modes.append(key)

        return modes

    values = list(range(1, 10)) + list(range(1, 5))


    print(get_mode(values))

    ```

    ```

4.  Variance

    ``` {.python}
    import math



    def get_mean(values):
        num_values = len(values)
        mean = float(sum(values)) / num_values
        return mean

    def square(x):
        return x * x

    def get_variance(values):
        mean = get_mean(values)
        s = 0
        for xi in values:
            s += square(xi - mean)

        return s / len(values)

    def get_std(values):
        return math.sqrt(get_variance(values))


    values = list(range(1, 3))
    print(get_variance(values), get_std(values))
    ```

5.  Standard deviation

    how much the members differ from the mean value of the group Refer
    variance section

### Exploratory data analysis

``` {.bash}
binisearch.py -o 'exploratory data analysis'
```

### Histograms

``` {.bash}
binisearch.py -o histogram
```

### Percentiles and outliers[]{.tag data-tag-name="drill"} {#percentiles-and-outliers id="b698f3a3-85eb-4c09-9926-4c7636dd3a72"}

1.  Percentile

    ``` {.bash}
    binisearch.py -o percentile
    ```

    If all you are interested in is where you stand compared to the rest
    of the herd, you need a statistic that reports relative standing,
    and that statistic is called a percentile. The kth percentile is a
    value in a data set that splits the data into two pieces: The lower
    piece contains k percent of the data, and the upper piece contains
    the rest of the data (which amounts to \[100 – k\] percent, because
    the total amount of data is 100%). Note: k is any number between 0
    and 100.

    ``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
    import numpy as np
    values = range(1, 1000)
    print(np.percentile(values, [5, 10, 95]))
    ```

2.  Outlier

    ``` {.bash}
    binisearch.py -o outlier
    ```

    1.  Outlier

        In statistics, an outlier is an observation point that is
        distant from other observations. An outlier may be due to
        variability in the measurement or it may indicate experimental
        error; the latter are sometimes excluded from the data set. An
        outlier can cause serious problems in statistical analyses. ‎O

### Probability theory

``` {.bash}
binisearch.py -o 'probability theory'
```

### Bayes theorem

``` {.bash}
binisearch.py -o 'bayes theorem'
```

### Random variables

``` {.bash}
binisearch.py -o 'random variables'
```

### Cumulative distribution function(CDF)

``` {.bash}
binisearch.py -o 'cumulative distribution function'
```

### Continous distributions

Normal, Poisson, Gaussian

``` {.bash}
binisearch.py -o 'normal distribution'
binisearch.py -o 'poisson distribution'
binisearch.py -o 'gaussian distribution '
```

### Skewness

``` {.bash}
binisearch.py -o skewness
```

A slant

Positive skew(right skew), mean greater than mode. long tail towards the
right. Negative skew(left skew), mean less than mode. long tail towards
the left.

Normal distribution will be symmetrical

### Analysis of variance ANOVA

``` {.bash}
binisearch.py -o anova
```

### Probability density function

``` {.bash}
binisearch.py -o 'probability density function'
```

<https://en.wikipedia.org/wiki/Probability_density_function>

Value of a continous random variable described as a funtion. Typically
plotted with boxplot.

mean +- std

Area under a particular region represents the probability of occurance
in that particular range

Cumulative distribution function is the area under probability
distribution function from -infinity to x.

x1 point of cdf - x2 point of cdf gives us the probability of value
falling in range x1 and x2

### Central limit theorem

``` {.bash}
binisearch.py -o 'central limit theorem'
```

In probability theory, the central limit theorem (CLT) establishes that,
in some situations, when independent random variables are added, their
properly normalized sum tends toward a normal distribution (informally a
"bell curve") even if the original variables themselves are not normally
distributed. The theorem is a key concept in probability theory because
it implies that probabilistic and statistical methods that work for
normal distributions can be applicable to many problems involving other
types of distributions.

### Monte carlo method

``` {.bash}
binisearch.py -o 'monte carlo method'
```

### Hypothesis testing

``` {.bash}
binisearch.py -o 'hypothesis testing'
```

<https://en.wikipedia.org/wiki/Statistical_hypothesis_testing>

### p value[]{.tag data-tag-name="drill"}

SCHEDULED: &lt;2018-12-08 Sat&gt;

``` {.bash}
binisearch.py -o 'p value'
```

1.  What is P value?

    A small p-value (typically ≤ 0.05) indicates strong evidence against
    the null hypothesis, so you reject the null hypothesis. A large
    p-value (&gt; 0.05) indicates weak evidence against the null
    hypothesis, so you fail to reject the null hypothesis.

### Chi square test[]{.tag data-tag-name="drill"}

SCHEDULED: &lt;2018-12-08 Sat&gt;

``` {.bash}
binisearch.py -o 'chi square test'
```

1.  What is chi square test?

    a statistical method assessing the goodness of fit between a set of
    observed values and those expected theoretically.

    interestingness measure

    c = 0 independent c &gt; 0 correlated either positive or negative
    further test required

    chi square = Sigma \[ square((Oi-Ei)) / Ei \]

    Chi square value should be less than a threshold depending on the
    degrees of freedom of a categorical variable

2.  Test with sympy

        import sympy
        x, y, z = sympy.symbols('x y z')
        sympy.init_printing()
        sympy.Integral(sympy.sqrt(1/x), x)

    ``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}

    import matplotlib.pyplot as plt
    import numpy as np
    plt.hist(np.random.randn(20000), bins=200)
    plt.savefig('abc.png')
    print('file:abc.png')
    ```

    ![](abc.png)

### Degrees of Freedom

In statistics, the number of degrees of freedom is the number of values
in the final calculation of a statistic that are free to vary.

The number of independent ways by which a dynamic system can move,
without violating any constraint imposed on it, is called number of
degrees of freedom. In other words, the number of degrees of freedom can
be defined as the minimum number of independent coordinates that can
specify the position of the system completely.

1.  In some cases(read later)

    Depends on situation.

    Degree of freedom is one less than the number of values possible for
    a categorical variable

    For a coin it is 1 (H, T) cardinality(target set) - 1

    2 - 1 = 1

    Dice (1, 2 ,3 ,4 ,5, 6)

    cardinality((1, 2 ,3 ,4 ,5, 6) )

    is 6 - 1 = 5

### Estimation

``` {.bash}
binisearch.py -o 'statistical estimation'
```

Estimation in Statistics. In statistics, estimation refers to the
process by which one makes inferences about a population, based on
information obtained from a sample.

### Confidence interval (CI)[]{.tag data-tag-name="drill"}

SCHEDULED: &lt;2018-12-08 Sat&gt;

``` {.bash}
binisearch.py -o 'confidence interval'
```

1.  Confidence interval

    In statistics, a confidence interval (CI) is a type of interval
    estimate, computed from the statistics of the observed data, that
    might contain the true value of an unknown population parameter. ...
    Most commonly, the 95% confidence level is used. However, other
    confidence levels can be used, for example, 90% and 99%.

### Maximum likelyhood estimation

``` {.bash}
binisearch.py -o 'maximum likelyhood estimation'
```

In statistics, maximum likelihood estimation (MLE) is a method of
estimating the parameters of a statistical model, given observations.
MLE attempts to find the parameter values that maximize the likelihood
function, given the observations.

### Kernel density estimate

``` {.bash}
binisearch.py -o 'kernel density estimate'
```

In statistics, kernel density estimation (KDE) is a non-parametric way
to estimate the probability density function of a random variable.
Kernel density estimation is a fundamental data smoothing problem where
inferences about the population are made, based on a finite data sample.

### Regression

``` {.bash}
binisearch.py -o regression
```

### Covariance

``` {.bash}
binisearch.py -o covariance
```

Check some scatter plots for covariance matrix Plot it. Check statistics
datacamp 1 , chapter 1

1.  Data frame example

    ``` {.python .rundoc-block rundoc-language="python" rundoc-results="output" rundoc-exports="both"}
    import pandas as pd
    df = pd.DataFrame([(1, 2), (0, 3), (2, 0), (1, 1)],
                       columns=['dogs', 'cats'])

    print(df)
    print(df.cov())
    ```

    ```

### Correlation

``` {.bash}
binisearch.py -o correlation
```

In statistics, dependence or association is any statistical
relationship, whether causal or not, between two random variables or
bivariate data.

Check statistics datacamp 1 , chapter 1

### Pearson coefficient

``` {.bash}
binisearch.py -o 'pearson coefficient'
```

Plot pearson correlation coefficient Check statistics datacamp 1 ,
chapter 1

### Causation

``` {.bash}
binisearch.py -o causation
```

<https://en.wikipedia.org/wiki/Correlation_does_not_imply_causation>

### Least square fit

``` {.bash}
binisearch.py -o 'least square fit'
```

The method of least squares is a standard approach in regression
analysis to approximate the solution of overdetermined systems, i.e.,
sets of equations in which there are more equations than unknowns.
"Least squares" means that the overall solution minimizes the sum of the
squares of the residuals made in the results of every single equation.

A mathematical procedure for finding the best-fitting curve to a given
set of points by minimizing the sum of the squares of the offsets ("the
residuals") of the points from the curve. The sum of the squares of the
offsets is used instead of the offset absolute values because this
allows the residuals to be treated as a continuous differentiable
quantity. However, because squares of the offsets are used, outlying
points can have a disproportionate effect on the fit, a property which
may or may not be desirable depending on the problem at hand.

### Euclidean distance

``` {.bash}
binisearch.py -o 'euclidean distance'
```

<https://en.wikipedia.org/wiki/Euclidean_distance>

Programming
-----------

### Python

### Working in excel

### Rstudio

### R

### Expressions

### Variables

### Vectors

### Matrices

### Arrays

### Factors

### Lists

### Dataframes

### Reading CSV data

### Reading raw data

### Subsetting data

### Manipulate data frames

### Functions

### Factor analysis

``` {.bash}
binisearch.py -o 'factor analysis'
```

### Install packages

Machine learning
----------------

<file:machine_learning.org>

### What is ML?

In traditional programming we decide the rules and we apply those rules
to the data to find the result. In ML we give the data to the program
and the program will give out the rules.

It is a process of learning from data.
<https://developers.google.com/machine-learning/glossary/>

### Numerical variable

``` {.bash}
binisearch.py -o 'numerical variable'
```

A variable with numerical values.

### Categorical variable[]{.tag data-tag-name="drill"}

SCHEDULED: &lt;2018-12-16 Sun&gt;

``` {.bash}
binisearch.py -o 'categorical variable'
```

1.  binary

2.  nominal

    (categories without order-europe, northamerica, africa),

3.  ordinal

    (categories with order - rating from 1 to 10)

### Supervised learning[]{.tag data-tag-name="drill"} {#supervised-learning id="4d99bd91-a965-4864-8998-547c3087dc3a"}

1.  What is supervised learning?

    We have labelled data. We learn from this labeled data. We usually
    split the data into train data and test data. We train the model on
    the train data. We test the data on the test data.

    train test split train on train data test on test data

### Unsupervised learning[]{.tag data-tag-name="drill"}

SCHEDULED: &lt;2018-12-09 Sun&gt;

We learn the pattern from the data

### Concepts inputs and attributes

``` {.bash}
binisearch.py -o 'inputs machine learning'
binisearch.py -o 'attributes machine learning'
```

### Training and Test data

1.  Definition

    We often split our labelled data to train data and split data we
    train on the train data and test on the test data

### Classifier[]{.tag data-tag-name="drill"} {#classifier id="db86c8bb-3974-4c0e-b66d-1807ca2b3cf1"}

1.  What is classification?

    <https://towardsdatascience.com/machine-learning-classifiers-a5cc4e1b0623>
    Classification is the process of predicting the class of given data
    points. Classes are sometimes called as targets/ labels or
    categories. Classification predictive modeling is the task of
    approximating a mapping function (f) from input variables (X) to
    discrete output variables (y).

    For example, spam detection in email service providers can be
    identified as a classification problem. This is s binary
    classification since there are only 2 classes as spam and not spam.
    A classifier utilizes some training data to understand how given
    input variables relate to the class. In this case, known spam and
    non-spam emails have to be used as the training data. When the
    classifier is trained accurately, it can be used to detect an
    unknown email.

    Classification belongs to the category of supervised learning where
    the targets also provided with the input data. There are many
    applications in classification in many domains such as in credit
    approval, medical diagnosis, target marketing etc.

    There are two types of learners in classification as lazy learners
    and eager learners.

2.  1 Lazy learners

    Lazy learners simply store the training data and wait until a
    testing data appear. When it does, classification is conducted based
    on the most related data in the stored training data. Compared to
    eager learners, lazy learners have less training time but more time
    in predicting.

    Ex. k-nearest neighbor, Case-based reasoning

3.  2\. Eager learners

    Eager learners construct a classification model based on the given
    training data before receiving data for classification. It must be
    able to commit to a single hypothesis that covers the entire
    instance space. Due to the model construction, eager learners take a
    long time for train and less time to predict.

    Ex. Decision Tree, Naive Bayes, Artificial Neural Networks

### Lift[]{.tag data-tag-name="drill"}

SCHEDULED: &lt;2018-12-09 Sun&gt;

``` {.bash}
binisearch.py -o 'lift data mining'
```

1.  Definition

    Interestingness measure

    lift(b,c) = 1 (independent) &gt;1 positively correlated &lt;1
    negatively correlated

    Chi square is another interestingness measure

### Overfitting

Overfitting is a process of fitting the model to the data too much so
that the model will not generalize well to new problems.

### Bias and variance

``` {.bash}
binisearch.py -o 'bias and variance'
```

1.  Definition

    <https://towardsdatascience.com/understanding-the-bias-variance-tradeoff-165e6942b229>
    <https://machinelearningmastery.com/gentle-introduction-to-the-bias-variance-trade-off-in-machine-learning/>

    Watch later

    <https://www.youtube.com/watch?v=5FeT9BAovjQ>
    <https://www.youtube.com/watch?v=jiQamxz2ZcQ>

### Trees and classification

Can decision trees be used for regression

Yes but complicated

<https://www.youtube.com/watch?v=rXMznb5PsY0>

### Classification rate[]{.tag data-tag-name="drill"}

SCHEDULED: &lt;2018-12-09 Sun&gt;

``` {.bash}
binisearch.py -o 'classification rate'
```

1.  Definition

    Classification Rate. For classification models, the ratio of
    correctly classified rows to the total number of rows. For example,
    a classification rate of 0.82 means that 82% of the rows in the
    training data set were correctly classified by the model.

### Decision Trees[]{.tag data-tag-name="drill"} {#decision-trees id="c2b81677-54b8-4b2b-bb4a-0338fa4ae2a7"}

1.  Definition

    <https://scikit-learn.org/stable/modules/tree.html>
    <http://localhost:8888/notebooks/decision_tree_classifier.ipynb>

    ``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
    from sklearn.datasets import load_iris
    from sklearn import tree
    iris = load_iris()
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(iris.data, iris.target)

    import graphviz 
    dot_data = tree.export_graphviz(clf, out_file=None) 
    graph = graphviz.Source(dot_data) 
    graph.render("iris") 

    dot_data = tree.export_graphviz(clf, out_file=None, 
                          feature_names=iris.feature_names,  

    class_names=iris.target_names,  
                          filled=True, rounded=True,  
                          special_characters=True)  
    graph = graphviz.Source(dot_data)  
    graph 

    ```

### Boosting[]{.tag data-tag-name="drill"}

SCHEDULED: &lt;2018-12-09 Sun&gt;

``` {.bash}
binisearch.py -o 'boosting machine learning'
```

1.  What is boosting?

    Boosting is a machine learning ensemble meta-algorithm for primarily
    reducing bias, and also variance in supervised learning, and a
    family of machine learning algorithms that convert weak learners to
    strong ones.

    <https://www.analyticsvidhya.com/blog/2015/11/quick-introduction-boosting-algorithms-machine-learning/>

    Combining several weak learners and producing a strong learner. weak
    learner - weakly correlated with output strong learner - very strong
    correlation with output

### Naive Bayes classification

Text classification Fast

Probabilistic classifier Assumes Occurance of one feature is independent
of another feature(called naive)

Bayes theorem

### K nearest neigbour[]{.tag data-tag-name="drill"} {#k-nearest-neigbour id="67ae8472-3327-4f10-9572-0b5bb105945f"}

1.  What is k nearest neighbour?

    Classifying the data to k nearest categories. It is an supervided
    classification algorithm.

    Calculate the distance between the data and then group the ones with
    least distance(more similar) together.

    <https://www.edureka.co/blog/k-nearest-neighbors-algorithm/>
    <https://www.quora.com/How-is-the-k-nearest-neighbor-algorithm-different-from-k-means-clustering>

### Logistic regression[]{.tag data-tag-name="drill"} {#logistic-regression id="92d18a03-bed8-4b91-9977-09819f397f2f"}

1.  What?

    Logistic regression predicts the probability of an outcome that can
    only have two values (i.e. a dichotomy). The prediction is based on
    the use of one or several predictors (numerical and categorical).

    <http://www.saedsayad.com/logistic_regression.htm>

### Ranking

``` {.bash}
binisearch.py -o 'ranking machine learning'
```

<https://en.wikipedia.org/wiki/Learning_to_rank>

### Linear regression

1.  What?

    We know that the equation of a line is given by y=mx+b, where m is
    the slope and b is the intercept.

    Our goal is to find the best values of slope (m) and intercept (b)
    to fit our data.

    Linear regression uses the ordinary least squares method to fit our
    data points.

    <https://dzone.com/articles/linear-regression-using-python-scikit-learn>

### Perceptron

``` {.bash}
binisearch.py -o perceptron
```

1.  Definition

    Perceptron is a simplified neuron model which responds with 1 when
    w.x &gt; theta and 0 otherwise

    <https://en.wikipedia.org/wiki/Perceptron>

### Hierarchical clustering[]{.tag data-tag-name="drill"} {#hierarchical-clustering id="b567a31b-65c7-4c18-85b3-5cd126ec56b4"}

1.  Definition

    Hierarchical clustering, also known as hierarchical cluster
    analysis, is an algorithm that groups similar objects into groups
    called clusters. The endpoint is a set of clusters, where each
    cluster is distinct from each other cluster, and the objects within
    each cluster are broadly similar to each other.

    Organised as a hierarchical tree

2.  Agglomerative

    Bottom up

3.  Divisive

    Top down

4.  Dendrogram

    Graph or picture which is useful for representation

    cluster dendrogram

### K means clustering[]{.tag data-tag-name="drill"} {#k-means-clustering id="99f202ec-8b3d-43ee-b952-180d422600b1"}

1.  What?

    K means clustering is an unsupervised classification algorithm We
    classify the data into clusters based on the similarity of the data
    points. Similar datapoint come together and form a cluster.

### Neural networks

``` {.bash}
binisearch.py -o 'neural networks'
```

### Sentiment analysis[]{.tag data-tag-name="drill"} {#sentiment-analysis id="2efcb0a8-5350-4582-b36a-13d0f62df4cc"}

1.  What?

    Sentiment analysis is about analysing the text data and figuring out
    whether the text is positive or negative about a particular topic

    For ex: Figuring out whether a particular movie review is positive
    or negative

### Collaborative filtering[]{.tag data-tag-name="drill"}

SCHEDULED: &lt;2018-12-09 Sun&gt;

``` {.bash}
binisearch.py -o 'collaborative filtering'
```

1.  What?

    In the newer, narrower sense, collaborative filtering is a method of
    making automatic predictions (filtering) about the interests of a
    user by collecting preferences or taste information from many users
    (collaborating).

    <https://en.wikipedia.org/wiki/Collaborative_filtering>

### Tagging or labelling[]{.tag data-tag-name="drill"}

SCHEDULED: &lt;2018-12-09 Sun&gt;

``` {.bash}
binisearch.py -o 'tagging machine learning'
```

1.  What?

    labeling plain text to sports, technology, movie etc. labeing a
    picture to fox, wolf, dog etc

Text mining NLP
---------------

### Corpus

``` {.bash}
binisearch.py -o 'Corpus nlp'
```

### Named entity recognition

``` {.bash}
binisearch.py -o 'Named entity recognition'
```

### Text analysis

``` {.bash}
binisearch.py -o 'Text analysis'
```

### Unstructured information management architecture UIMA

``` {.bash}
binisearch.py -o 'UIMA'
```

### Term document matrix

``` {.bash}
binisearch.py -o 'Term document matrix'
```

### Term frequency and weight

``` {.bash}
binisearch.py -o 'Term frequency and weight'
```

### Support vector machines

``` {.bash}
binisearch.py -o 'Support vector machines'
```

### Association rules

``` {.bash}
binisearch.py -o 'Association rules'
```

### Market basket analysis

``` {.bash}
binisearch.py -o 'Market basket analysis'
```

### Feature extraction

``` {.bash}
binisearch.py -o 'Feature extraction'
```

### Using mahout

``` {.bash}
binisearch.py -o 'mahout'
```

### Using weka

``` {.bash}
binisearch.py -o 'weka'
```

### Using NLTK

``` {.bash}
binisearch.py -o 'NLTK'
```

### Classify text

``` {.bash}
binisearch.py -o 'Classify text'
```

### Vocabulary mapping

``` {.bash}
binisearch.py -o 'Vocabulary mapping'
```

Visualization
-------------

<http://achariam.com/dataviz/>

1.  Good data visualization is informative

Well presented data forms the backbone of a compelling story. It has the
power to strengthen and illuminate a narrative—improving understanding
and focusing on what’s important.

1.  Good data visualization is well balanced

Communicating quantitative data effectively requires the right balance
of components. Color is used with purpose and is not distracting. All
parts are labeled and include a legend when necessary. The scale of the
visualization must be immediately identifiable. The standard lexicon of
graphs are often all that is required—do not use pie charts.

1.  Good data visualization is equally concerned with what is not
    displayed

People are easily overwhelmed with extraneous details. Simplify and
reduce what is being presented to what is essential.

1.  Good data visualization is created with pure data

Avoid utilizing muddy or incomplete sources of data. Misleading the
audience with false information or lack of clarity is in poor taste.
Ultimately, good data visualization enables better decisions and
actions.

1.  Good data visualization is human

Parsing large data quantities of data is beyond human perception. The
goal with any kind of data visualization is to augment and improve human
perception. Just like a microscope it allows us to explore data within
the realm of our understanding.

### Data exploration in R

``` {.bash}
binisearch.py -o 'Data exploration in R'
```

Hist, boxplot etc

### Univariate bivariate and multivariate visualization

``` {.bash}
binisearch.py -o 'Univariate bivariate and multivariate visualization'
```

### ggplot2

``` {.bash}
binisearch.py -o 'ggplot2'
```

### Common code

``` {.python .rundoc-block rundoc-language="python" rundoc-session="yes"}
def display_inline(filename):
    plt.savefig(filename)
    print()
    print('[[./{}]]'.format(filename))

```

### Histogram and Pie(Uni)

``` {.bash}
binisearch.py -o 'Histogram and Pie(Uni)'
```

``` {.python .rundoc-block rundoc-language="python" rundoc-session="yes" rundoc-results="output" rundoc-exports="both"}
# alpha is opacity

import numpy as np
#import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 5
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.1)
#plt.show()
display_inline('images/histogram.png')

```

![alt ./images/histogram.png](./images/histogram.png)
```

### Tree and Treemap

``` {.bash}
binisearch.py -o 'Tree and Treemap'
```

<https://python-graph-gallery.com/200-basic-treemap-with-python/>

``` {.python .rundoc-block rundoc-language="python" rundoc-session="yes" rundoc-results="output" rundoc-exports="both"}

# libraries 
import matplotlib.pyplot as plt 
import squarify # pip install squarify (algorithm for treemap) 

# If you have 2 lists 
squarify.plot(sizes=[13,22,35,5], label=["group A", "group B", "group C", "group D"]) 
plt.axis('off') 
display_inline('./images/treemap1.png')

# If you have a data frame? 
import pandas as pd 
df = pd.DataFrame({'nb_people':[8,3,4,2], 'group':["group A", "group B", "group C", "group D"] }) 
squarify.plot(sizes=df['nb_people'], label=df['group']) 
plt.axis('off') 
display_inline('./images/treemap2.png')


```

![alt ././images/treemap1.png](././images/treemap1.png)
![alt ././images/treemap2.png](././images/treemap2.png)
```

### Dendrogram {#dendrogram-1}

<https://python-graph-gallery.com/400-basic-dendrogram/>

``` {.python}

# Libraries
import pandas as pd
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

# Import the mtcars dataset from the web + keep only numeric variables
url = 'https://python-graph-gallery.com/wp-content/uploads/mtcars.csv'
df = pd.read_csv(url)
df = df.set_index('model')
del df.index.name
df


# Calculate the distance between each sample
# You have to think about the metric you use (how to measure similarity) + about the method of clusterization you use (How to group cars)
Z = linkage(df, 'ward')


# Make the dendrogram
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance (Ward)')
dendrogram(Z, labels=df.index, leaf_rotation=90)

plt.show()

```

### Scatterplot(bi)

``` {.bash}
binisearch.py -o 'Scatterplot(bi)'
```

``` {.python}
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.plot(x, y, 'o', color='black');
plt.show()
```

``` {.python}
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.scatter(x, y, marker='o', color='black');
plt.show()
```

### Heatmap

<https://python-graph-gallery.com/heatmap/>

``` {.python .rundoc-block rundoc-language="python" rundoc-tangle="yes" rundoc-tangle="/tmp/heatmap.py"}
import seaborn as sns
import pandas as pd
import numpy as np

# Create a dataset (fake)
df = pd.DataFrame(np.random.random((5,5)), columns=["a","b","c","d","e"])

# Default heatmap: just a visualization of this square matrix
p1 = sns.heatmap(df)

```

### Line charts(bi)

``` {.bash}
binisearch.py -o 'Line charts(bi)'
```

``` {.python}
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np

x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.plot(x, y, color='black');
plt.show()
```

### Spatial charts

``` {.bash}
binisearch.py -o 'Spatial charts'
```

### Survey plot

A survey plot is a simple multi-attribute visualization technique that
can help to spot correlations between any two variables especially when
the data is sorted according to a particular dimension. Each horizontal
splice in a plot corresponds to a particular data instance. The data on
a specific attribute is shown in a single column, where the length of
the line corresponds to the dimensional value. When data includes a
discrete or continuous class, the slices (data instances) are colored
correspondingly.

Implementation in Orange supports sorting by two selected attributes
(Sorting). The attributes shown in the plot are listed in Shown
attributes box, all other appear in the list of Hidden attributes.

Below is a snapshot of survey plot widget for an Iris. Plot nicely shows
that petal width and length and sepal length are correlated. It is also
very clear that Iris-setosa can be classified based on petal length or
width alone, while for the Iris versicolor and virginica there is some
ambiguity with some potential outliers, one of which is highlighted in
the snapshot.

<https://docs.orange.biolab.si/2/widgets/rst/visualize/surveyplot.html>

``` {.bash}
binisearch.py -o 'Survey plot visualization'
```

### Timeline

``` {.bash}
binisearch.py -o 'Timeline'
```

<https://matplotlib.org/gallery/lines_bars_and_markers/timeline.html>

``` {.python}
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime

# A list of Matplotlib releases and their dates
# Taken from https://api.github.com/repos/matplotlib/matplotlib/releases
names = ['v2.2.2', 'v2.2.1', 'v2.2.0', 'v2.1.2', 'v2.1.1', 'v2.1.0', 'v2.0.2',
         'v2.0.1', 'v2.0.0', 'v1.5.3', 'v1.5.2', 'v1.5.1', 'v1.5.0', 'v1.4.3',
         'v1.4.2', 'v1.4.1', 'v1.4.0']

dates = ['2018-03-17T03:00:07Z', '2018-03-16T22:06:39Z',
         '2018-03-06T12:53:32Z', '2018-01-18T04:56:47Z',
         '2017-12-10T04:47:38Z', '2017-10-07T22:35:12Z',
         '2017-05-10T02:11:15Z', '2017-05-02T01:59:49Z',
         '2017-01-17T02:59:36Z', '2016-09-09T03:00:52Z',
         '2016-07-03T15:52:01Z', '2016-01-10T22:38:50Z',
         '2015-10-29T21:40:23Z', '2015-02-16T04:22:54Z',
         '2014-10-26T03:24:13Z', '2014-10-18T18:56:23Z',
         '2014-08-26T21:06:04Z']
dates = [datetime.strptime(ii, "%Y-%m-%dT%H:%M:%SZ") for ii in dates]

levels = np.array([-5, 5, -3, 3, -1, 1])
fig, ax = plt.subplots(figsize=(8, 5))

# Create the base line
start = min(dates)
stop = max(dates)
ax.plot((start, stop), (0, 0), 'k', alpha=.5)

# Iterate through releases annotating each one
for ii, (iname, idate) in enumerate(zip(names, dates)):
    level = levels[ii % 6]
    vert = 'top' if level < 0 else 'bottom'

    ax.scatter(idate, 0, s=100, facecolor='w', edgecolor='k', zorder=9999)
    # Plot a line up to the text
    ax.plot((idate, idate), (0, level), c='r', alpha=.7)
    # Give the text a faint background and align it properly
    ax.text(idate, level, iname,
            horizontalalignment='right', verticalalignment=vert, fontsize=14,
            backgroundcolor=(1., 1., 1., .3))
ax.set(title="Matplotlib release dates")
# Set the xticks formatting
# format xaxis with 3 month intervals
ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval=3))
ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
fig.autofmt_xdate()

# Remove components for a cleaner look
plt.setp((ax.get_yticklabels() + ax.get_yticklines() +
          list(ax.spines.values())), visible=False)
plt.show()
```

### Barplot

<https://python-graph-gallery.com/barplot/>
<https://python-graph-gallery.com/1-basic-barplot/>

``` {.python}
import numpy as np
import matplotlib.pyplot as plt

# Make a fake dataset:
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))

# Create bars
plt.bar(y_pos, height)

# Create names on the x-axis
plt.xticks(y_pos, bars)

# Show graphic
plt.show()


```

### Violinplot

<https://python-graph-gallery.com/violin-plot/>
<https://python-graph-gallery.com/58-show-number-of-observation-on-violinplot/>

``` {.python}

# library & dataset
import matplotlib.pyplot as plt
import seaborn as sns, numpy as np
df = sns.load_dataset("iris")

# Basic violinplot
ax = sns.violinplot(x="species", y="sepal_length", data=df)

# Calculate number of obs per group & median to position labels
medians = df.groupby(['species'])['sepal_length'].median().values
nobs = df['species'].value_counts().values
nobs = [str(x) for x in nobs.tolist()]
nobs = ["n: " + i for i in nobs]

# Add it to the plot
pos = range(len(nobs))
for tick,label in zip(pos,ax.get_xticklabels()):
   ax.text(pos[tick], medians[tick] + 0.03, nobs[tick], horizontalalignment='center', size='x-small', color='w', weight='semibold')
plt.show()

```

### pairplot

<https://seaborn.pydata.org/generated/seaborn.pairplot.html>

``` {.python}
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="ticks", color_codes=True)
iris = sns.load_dataset("iris")
g = sns.pairplot(iris)
plt.show()
```

### lmplot

<https://seaborn.pydata.org/generated/seaborn.lmplot.html>

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output" rundoc-exports="both"}
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(color_codes=True)
tips = sns.load_dataset("tips")
g = sns.lmplot(x="total_bill", y="tip", data=tips)
filename = 'lmplot.png'
#plt.show()
plt.savefig(filename)
print('[[./{}]]'.format(filename))

```

![alt ./lmplot.png](./lmplot.png)
```

### joinplot

<https://seaborn.pydata.org/generated/seaborn.jointplot.html>

``` {.python}
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="white", color_codes=True)
tips = sns.load_dataset("tips")
g = sns.jointplot(x="total_bill", y="tip", data=tips)
plt.show()
```

### Distributions

<https://seaborn.pydata.org/tutorial/distributions.html>

### Contour

<https://www.python-course.eu/matplotlib_contour_plot.php>

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
import matplotlib.pyplot as plt
import numpy as np

xlist = np.linspace(-3.0, 3.0, 3)
ylist = np.linspace(-3.0, 3.0, 4)
X, Y = np.meshgrid(xlist, ylist)
Z = np.sqrt(X**2 + Y**2)
print(X)
plt.figure()
cp = plt.contour(X, Y, Z)
plt.clabel(cp, inline=True, 
          fontsize=10)
plt.title('Contour Plot')
plt.xlabel('x (cm)')
plt.ylabel('y (cm)')
plt.show()

```

1.  What is mesh grid?

    ``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
    import numpy as np

    xlist = np.arange(1, 7)
    ylist = np.arange(1, 7)
    X, Y = np.meshgrid(xlist, ylist)
    print(xlist)
    print(ylist)
    print(X)
    print(Y)
    ```

### Boxplot

<http://python-graph-gallery.com/boxplot/>
<https://python-graph-gallery.com/30-basic-boxplot-with-seaborn/>

1.  1 - One numerical variable only

    If you have only one numerical variable, you can use this code to
    get a boxplot with only one group (left chart).

    ``` {.python}
    # library & dataset
    import matplotlib.pyplot as plt
    import seaborn as sns
    df = sns.load_dataset('iris')

    # Make boxplot for one group only
    sns.boxplot( y=df["sepal_length"] )
    plt.show()

    ```

2.  2 - One numerical variable, and several groups

    Let’s say we want to study the distribution of a numerical variable,
    but for each group separately. Here we study the sepal length of 3
    species of flower.

    ``` {.python}

    # library & dataset
    import matplotlib.pyplot as plt
    import seaborn as sns
    df = sns.load_dataset('iris')

    sns.boxplot( x=df["species"], y=df["sepal_length"] )
    plt.show()

    ```

3.  3 - Several numerical variable

    Finally we can study the distribution of several numerical
    variables, let’s say sepal length and width:

    ``` {.python}

    # library & dataset
    import matplotlib.pyplot as plt
    import seaborn as sns
    df = sns.load_dataset('iris')

    sns.boxplot(data=df.ix[:,0:3])
    plt.show()

    ```

### Decision Tree

``` {.bash}
binisearch.py -o 'Decision Tree'
```

<https://medium.com/@rnbrown/creating-and-visualizing-decision-trees-with-python-f8e8fa394176>

``` {.python .rundoc-block rundoc-language="python" rundoc-tangle="yes" rundoc-tangle="/tmp/exp.py"}
import sklearn.datasets as datasets
import pandas as pd
iris=datasets.load_iris()
df=pd.DataFrame(iris.data, columns=iris.feature_names)
y=iris.target


from sklearn.tree import DecisionTreeClassifier
dtree=DecisionTreeClassifier()
dtree.fit(df,y)

from sklearn.externals.six import StringIO  
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(dtree, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
Image(graph.create_png())


```

### Animation using image magic

<https://python-graph-gallery.com/341-python-gapminder-animation/>

``` {.python}
# libraries
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style("white")
import pandas as pd
my_dpi=96

# Get the data (csv file is hosted on the web)
url = 'https://python-graph-gallery.com/wp-content/uploads/gapminderData.csv'
data = pd.read_csv(url)

# And I need to transform my categorical column (continent) in a numerical value group1->1, group2->2...
data['continent']=pd.Categorical(data['continent'])

# For each year:
for i in data.year.unique():

    # initialize a figure
    fig = plt.figure(figsize=(680/my_dpi, 480/my_dpi), dpi=my_dpi)

    # Change color with c and alpha. I map the color to the X axis value.
    tmp=data[ data.year == i ]
    plt.scatter(tmp['lifeExp'], tmp['gdpPercap'] , s=tmp['pop']/200000 , c=tmp['continent'].cat.codes, cmap="Accent", alpha=0.6, edgecolors="white", linewidth=2)

    # Add titles (main and on axis)
    plt.yscale('log')
    plt.xlabel("Life Expectancy")
    plt.ylabel("GDP per Capita")
    plt.title("Year: "+str(i) )
    plt.ylim(0,100000)
    plt.xlim(30, 90)

    # Save it
    filename='Gapminder_step'+str(i)+'.png'
    plt.savefig(filename, dpi=96)
    plt.gca()

```

``` {.bash}

# Then use image magick (this is bash, not python)
convert -delay 80 Gapminder*.png animated_gapminder.gif

```

### Wordcloud

<https://python-graph-gallery.com/260-basic-wordcloud/>

``` {.python}
# Libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create a list of word
text=("Python Python Python Matplotlib Matplotlib Seaborn Network Plot Violin Chart Pandas Datascience Wordcloud Spider Radar Parrallel Alpha Color Brewer Density Scatter Barplot Barplot Boxplot Violinplot Treemap Stacked Area Chart Chart Visualization Dataviz Donut Pie Time-Series Wordcloud Wordcloud Sankey Bubble")

# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()

```

### Area plot

<https://python-graph-gallery.com/pie-plot/>

<https://python-graph-gallery.com/140-basic-pieplot-with-panda/>

``` {.python}

# library
import matplotlib.pyplot as plt
import pandas as pd

# --- dataset 1: just 4 values for 4 groups:
df = pd.DataFrame([8,5,1,2], index=['a', 'b', 'c', 'd'], columns=['x'])

# make the plot
df.plot(kind='pie', subplots=True, figsize=(8, 8))
plt.show()
```

### Stacked area plot

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
# library
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dataset
np.random.seed(42)
df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
print(df)
# plot
df.plot.area()
plt.show()

```

### D3.Js

``` {.bash}
binisearch.py -o 'D3.Js'
```

### Infovis

``` {.bash}
binisearch.py -o 'Infovis'
```

### IBM Many eyes

``` {.bash}
binisearch.py -o 'IBM Many eyes'
```

### Tableu

``` {.bash}
binisearch.py -o 'Tableu'
```

Big data
--------

### Map reduce fundamentals

``` {.bash}
binisearch.py -o 'Map reduce fundamentals'
```

### Hadoop components

``` {.bash}
binisearch.py -o 'Hadoop components'
```

### HDFS

``` {.bash}
binisearch.py -o 'HDFS'
```

### Data replication principles

``` {.bash}
binisearch.py -o 'Data replication principles'
```

### Setup hadoop(IBM/cloudera/Hortonworks)

``` {.bash}
binisearch.py -o 'Setup hadoop(IBM/cloudera/Hortonworks)'
```

### Name and datanodes

``` {.bash}
binisearch.py -o 'Name and datanodes'
```

### Job and task traker

``` {.bash}
binisearch.py -o 'Job and task traker'
```

### M/R programming

``` {.bash}
binisearch.py -o 'M/R programming'
```

### Sqoop: Loading data in HDFS

``` {.bash}
binisearch.py -o 'Sqoop: Loading data in HDFS'
```

### Flume, Scribe: For unstruct data

``` {.bash}
binisearch.py -o 'Flume, Scribe: For unstruct data'
```

### SQL with pig

``` {.bash}
binisearch.py -o 'SQL with pig'
```

### DWH with hive

``` {.bash}
binisearch.py -o 'DWH with hive'
```

### Scribe with, chukwa for weblog

``` {.bash}
binisearch.py -o 'Scribe with, chukwa for weblog'
```

### Using mahout

``` {.bash}
binisearch.py -o 'Using mahout'
```

### Zookeeper/Avro

``` {.bash}
binisearch.py -o 'Zookeeper/Avro'
```

### Storm hadoop realtime

``` {.bash}
binisearch.py -o 'Storm hadoop realtime'
```

### Rhadoop, Rhipe

``` {.bash}
binisearch.py -o 'Rhadoop, Rhipe'
```

### rmr

``` {.bash}
binisearch.py -o 'rmr'
```

### Cassandra

``` {.bash}
binisearch.py -o 'Cassandra'
```

### Mongodb, neo4j

``` {.bash}
binisearch.py -o 'Mongodb, neo4j'
```

Data ingestion
--------------

``` {.bash}
binisearch.py -o 'data ingestion'

```

Data Ingestion is the process of accessing and importing data for
immediate use or storage in a database. To ingest something is to "take
something in or absorb something."

Data can be ingested in real time or in batches. When data is ingested
in real time, each data item is imported as soon as it is issued by the
source. When data is ingested in batches, data items are imported in
discrete chunks at periodic intervals of time. An effective data
ingestion process begins by prioritizing data sources, validating
individual files and routing data items to the correct destination.

When numerous big data sources exist in diverse formats (the sources may
often number in the hundreds and the formats in the dozens), it can be
challenging for businesses to ingest data at the speed that's necessary
to ensure smooth performance or maintain a competitive advantage. To
that end, vendors offer programs that are tailored to ingest data for
specific applications or computing environments. When data ingestion is
automated, the software used to carry out the process may also include
data preparation features that will structure and organize incoming data
so it can be analysed in on the fly or at a later date by business
intelligence (BI) and business analytics (BA) programs.

### Summary of data formats

``` {.bash}
binisearch.py -o 'Summary of data formats'
```

### Data discovery

``` {.bash}
binisearch.py -o 'Data discovery'
```

### Data sources and acquisition

``` {.bash}
binisearch.py -o 'Data sources and acquisition'
```

### Data integration

``` {.bash}
binisearch.py -o 'Data integration'
```

Data integration involves combining data residing in different sources
and providing users with a unified view of them. This process becomes
significant in a variety of situations, which include both commercial
(such as when two similar companies need to merge their databases) and
scientific (combining research results from different bioinformatics
repositories, for example) domains. Data integration appears with
increasing frequency as the volume (that is, big data) and the need to
share existing data explodes. It has become the focus of extensive
theoretical work, and numerous open problems remain unsolved.

### Data fusion

``` {.bash}
binisearch.py -o 'Data fusion'
```

Data fusion is the process of integrating multiple data sources to
produce more consistent, accurate, and useful information than that
provided by any individual data source

### Transformation and enrichment

``` {.bash}
binisearch.py -o 'Transformation and enrichment'
```

### Data survery

``` {.bash}
binisearch.py -o 'Data survery'
```

### Google openrefine

``` {.bash}
binisearch.py -o 'Google openrefine'
```

### How much data?

``` {.bash}
binisearch.py -o 'How much data?'
```

### Using ETL

``` {.bash}
binisearch.py -o 'Using ETL'
```

Data munging
------------

Data wrangling, sometimes referred to as data munging, is the process of
transforming and mapping data from one "raw" data form into another
format with the intent of making it more appropriate and valuable for a
variety of downstream purposes such as analytics.

``` {.bash}
binisearch.py -o 'data munging'

```

### Dimensionality and numerosity reduction

``` {.bash}
binisearch.py -o 'Dimensionality and numerosity reduction'
```

### Normalization

``` {.bash}
binisearch.py -o 'Normalization'
```

Normalizing the data is done so that all the input variables have the
same treatment in the model and the coefficients of a model are not
scaled with respect to the units of the inputs.

For instance, consider that you have a model that measures the aging of
paintings based on room temperature, humidity and some other variables.
If humidity is measured in litres per cubic metre and temperature in
degrees Celsius, the coefficients in the model will be scaled
accordingly and may have a high value for humidity and a low value for
temperature (say). If you scale the variables, such as by using (x−μ)/σ
or any other technique, variability in output due to unit change in
input variables will be modeled more realistically.

You may wish to rescale the predicted output to interpret the results.

In regression, the t-values and R2 values are not affected due to
scaling or not scaling. However, interpreting the results becomes easier
using scaling.

<https://www.statisticshowto.datasciencecentral.com/normalized/>
<http://www.analytictech.com/ba762/handouts/normalization.htm>

### Data Scrubbing

I think originally he intended Data cleansing. Data cleansing is a
better word to use

1.  Data scrubbing

    ``` {.bash}
    binisearch.py -o 'Data Scrubbing'
    ```

    Data scrubbing is an error correction technique that uses a
    background task to periodically inspect main memory or storage for
    errors, then correct detected errors using redundant data in the
    form of different checksums or copies of data. Data scrubbing
    reduces the likelihood that single correctable errors will
    accumulate, leading to reduced risks of uncorrectable errors.

2.  Data cleansing

    ``` {.bash}
    binisearch.py -o 'Data cleansing'
    ```

    Data cleansing or data cleaning is the process of detecting and
    correcting (or removing) corrupt or inaccurate records from a record
    set, table, or database and refers to identifying incomplete,
    incorrect, inaccurate or irrelevant parts of the data and then
    replacing, modifying, or deleting the dirty or coarse data

### Handling missing values

``` {.bash}
binisearch.py -o 'Handling missing values'
```

<https://www.kaggle.com/dansbecker/handling-missing-values>

Delete values Imputation Extended imputation

### Unbiased estimators

``` {.bash}
binisearch.py -o 'Unbiased estimators'
```

In statistics, the bias (or bias function) of an estimator is the
difference between this estimator's expected value and the true value of
the parameter being estimated. An estimator or decision rule with zero
bias is called unbiased. Otherwise the estimator is said to be biased.

### Binning sparse values

``` {.bash}
binisearch.py -o 'Binning sparse values'
```

Binning is a way to group a number of more or less continuous values
into a smaller number of "bins". For example, if you have data about a
group of people, you might want to arrange their ages into a smaller
number of age intervals.

### Feature extraction

``` {.bash}
binisearch.py -o 'Feature extraction'
```

### Denoising

``` {.bash}
binisearch.py -o 'Denoising'
```

### Sampling

``` {.bash}
binisearch.py -o 'Sampling'
```

### Stratified sampling

``` {.bash}
binisearch.py -o 'Stratified sampling'
```

In statistical surveys, when subpopulations within an overall population
vary, it could be advantageous to sample each subpopulation (stratum)
independently. Stratification is the process of dividing members of the
population into homogeneous subgroups before sampling. The strata should
be mutually exclusive: every element in the population must be assigned
to only one stratum. The strata should also be collectively exhaustive:
no population element can be excluded. Then simple random sampling or
systematic sampling is applied within each stratum. The objective is to
improve the precision of the sample by reducing sampling error. It can
produce a weighted mean that has less variability than the arithmetic
mean of a simple random sample of the population.

In computational statistics, stratified sampling is a method of variance
reduction when Monte Carlo methods are used to estimate population
statistics from a known population.\[1\]

### Principal component analysis

``` {.bash}
binisearch.py -o 'Principal component analysis'
```

Data preprocessing
------------------

<https://unacademy.com/lesson/data-cleaning-noisy-data/NI5A24ZO>
improvise the data to good quality

Data cleaning clean the data

Data integration combining different data to comon data

Transformation change the data

Data production

data is incomplete, noisy, inconsistent

No quality data, no quality mining result

Data pre processing to maintain quality

example

Manager at store

incomplete No recorded value for name inaccurate noice errors
Inconsitent data unusual values, discrepancies in department codes used
to categorize items

Data quality

Accuracy - errors in data entry, format incorrect, data transmission
error completeness- data of interest missing consistency-
timeliness-data not arriving at right time believability-past errors
makes you distrust the source interpretability-data is not interpretable
sometimes

Data cleaning

Knowledge discovery

fill missing values smooth out noise identifying outliers correct
inconsistencies

How to fill missing values

Ignore the data when class label is missing if small percentage is
missing we can use this

Filling the missing value manually This can be done if feasible

Use a global constant with a missing value Unknown, infinity Algorithm
might think that it is a category or entity on its own

Use a measure of central tendency We can use the mean Credit risk can be
used for mean value In normal distribution For skewed distribution we
should use median

Use the most probable value to fill the missing value May be mode
Determined by regression, inference based tools, bayesian formalism,
decision tree induction

Missing value is sometimes correct data Not applicable option might be
missing in some data

Noisy data Noise is a random error in the measured variable

Data visualization can be used to identify outliers

Binning Neighbourhood values are considered

Partiion into equal-frequency bins bin 1 - 4 8 15 bin 2 - 21, 21, 24 bin
3 - 25, 28, 34 Binsize Smoothing by bin means bin 1 - 9 9 9 bin 2 - 22
22 22 bin 3 - 29 29 29

Smoothing by bin boundaries Did not understand this correclty bin 1 - 4
4 15 bin 2 - 21 21 24 bin 3 - 25 25 34

Regression

Data smoothing technique that conforms data values to a function Linear
regrssion finding the best line to fit two attributes Multiple linear
regreassion is an extension of linear regression where two or more
attributes are involved and the data are fit to multidimensional surface

linear regression one attribute is fit to other

Multi dimensional 3 d or multi dimensional attribute(fit to a 2d plane)
May be hyper plane is made to fit

Outliers may not give a good output in data mining For example in
clutering.

Data integration

Merging of data from multiple data sources How can we match the schema
from various sources? Whether the attributes are correlated? nominal
numerial tuple duplication? Is the data value conflict detected?

www data science and culture data

Schema integration customer~number~ customer~id~ are they the same it
may not be consistent in all dbs

Structure of data

Solution to entity identification problem is metadata metadata name,
meaning, dat type, renge permited, null values for handling blank(zero,
null)

Redundancy and correlation analysis Redundant if an attribute can be
derived from another attribute

Solution - Correlation Analysis

Given two attributes such analysis can measure how strongly one
attribute implies other, based on available data

For nominal data, we use chi square test for numerical data we can use
correlation coefficient and covariance

x2 correlation test for nominal data

A a1, a2, .. ac (c distinct values) B b1, b2, ... br (r ") The data
tuples described by A and b can be shown as contingency table, with c
values of A making up the columns and the r values of B making up the
rows.

Finished upto data integration video

Toolbox
-------

### Ms excel analysis toolpak

``` {.bash}
binisearch.py -o 'Ms excel analysis toolpak'
```

### Java, python

``` {.bash}
binisearch.py -o 'Java, python'
```

### R, Rstudio, Rattle

``` {.bash}
binisearch.py -o 'R, Rstudio, Rattle'
```

### Weka, knime, Rapidminer

``` {.bash}
binisearch.py -o 'Weka, knime, Rapidminer'
```

### Hadoop distribution of choice

``` {.bash}
binisearch.py -o 'Hadoop distribution of choice'
```

### Spark, Storm

``` {.bash}
binisearch.py -o 'Spark, Storm'
```

### Flume, Scribe, Chukwa

``` {.bash}
binisearch.py -o 'Flume, Scribe, Chukwa'
```

### Nutch, Talend, Scraperwiki

``` {.bash}
binisearch.py -o 'Nutch, Talend, Scraperwiki'
```

### Webscraper, flume, scoop

``` {.bash}
binisearch.py -o 'Webscraper, flume, scoop'
```

### tm, rweka, NLTK

``` {.bash}
binisearch.py -o 'tm, rweka, NLTK'
```

### RHIPE

``` {.bash}
binisearch.py -o 'RHIPE'
```

### D3.js,ggplot2,Shiny

``` {.bash}
binisearch.py -o 'D3.js,ggplot2,Shiny'
```

### IBM languageware

``` {.bash}
binisearch.py -o 'IBM languageware'
```

### Cassandra. mongodb

``` {.bash}
binisearch.py -o 'Cassandra. mongodb'
```

General resources handpicked
----------------------------

<https://elitedatascience.com/data-science-resources>
<http://code-love.com/2017/05/27/learn-data-science/>

[DONE]{.done .DONE} Data science hacker news {#data-science-hacker-news}
--------------------------------------------

SCHEDULED: &lt;2017-12-16 Sat 12:00&gt;

-   State "DONE" from "TODO" \[2017-12-15 Fri 11:31\]
-   State "DONE" from "TODO" \[2017-10-23 Mon 11:11\]
-   State "DONE" from "TODO" \[2017-10-12 Thu 10:36\]

CLOCK: \[2017-10-12 Thu 10:35\]--\[2017-10-12 Thu 10:36\] =&gt; 0:01

-   State "DONE" from "TODO" \[2017-09-14 Thu 10:28\]
-   State "DONE" from "TODO" \[2017-08-23 Wed 14:34\]
-   State "DONE" from "TODO" \[2017-08-17 Thu 10:07\]
-   State "DONE" from "TODO" \[2017-08-16 Wed 14:38\]
-   State "DONE" from "TODO" \[2017-07-19 Wed 10:48\]

CLOCK: \[2017-07-18 Tue 14:10\]--\[2017-07-18 Tue 14:10\] =&gt; 0:00

-   State "DONE" from "TODO" \[2017-07-13 Thu 12:45\]
-   State "DONE" from "TODO" \[2017-07-11 Tue 10:28\]

<http://www.datatau.com/>
<https://www.facebook.com/hashtag/machinelearning>
<https://www.twitter.com/hashtag/machinelearning>
<https://www.facebook.com/hashtag/datascience>
<https://www.twitter.com/hashtag/datascience>

<https://news.ycombinator.com/>

Mathematical modeling
---------------------

Simulation
----------

Databases
---------

Inputs(convergence of digital platform)
---------------------------------------

### Social media

### emails

### tweets

### text messages(sms)

### blogs

### amazon

Data engineering
----------------

Scientific method
-----------------

Advanced computing
------------------

Hacker mindset
--------------

Domain enterprise
-----------------

Must read books
---------------

<http://www.kdnuggets.com/2017/04/10-free-must-read-books-machine-learning-data-science.html?utm_content=bufferc386f&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer>

<https://www.quora.com/What-are-the-best-books-about-data-science>

<http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/>

<https://github.com/zacharski/pg2dm-python>

How to learn data science in 10 days
------------------------------------

<https://www.quora.com/What-should-I-learn-in-data-science-in-100-hours>

Data sets
---------

<https://elitedatascience.com/datasets>
<https://github.com/awesomedata/awesome-public-datasets?utm_campaign=News&utm_medium=Community&utm_source=DataCamp.com#economics>

Papers with code link
---------------------

I need to explore this later <https://github.com/zziz/pwc>