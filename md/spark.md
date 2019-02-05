sql join in diagramatic form
============================

``` {.bash}
xdg-open sqljoin.png
firefox https://www.google.co.in/search?q=sql+join+venn+diagram&client=ubuntu&hs=cPe&channel=fs&biw=1535&bih=805&tbm=isch&imgil=SXGHjyoV2uc_DM%253A%253Bwgr8RIHzcKDOHM%253Bhttp%25253A%25252F%25252Fwww.codeproject.com%25252FArticles%25252F33052%25252FVisual-Representation-of-SQL-Joins&source=iu&pf=m&fir=SXGHjyoV2uc_DM%253A%252Cwgr8RIHzcKDOHM%252C_&usg=__MfZs8aa97jg__Y52Io4c6KOhYUc%3D&ved=0ahUKEwiZ3ePolvPPAhWLs48KHakxBGgQyjcINA&ei=JNsNWJm7G4vnvgSp45DABg#imgrc=mogSTbjuV7hmkM%3A
```

Spark overview
==============

<http://spark.apache.org/docs/latest/sql-programming-guide.html>
Overview

Spark SQL is a Spark module for structured data processing. Methods to
interact with Spark SQL a) SQL b) Dataset API.

Boilerplate code in all spark programs
======================================

    from pyspark import SparkContext, SparkConf

    sc = SparkContext("local", "my app name")

    from pyspark.sql import SQLContext
    sqlContext = SQLContext(sc)


    * DataFrame
    A DataFrame is a Dataset organized into named columns.

    Json and parquet files
    DataFrame can write to parquet files
    * Example codes of untyped dataset operations or DataFrame operations
    #+BEGIN_SRC sh :results output
    cat /home/bineesh/temp/hadoop/spark-2.0.0-bin-hadoop2.7/examples/src/main/resources/people.json

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
import os
for k in os.environ:
    print(k, os.environ[k])

```

``` {.bash}
ls ~/temp/hadoop/spark-2.4.0-bin-hadoop2.7/examples/src/main/resources/people.csv
```

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("dummy app name").setMaster("local")
sc = SparkContext(conf=conf)
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

path = '/home/bineesh/temp/hadoop/spark-2.4.0-bin-hadoop2.7/examples/src/main/resources/people.json'
df = sqlContext.read.json(path)

# Displays the content of the DataFrame to stdout
df.show()
print("Schema is")
df.printSchema()

print("only name column")
df.select("name").show()

print("df name and df age + 1")
df.select(df['name'], df['age'] + 1).show()


print("Select people older than 21")
df.filter(df['age'] > 21).show()
## age name
## 30  Andy


print("Count people by age")
df.groupBy("age").count().show()
## age  count
## null 1
## 19   1
## 30   1
"""
"""
```

Interesting observation. Because of lazy evaluation I was unable to
delete the temporary file I created. Only when the show command is
called the evaluation of the dataframe happened

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
import io
from pyspark import SparkContext, SparkConf
try:
    conf = SparkConf().setAppName("dummy app name").setMaster("local")
    sc = SparkContext(conf=conf)
except:
    pass
from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

from tempfile import NamedTemporaryFile

raw_data = b"""
{"name":"Michael"}
{"name":"Andy", "age":30}
{"name":"Justin", "age":19}
{"name":"Albert", "age":100}
{"name":"Niel", "age":100}
{"name":"Vargheese", "age":30}
"""

def read_from_string(string1):
    with NamedTemporaryFile(delete=False) as f:
        f.write(raw_data)
        tempfilename = f.name
        print(tempfilename)
    df = sqlContext.read.json(tempfilename)
    return df    


df = read_from_string(raw_data)
print("Count people by age")
df.groupBy("age").count().show()

df.createOrReplaceTempView("people")

print("Printing everything from table using sql")
sqlDF = sqlContext.sql("SELECT * FROM people")
sqlDF.show()

print("selectting columns based on a filter using sql")
sqlContext.sql("select * from people where age = 30").show()

```

changing the column name of dataframe
=====================================

<http://stackoverflow.com/questions/33778664/spark-dataframe-distinguish-columns-with-duplicated-name>
Column rename example

f0 = flatClustering0.withColumnRenamed('item', 'item~jan~') f1 =
flatClustering1.withColumnRenamed('item', 'item~may~')

Like Relational algebra rename operation

GroupBy
=======

``` {.python .rundoc-block rundoc-language="python" rundoc-session="yes" rundoc-results="output"}
# Warning: do not import * here; only import specifically needed names
from pyspark.sql.functions import explode
from pyspark.sql.types import StructField, StructType, StringType, ArrayType
from pyspark.sql.window import Window
import pyspark.sql.functions as F
import re
from pyspark import SparkContext, SparkConf

try:
    conf = SparkConf().setAppName("dummy app name").setMaster("local")
    sc = SparkContext("local", "my app name")
except:
    pass

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

lst1 = [(i, 2 * i, 3 * i, i ** 2) for i in range(1, 5)]
rdd = sc.parallelize(lst1)
print()
print(rdd.collect())
ri = rdd.groupBy(lambda x: x[0])

print(ri.collect())
print(ri.mapValues(list).take(3))
```

\#+END~SRC~

How to take a sample of a large rdd?
====================================

  -----------------------------------------------------------------------------------------------
  sample(self, withReplacement, fraction, seed=None)
  Return a sampled subset of this RDD.
  :param withReplacement: can elements be sampled multiple times (replaced when sampled out)
  :param fraction: expected size of the sample as a fraction of this RDD's size
  without replacement: probability that each element is chosen; fraction must be \[0, 1\]
  with replacement: expected number of times each element is chosen; fraction must be &gt;= 0
  :param seed: seed for the random number generator
  &gt;&gt;&gt; rdd = sc.parallelize(range(100), 4)
  &gt;&gt;&gt; 6 &lt;= rdd.sample(False, 0.1, 81).count() &lt;= 14
  True
  sampleByKey(self, withReplacement, fractions, seed=None)
  Return a subset of this RDD sampled by key (via stratified sampling).
  Create a sample of this RDD using variable sampling rates for
  different keys as specified by fractions, a key to sampling rate map.
  &gt;&gt;&gt; fractions = {"a": 0.2, "b": 0.1}
  &gt;&gt;&gt; rdd = sc.parallelize(fractions.keys()).cartesian(sc.parallelize(range(0, 1000)))
  &gt;&gt;&gt; sample = dict(rdd.sampleByKey(False, fractions, 2).groupByKey().collect())
  &gt;&gt;&gt; 100 &lt; len(sample\["a"\]) &lt; 300 and 50 &lt; len(sample\["b"\]) &lt; 150
  True
  &gt;&gt;&gt; max(sample\["a"\]) &lt;= 999 and min(sample\["a"\]) &gt;= 0
  True
  &gt;&gt;&gt; max(sample\["b"\]) &lt;= 999 and min(sample\["b"\]) &gt;= 0
  True
  -----------------------------------------------------------------------------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

rdd1 = sc.parallelize(range(100))
#print(help(rdd1))
rdd2 = rdd1.sample(False, 0.1)
print(rdd2.collect())

l = [('Alice', 1)]
df1 = sqlContext.createDataFrame(l)
print(df1.collect())
print(help(df1))
```

How to take a sample of a large dataframe?
==========================================

  --------------------------------------------------------
  sample(self, withReplacement, fraction, seed=None)
  Returns a sampled subset of this :class:\`DataFrame\`.
  &gt;&gt;&gt; df.sample(False, 0.5, 42).count()
  2
  --------------------------------------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf
from pyspark.sql import Row
try:
   sc = SparkContext("local", "my app name")
   from pyspark.sql import SQLContext
except:
    pass
sqlContext = SQLContext(sc)

lst1 = [Row(name='Name%s' %i, age=i, height=i)  for i in range(1, 101)]
df1 = sc.parallelize(lst1).toDF()
df2 = df1.sample(False, .05)
df2.show()
```

How to save rdd as text file?
=============================

  -----------------------------------------------------------------------------------------------------
  saveAsTextFile(self, path, compressionCodecClass=None)
  Save this RDD as a text file, using string representations of elements.
  @param path: path to text file
  @param compressionCodecClass: (None by default) string i.e.
  "org.apache.hadoop.io.compress.GzipCodec"
  &gt;&gt;&gt; tempFile = NamedTemporaryFile(delete=True)
  &gt;&gt;&gt; tempFile.close()
  &gt;&gt;&gt; sc.parallelize(range(10)).saveAsTextFile(tempFile.name)
  &gt;&gt;&gt; from fileinput import input
  &gt;&gt;&gt; from glob import glob
  &gt;&gt;&gt; ''.join(sorted(input(glob(tempFile.name + "/part-0000\*"))))
  '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'
  Empty lines are tolerated when saving to text files.
  &gt;&gt;&gt; tempFile2 = NamedTemporaryFile(delete=True)
  &gt;&gt;&gt; tempFile2.close()
  &gt;&gt;&gt; sc.parallelize(\['', 'foo', '', 'bar', ''\]).saveAsTextFile(tempFile2.name)
  &gt;&gt;&gt; ''.join(sorted(input(glob(tempFile2.name + "/part-0000\*"))))
  '\n\n\nbar\nfoo\n'
  Using compressionCodecClass
  &gt;&gt;&gt; tempFile3 = NamedTemporaryFile(delete=True)
  &gt;&gt;&gt; tempFile3.close()
  &gt;&gt;&gt; codec = "org.apache.hadoop.io.compress.GzipCodec"
  &gt;&gt;&gt; sc.parallelize(\['foo', 'bar'\]).saveAsTextFile(tempFile3.name, codec)
  &gt;&gt;&gt; from fileinput import input, hook~compressed~
  &gt;&gt;&gt; result = sorted(input(glob(tempFile3.name + "/part\*.gz"), openhook=hook~compressed~))
  &gt;&gt;&gt; b''.join(result).decode('utf-8')
  u'bar\nfoo\n'
  -----------------------------------------------------------------------------------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output" rundoc-tangle="yes" rundoc-tangle="/tmp/rdd_save_as_textfile.py"}

from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
import tempfile
import os
try:
    sc = SparkContext("local", "my app name")
    from pyspark.sql import SQLContext
except:
    pass


rdd1 = sc.parallelize(range(10))

filename = '/tmp/saved'
try:
    os.remove(filename)
except:
    pass
rdd1.saveAsTextFile(filename)

```

How to save rdd to amazon s3?
=============================

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

import ConfigParser
import os

class S3ConfParser(ConfigParser.ConfigParser):

    def as_dict(self):
        d = dict(self._sections)
        for k in d:
            d[k] = dict(self._defaults, **d[k])
            d[k].pop('__name__', None)
        return d

filename = '/home/bineesh/temp/only_stored_locally/s3cfg.liang'
cp = S3ConfParser()
cp.read(filename)
AccessKey = cp.get('default', 'access_key')
SecretKey = cp.get('default', 'secret_key')
AwsBucketName = None
bucket = 'dais-ng'
directory = 'work_bineesh'
full_path = ['block_out_unsorted', 'part.txt']


path = os.path.join(directory, *full_path)


def fileAtS3Path(p, bucket=AwsBucketName):
  return 's3n://{}:{}@{}/{}'.format(AccessKey, SecretKey, bucket, p)

print(fileAtS3Path(path, bucket))

path1 = os.path.join(directory, 'to_save_rdd.txt')
print(path1)
newpath = fileAtS3Path(path1, bucket)
print(newpath)

rdd1 = sc.parallelize(range(10))
rdd1.saveAsTextFile(newpath)
'''
rdd1.saveAsTextFile(s"s3n://$AccessKey:$SecretKey@$AwsBucketName/temp.txt")
'''
```

How to create a dataframe from row?
===================================

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf
from pyspark.sql import Row
sc = SparkContext("local", "my app name")

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)
a = [Row(record_index=376549, ot=[u'vasin_S-7406-2016', u'Vasin', u'V', u'Victor', None, None, u'S-7406-2016'], cluster_id=u'vasin_S-7406-2016', profile_ut=u'WOS:000070627200023', name=u'Vasin, VA', pos=u'3', similarity=0.8161098161098161, rank=1)]

xrdd = sc.parallelize(a)
print(xrdd, type(xrdd))
xdf = xrdd.toDF()
print(xdf, type(xdf))
```

Help docstring of dataframes
============================

Help on DataFrame in module pyspark.sql.dataframe object:

class DataFrame(****builtin****.object)

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------- -------------------- ---------
  A distributed collection of data grouped into named columns.
  A :class:\`DataFrame\` is equivalent to a relational table in Spark SQL,
  and can be created using various functions in :class:\`SQLContext\`::
  people = sqlContext.read.parquet("...")
  Once created, it can be manipulated using the various domain-specific-language
  (DSL) functions defined in: :class:\`DataFrame\`, :class:\`Column\`.
  To select a column from the data frame, use the apply method::
  ageCol = people.age
  A more concrete example::
  \# To create DataFrame using SQLContext
  people = sqlContext.read.parquet("...")
  department = sqlContext.read.parquet("...")
  people.filter(people.age &gt; 30).join(department, people.deptId == department.id) .groupBy(department.name, "gender").agg({"salary": "avg", "age": "max"})
  .. versionadded:: 1.3
  Methods defined here:
  \_~getattr~\_~(self,\ name)~
  Returns the :class:\`Column\` denoted by \`\`name\`\`.
  &gt;&gt;&gt; df.select(df.age).collect()
  \[Row(age=2), Row(age=5)\]
  .. versionadded:: 1.3
  \_~getitem~\_~(self,\ item)~
  Returns the column as a :class:\`Column\`.
  &gt;&gt;&gt; df.select(df\['age'\]).collect()
  \[Row(age=2), Row(age=5)\]
  &gt;&gt;&gt; df\[ \["name", "age"\]\].collect()
  \[Row(name=u'Alice', age=2), Row(name=u'Bob', age=5)\]
  &gt;&gt;&gt; df\[ df.age &gt; 3 \].collect()
  \[Row(age=5, name=u'Bob')\]
  &gt;&gt;&gt; df\[df\[0\] &gt; 3\].collect()
  \[Row(age=5, name=u'Bob')\]
  .. versionadded:: 1.3
  \_~init~\_~(self,\ jdf,\ sql~ctx~)~
  \_~repr~\_~(self)~
  agg(self, \*exprs)
  Aggregate on the entire :class:\`DataFrame\` without groups
  (shorthand for \`\`df.groupBy.agg()\`\`).
  &gt;&gt;&gt; df.agg({"age": "max"}).collect()
  \[Row(max(age)=5)\]
  &gt;&gt;&gt; from pyspark.sql import functions as F
  &gt;&gt;&gt; df.agg(F.min(df.age)).collect()
  \[Row(min(age)=2)\]
  .. versionadded:: 1.3
  alias(self, alias)
  Returns a new :class:\`DataFrame\` with an alias set.
  &gt;&gt;&gt; from pyspark.sql.functions import \*
  &gt;&gt;&gt; df~as1~ = df.alias("df~as1~")
  &gt;&gt;&gt; df~as2~ = df.alias("df~as2~")
  &gt;&gt;&gt; joined~df~ = df~as1~.join(df~as2~, col("df~as1~.name") == col("df~as2~.name"), 'inner')
  &gt;&gt;&gt; joined~df~.select("df~as1~.name", "df~as2~.name", "df~as2~.age").collect()
  \[Row(name=u'Bob', name=u'Bob', age=5), Row(name=u'Alice', name=u'Alice', age=2)\]
  .. versionadded:: 1.3
  approxQuantile(self, col, probabilities, relativeError)
  Calculates the approximate quantiles of a numerical column of a
  DataFrame.
  The result of this algorithm has the following deterministic bound:
  If the DataFrame has N elements and if we request the quantile at
  probability \`p\` up to error \`err\`, then the algorithm will return
  a sample \`x\` from the DataFrame so that the **exact** rank of \`x\` is
  close to (p \* N). More precisely,
  floor((p - err) \* N) &lt;= rank(x) &lt;= ceil((p + err) \* N).
  This method implements a variation of the Greenwald-Khanna
  algorithm (with some speed optimizations). The algorithm was first
  present in \[\[<http://dx.doi.org/10.1145/375663.375670>
  Space-efficient Online Computation of Quantile Summaries\]\]
  by Greenwald and Khanna.
  :param col: the name of the numerical column
  :param probabilities: a list of quantile probabilities
  Each number must belong to \[0, 1\].
  For example 0 is the minimum, 0.5 is the median, 1 is the maximum.
  :param relativeError: The relative target precision to achieve
  (&gt;= 0). If set to zero, the exact quantiles are computed, which
  could be very expensive. Note that values greater than 1 are
  accepted but give the same result as 1.
  :return: the approximate quantiles at the given probabilities
  .. versionadded:: 2.0
  cache(self)
  Persists with the default storage level (C{MEMORY~ONLY~}).
  .. versionadded:: 1.3
  coalesce(self, numPartitions)
  Returns a new :class:\`DataFrame\` that has exactly \`numPartitions\` partitions.
  Similar to coalesce defined on an :class:\`RDD\`, this operation results in a
  narrow dependency, e.g. if you go from 1000 partitions to 100 partitions,
  there will not be a shuffle, instead each of the 100 new partitions will
  claim 10 of the current partitions.
  &gt;&gt;&gt; df.coalesce(1).rdd.getNumPartitions()
  1
  .. versionadded:: 1.4
  collect(self)
  Returns all the records as a list of :class:\`Row\`.
  &gt;&gt;&gt; df.collect()
  \[Row(age=2, name=u'Alice'), Row(age=5, name=u'Bob')\]
  .. versionadded:: 1.3
  corr(self, col1, col2, method=None)
  Calculates the correlation of two columns of a DataFrame as a double value.
  Currently only supports the Pearson Correlation Coefficient.
  :func:\`DataFrame.corr\` and :func:\`DataFrameStatFunctions.corr\` are aliases of each other.
  :param col1: The name of the first column
  :param col2: The name of the second column
  :param method: The correlation method. Currently only supports "pearson"
  .. versionadded:: 1.4
  count(self)
  Returns the number of rows in this :class:\`DataFrame\`.
  &gt;&gt;&gt; df.count()
  2
  .. versionadded:: 1.3
  cov(self, col1, col2)
  Calculate the sample covariance for the given columns, specified by their names, as a
  double value. :func:\`DataFrame.cov\` and :func:\`DataFrameStatFunctions.cov\` are aliases.
  :param col1: The name of the first column
  :param col2: The name of the second column
  .. versionadded:: 1.4
  createOrReplaceTempView(self, name)
  Creates or replaces a temporary view with this DataFrame.
  The lifetime of this temporary table is tied to the :class:\`SparkSession\`
  that was used to create this :class:\`DataFrame\`.
  &gt;&gt;&gt; df.createOrReplaceTempView("people")
  &gt;&gt;&gt; df2 = df.filter(df.age &gt; 3)
  &gt;&gt;&gt; df2.createOrReplaceTempView("people")
  &gt;&gt;&gt; df3 = spark.sql("select \* from people")
  &gt;&gt;&gt; sorted(df3.collect()) == sorted(df2.collect())
  True
  &gt;&gt;&gt; spark.catalog.dropTempView("people")
  .. versionadded:: 2.0
  createTempView(self, name)
  Creates a temporary view with this DataFrame.
  The lifetime of this temporary table is tied to the :class:\`SparkSession\`
  that was used to create this :class:\`DataFrame\`.
  throws :class:\`TempTableAlreadyExistsException\`, if the view name already exists in the
  catalog.
  &gt;&gt;&gt; df.createTempView("people")
  &gt;&gt;&gt; df2 = spark.sql("select \* from people")
  &gt;&gt;&gt; sorted(df.collect()) == sorted(df2.collect())
  True
  &gt;&gt;&gt; df.createTempView("people") \# doctest: +IGNORE~EXCEPTIONDETAIL~
  Traceback (most recent call last):
  ...
  AnalysisException: u"Temporary table 'people' already exists;"
  &gt;&gt;&gt; spark.catalog.dropTempView("people")
  .. versionadded:: 2.0
  crosstab(self, col1, col2)
  Computes a pair-wise frequency table of the given columns. Also known as a contingency
  table. The number of distinct values for each column should be less than 1e4. At most 1e6
  non-zero pair frequencies will be returned.
  The first column of each row will be the distinct values of \`col1\` and the column names
  will be the distinct values of \`col2\`. The name of the first column will be \`\$col1\_\$col2\`.
  Pairs that have no occurrences will have zero as their counts.
  :func:\`DataFrame.crosstab\` and :func:\`DataFrameStatFunctions.crosstab\` are aliases.
  :param col1: The name of the first column. Distinct items will make the first item of
  each row.
  :param col2: The name of the second column. Distinct items will make the column names
  of the DataFrame.
  .. versionadded:: 1.4
  cube(self, \*cols)
  Create a multi-dimensional cube for the current :class:\`DataFrame\` using
  the specified columns, so we can run aggregation on them.
  &gt;&gt;&gt; df.cube("name", df.age).count().orderBy("name", "age").show()
  ~~-----~~----+-----+
  ~~-----~~----+-----+
  ~~-----~~----+-----+
  .. versionadded:: 1.4
  describe(self, \*cols)
  Computes statistics for numeric columns.
  This include count, mean, stddev, min, and max. If no columns are
  given, this function computes statistics for all numerical columns.
  .. note:: This function is meant for exploratory data analysis, as we make no guarantee about the backward compatibility of the schema of the resulting DataFrame.
  &gt;&gt;&gt; df.describe().show()
  ~~-------~~------------------+
  ~~-------~~------------------+
  ~~-------~~------------------+
  &gt;&gt;&gt; df.describe(\['age', 'name'\]).show()
  ~~-------~~------------------+-----+
  ~~-------~~------------------+-----+
  ~~-------~~------------------+-----+
  .. versionadded:: 1.3.1
  distinct(self)
  Returns a new :class:\`DataFrame\` containing the distinct rows in this :class:\`DataFrame\`.
  &gt;&gt;&gt; df.distinct().count()
  2
  .. versionadded:: 1.3
  drop(self, col)
  Returns a new :class:\`DataFrame\` that drops the specified column.
  :param col: a string name of the column to drop, or a
  :class:\`Column\` to drop.
  &gt;&gt;&gt; df.drop('age').collect()
  \[Row(name=u'Alice'), Row(name=u'Bob')\]
  &gt;&gt;&gt; df.drop(df.age).collect()
  \[Row(name=u'Alice'), Row(name=u'Bob')\]
  &gt;&gt;&gt; df.join(df2, df.name == df2.name, 'inner').drop(df.name).collect()
  \[Row(age=5, height=85, name=u'Bob')\]
  &gt;&gt;&gt; df.join(df2, df.name == df2.name, 'inner').drop(df2.name).collect()
  \[Row(age=5, name=u'Bob', height=85)\]
  .. versionadded:: 1.4
  dropDuplicates(self, subset=None)
  Return a new :class:\`DataFrame\` with duplicate rows removed,
  optionally only considering certain columns.
  :func:\`drop~duplicates~\` is an alias for :func:\`dropDuplicates\`.
  &gt;&gt;&gt; from pyspark.sql import Row
  &gt;&gt;&gt; df = sc.parallelize(\[ \
  ... Row(name='Alice', age=5, height=80), \
  ... Row(name='Alice', age=5, height=80), \
  ... Row(name='Alice', age=10, height=80)\]).toDF()
  &gt;&gt;&gt; df.dropDuplicates().show()
  ~~---~~------+-----+
  ~~---~~------+-----+
  ~~---~~------+-----+
  &gt;&gt;&gt; df.dropDuplicates(\['name', 'height'\]).show()
  ~~---~~------+-----+
  ~~---~~------+-----+
  ~~---~~------+-----+
  .. versionadded:: 1.4
  drop~duplicates~ = dropDuplicates(self, subset=None)
  :func:\`drop~duplicates~\` is an alias for :func:\`dropDuplicates\`.
  .. versionadded:: 1.4
  dropna(self, how='any', thresh=None, subset=None)
  Returns a new :class:\`DataFrame\` omitting rows with null values.
  :func:\`DataFrame.dropna\` and :func:\`DataFrameNaFunctions.drop\` are aliases of each other.
  :param how: 'any' or 'all'.
  If 'any', drop a row if it contains any nulls.
  If 'all', drop a row only if all its values are null.
  :param thresh: int, default None
  If specified, drop rows that have less than \`thresh\` non-null values.
  This overwrites the \`how\` parameter.
  :param subset: optional list of column names to consider.
  &gt;&gt;&gt; df4.na.drop().show()
  ~~---~~------+-----+
  ~~---~~------+-----+
  ~~---~~------+-----+
  .. versionadded:: 1.3.1
  explain(self, extended=False)
  Prints the (logical and physical) plans to the console for debugging purpose.
  :param extended: boolean, default \`\`False\`\`. If \`\`False\`\`, prints only the physical plan.
  &gt;&gt;&gt; df.explain()
  == Physical Plan ==
  Scan ExistingRDD\[age\#0,name\#1\]
  &gt;&gt;&gt; df.explain(True)
  == Parsed Logical Plan ==
  ...
  == Analyzed Logical Plan ==
  ...
  == Optimized Logical Plan ==
  ...
  == Physical Plan ==
  ...
  .. versionadded:: 1.3
  fillna(self, value, subset=None)
  Replace null values, alias for \`\`na.fill()\`\`.
  :func:\`DataFrame.fillna\` and :func:\`DataFrameNaFunctions.fill\` are aliases of each other.
  :param value: int, long, float, string, or dict.
  Value to replace null values with.
  If the value is a dict, then \`subset\` is ignored and \`value\` must be a mapping
  from column name (string) to replacement value. The replacement value must be
  an int, long, float, or string.
  :param subset: optional list of column names to consider.
  Columns specified in subset that do not have matching data type are ignored.
  For example, if \`value\` is a string, and subset contains a non-string column,
  then the non-string column is simply ignored.
  &gt;&gt;&gt; df4.na.fill(50).show()
  ~~---~~------+-----+
  ~~---~~------+-----+
  ~~---~~------+-----+
  &gt;&gt;&gt; df4.na.fill({'age': 50, 'name': 'unknown'}).show()
  ~~---~~------+-------+
  ~~---~~------+-------+
  ~~---~~------+-------+
  .. versionadded:: 1.3.1
  filter(self, condition)
  Filters rows using the given condition.
  :func:\`where\` is an alias for :func:\`filter\`.
  :param condition: a :class:\`Column\` of :class:\`types.BooleanType\`
  or a string of SQL expression.
  &gt;&gt;&gt; df.filter(df.age &gt; 3).collect()
  \[Row(age=5, name=u'Bob')\]
  &gt;&gt;&gt; df.where(df.age == 2).collect()
  \[Row(age=2, name=u'Alice')\]
  &gt;&gt;&gt; df.filter("age &gt; 3").collect()
  \[Row(age=5, name=u'Bob')\]
  &gt;&gt;&gt; df.where("age = 2").collect()
  \[Row(age=2, name=u'Alice')\]
  .. versionadded:: 1.3
  first(self)
  Returns the first row as a :class:\`Row\`.
  &gt;&gt;&gt; df.first()
  Row(age=2, name=u'Alice')
  .. versionadded:: 1.3
  foreach(self, f)
  Applies the \`\`f\`\` function to all :class:\`Row\` of this :class:\`DataFrame\`.
  This is a shorthand for \`\`df.rdd.foreach()\`\`.
  &gt;&gt;&gt; def f(person):
  ... print(person.name)
  &gt;&gt;&gt; df.foreach(f)
  .. versionadded:: 1.3
  foreachPartition(self, f)
  Applies the \`\`f\`\` function to each partition of this :class:\`DataFrame\`.
  This a shorthand for \`\`df.rdd.foreachPartition()\`\`.
  &gt;&gt;&gt; def f(people):
  ... for person in people:
  ... print(person.name)
  &gt;&gt;&gt; df.foreachPartition(f)
  .. versionadded:: 1.3
  freqItems(self, cols, support=None)
  Finding frequent items for columns, possibly with false positives. Using the
  frequent element count algorithm described in
  "<http://dx.doi.org/10.1145/762471.762473>, proposed by Karp, Schenker, and Papadimitriou".
  :func:\`DataFrame.freqItems\` and :func:\`DataFrameStatFunctions.freqItems\` are aliases.
  .. note:: This function is meant for exploratory data analysis, as we make no guarantee about the backward compatibility of the schema of the resulting DataFrame.
  :param cols: Names of the columns to calculate frequent items for as a list or tuple of
  strings.
  :param support: The frequency with which to consider an item 'frequent'. Default is 1%.
  The support must be greater than 1e-4.
  .. versionadded:: 1.4
  groupBy(self, \*cols)
  Groups the :class:\`DataFrame\` using the specified columns,
  so we can run aggregation on them. See :class:\`GroupedData\`
  for all the available aggregate functions.
  :func:\`groupby\` is an alias for :func:\`groupBy\`.
  :param cols: list of columns to group by.
  Each element should be a column name (string) or an expression (:class:\`Column\`).
  &gt;&gt;&gt; df.groupBy().avg().collect()
  \[Row(avg(age)=3.5)\]
  &gt;&gt;&gt; sorted(df.groupBy('name').agg({'age': 'mean'}).collect())
  \[Row(name=u'Alice', avg(age)=2.0), Row(name=u'Bob', avg(age)=5.0)\]
  &gt;&gt;&gt; sorted(df.groupBy(df.name).avg().collect())
  \[Row(name=u'Alice', avg(age)=2.0), Row(name=u'Bob', avg(age)=5.0)\]
  &gt;&gt;&gt; sorted(df.groupBy(\['name', df.age\]).count().collect())
  \[Row(name=u'Alice', age=2, count=1), Row(name=u'Bob', age=5, count=1)\]
  .. versionadded:: 1.3
  groupby = groupBy(self, \*cols)
  :func:\`groupby\` is an alias for :func:\`groupBy\`.
  .. versionadded:: 1.4
  head(self, n=None)
  Returns the first \`\`n\`\` rows.
  Note that this method should only be used if the resulting array is expected
  to be small, as all the data is loaded into the driver's memory.
  :param n: int, default 1. Number of rows to return.
  :return: If n is greater than 1, return a list of :class:\`Row\`.
  If n is 1, return a single Row.
  &gt;&gt;&gt; df.head()
  Row(age=2, name=u'Alice')
  &gt;&gt;&gt; df.head(1)
  \[Row(age=2, name=u'Alice')\]
  .. versionadded:: 1.3
  intersect(self, other)
  Return a new :class:\`DataFrame\` containing rows only in
  both this frame and another frame.
  This is equivalent to \`INTERSECT\` in SQL.
  .. versionadded:: 1.3
  isLocal(self)
  Returns \`\`True\`\` if the :func:\`collect\` and :func:\`take\` methods can be run locally
  (without any Spark executors).
  .. versionadded:: 1.3
  join(self, other, on=None, how=None)
  Joins with another :class:\`DataFrame\`, using the given join expression.
  :param other: Right side of the join
  :param on: a string for the join column name, a list of column names,
  a join expression (Column), or a list of Columns.
  If \`on\` is a string or a list of strings indicating the name of the join column(s),
  the column(s) must exist on both sides, and this performs an equi-join.
  :param how: str, default 'inner'.
  One of \`inner\`, \`outer\`, \`left~outer~\`, \`right~outer~\`, \`leftsemi\`.
  The following performs a full outer join between \`\`df1\`\` and \`\`df2\`\`.
  &gt;&gt;&gt; df.join(df2, df.name == df2.name, 'outer').select(df.name, df2.height).collect()
  \[Row(name=None, height=80), Row(name=u'Bob', height=85), Row(name=u'Alice', height=None)\]
  &gt;&gt;&gt; df.join(df2, 'name', 'outer').select('name', 'height').collect()
  \[Row(name=u'Tom', height=80), Row(name=u'Bob', height=85), Row(name=u'Alice', height=None)\]
  &gt;&gt;&gt; cond = \[df.name == df3.name, df.age == df3.age\]
  &gt;&gt;&gt; df.join(df3, cond, 'outer').select(df.name, df3.age).collect()
  \[Row(name=u'Alice', age=2), Row(name=u'Bob', age=5)\]
  &gt;&gt;&gt; df.join(df2, 'name').select(df.name, df2.height).collect()
  \[Row(name=u'Bob', height=85)\]
  &gt;&gt;&gt; df.join(df4, \['name', 'age'\]).select(df.name, df.age).collect()
  \[Row(name=u'Bob', age=5)\]
  .. versionadded:: 1.3
  limit(self, num)
  Limits the result count to the number specified.
  &gt;&gt;&gt; df.limit(1).collect()
  \[Row(age=2, name=u'Alice')\]
  &gt;&gt;&gt; df.limit(0).collect()
  \[\]
  .. versionadded:: 1.3
  orderBy = sort(self, \*cols, \*\*kwargs)
  persist(self, storageLevel=StorageLevel(False, True, False, False, 1))
  Sets the storage level to persist its values across operations
  after the first time it is computed. This can only be used to assign
  a new storage level if the RDD does not have a storage level set yet.
  If no storage level is specified defaults to (C{MEMORY~ONLY~}).
  .. versionadded:: 1.3
  printSchema(self)
  Prints out the schema in the tree format.
  &gt;&gt;&gt; df.printSchema()
  root
  &lt;BLANKLINE&gt;
  .. versionadded:: 1.3
  randomSplit(self, weights, seed=None)
  Randomly splits this :class:\`DataFrame\` with the provided weights.
  :param weights: list of doubles as weights with which to split the DataFrame. Weights will
  be normalized if they don't sum up to 1.0.
  :param seed: The seed for sampling.
  &gt;&gt;&gt; splits = df4.randomSplit(\[1.0, 2.0\], 24)
  &gt;&gt;&gt; splits\[0\].count()
  1
  &gt;&gt;&gt; splits\[1\].count()
  3
  .. versionadded:: 1.4
  registerTempTable(self, name)
  Registers this RDD as a temporary table using the given name.
  The lifetime of this temporary table is tied to the :class:\`SQLContext\`
  that was used to create this :class:\`DataFrame\`.
  &gt;&gt;&gt; df.registerTempTable("people")
  &gt;&gt;&gt; df2 = spark.sql("select \* from people")
  &gt;&gt;&gt; sorted(df.collect()) == sorted(df2.collect())
  True
  &gt;&gt;&gt; spark.catalog.dropTempView("people")
  .. note:: Deprecated in 2.0, use createOrReplaceTempView instead.
  .. versionadded:: 1.3
  repartition(self, numPartitions, \*cols)
  Returns a new :class:\`DataFrame\` partitioned by the given partitioning expressions. The
  resulting DataFrame is hash partitioned.
  \`\`numPartitions\`\` can be an int to specify the target number of partitions or a Column.
  If it is a Column, it will be used as the first partitioning column. If not specified,
  the default number of partitions is used.
  .. versionchanged:: 1.6
  Added optional arguments to specify the partitioning columns. Also made numPartitions
  optional if partitioning columns are specified.
  &gt;&gt;&gt; df.repartition(10).rdd.getNumPartitions()
  10
  &gt;&gt;&gt; data = df.union(df).repartition("age")
  &gt;&gt;&gt; data.show()
  ~~---~~-----+
  ~~---~~-----+
  ~~---~~-----+
  &gt;&gt;&gt; data = data.repartition(7, "age")
  &gt;&gt;&gt; data.show()
  ~~---~~-----+
  ~~---~~-----+
  ~~---~~-----+
  &gt;&gt;&gt; data.rdd.getNumPartitions()
  7
  &gt;&gt;&gt; data = data.repartition("name", "age")
  &gt;&gt;&gt; data.show()
  ~~---~~-----+
  ~~---~~-----+
  ~~---~~-----+
  .. versionadded:: 1.3
  replace(self, to~replace~, value, subset=None)
  Returns a new :class:\`DataFrame\` replacing a value with another value.
  :func:\`DataFrame.replace\` and :func:\`DataFrameNaFunctions.replace\` are
  aliases of each other.
  :param to~replace~: int, long, float, string, or list.
  Value to be replaced.
  If the value is a dict, then \`value\` is ignored and \`to~replace~\` must be a
  mapping from column name (string) to replacement value. The value to be
  replaced must be an int, long, float, or string.
  :param value: int, long, float, string, or list.
  Value to use to replace holes.
  The replacement value must be an int, long, float, or string. If \`value\` is a
  list or tuple, \`value\` should be of the same length with \`to~replace~\`.
  :param subset: optional list of column names to consider.
  Columns specified in subset that do not have matching data type are ignored.
  For example, if \`value\` is a string, and subset contains a non-string column,
  then the non-string column is simply ignored.
  &gt;&gt;&gt; df4.na.replace(10, 20).show()
  ~~----~~------+-----+
  ~~----~~------+-----+
  ~~----~~------+-----+
  &gt;&gt;&gt; df4.na.replace(\['Alice', 'Bob'\], \['A', 'B'\], 'name').show()
  ~~----~~------+----+
  ~~----~~------+----+
  ~~----~~------+----+
  .. versionadded:: 1.4
  rollup(self, \*cols)
  Create a multi-dimensional rollup for the current :class:\`DataFrame\` using
  the specified columns, so we can run aggregation on them.
  &gt;&gt;&gt; df.rollup("name", df.age).count().orderBy("name", "age").show()
  ~~-----~~----+-----+
  ~~-----~~----+-----+
  ~~-----~~----+-----+
  .. versionadded:: 1.4
  sample(self, withReplacement, fraction, seed=None)
  Returns a sampled subset of this :class:\`DataFrame\`.
  &gt;&gt;&gt; df.sample(False, 0.5, 42).count()
  2
  .. versionadded:: 1.3
  sampleBy(self, col, fractions, seed=None)
  Returns a stratified sample without replacement based on the
  fraction given on each stratum.
  :param col: column that defines strata
  :param fractions:
  sampling fraction for each stratum. If a stratum is not
  specified, we treat its fraction as zero.
  :param seed: random seed
  :return: a new DataFrame that represents the stratified sample
  &gt;&gt;&gt; from pyspark.sql.functions import col
  &gt;&gt;&gt; dataset = sqlContext.range(0, 100).select((col("id") % 3).alias("key"))
  &gt;&gt;&gt; sampled = dataset.sampleBy("key", fractions={0: 0.1, 1: 0.2}, seed=0)
  &gt;&gt;&gt; sampled.groupBy("key").count().orderBy("key").show()
  ~~---~~-----+
  ~~---~~-----+
  ~~---~~-----+
  .. versionadded:: 1.5
  select(self, \*cols)
  Projects a set of expressions and returns a new :class:\`DataFrame\`.
  :param cols: list of column names (string) or expressions (:class:\`Column\`).
  If one of the column names is '\*', that column is expanded to include all columns
  in the current DataFrame.
  &gt;&gt;&gt; df.select('\*').collect()
  \[Row(age=2, name=u'Alice'), Row(age=5, name=u'Bob')\]
  &gt;&gt;&gt; df.select('name', 'age').collect()
  \[Row(name=u'Alice', age=2), Row(name=u'Bob', age=5)\]
  &gt;&gt;&gt; df.select(df.name, (df.age + 10).alias('age')).collect()
  \[Row(name=u'Alice', age=12), Row(name=u'Bob', age=15)\]
  .. versionadded:: 1.3
  selectExpr(self, \*expr)
  Projects a set of SQL expressions and returns a new :class:\`DataFrame\`.
  This is a variant of :func:\`select\` that accepts SQL expressions.
  &gt;&gt;&gt; df.selectExpr("age \* 2", "abs(age)").collect()
  \[Row((age \* 2)=4, abs(age)=2), Row((age \* 2)=10, abs(age)=5)\]
  .. versionadded:: 1.3
  show(self, n=20, truncate=True)
  Prints the first \`\`n\`\` rows to the console.
  :param n: Number of rows to show.
  :param truncate: Whether truncate long strings and align cells right.
  &gt;&gt;&gt; df
  DataFrame\[age: int, name: string\]
  &gt;&gt;&gt; df.show()
  ~~---~~-----+
  ~~---~~-----+
  ~~---~~-----+
  .. versionadded:: 1.3
  sort(self, \*cols, \*\*kwargs)
  Returns a new :class:\`DataFrame\` sorted by the specified column(s).
  :param cols: list of :class:\`Column\` or column names to sort by.
  :param ascending: boolean or list of boolean (default True).
  Sort ascending vs. descending. Specify list for multiple sort orders.
  If a list is specified, length of the list must equal length of the \`cols\`.
  &gt;&gt;&gt; df.sort(df.age.desc()).collect()
  \[Row(age=5, name=u'Bob'), Row(age=2, name=u'Alice')\]
  &gt;&gt;&gt; df.sort("age", ascending=False).collect()
  \[Row(age=5, name=u'Bob'), Row(age=2, name=u'Alice')\]
  &gt;&gt;&gt; df.orderBy(df.age.desc()).collect()
  \[Row(age=5, name=u'Bob'), Row(age=2, name=u'Alice')\]
  &gt;&gt;&gt; from pyspark.sql.functions import \*
  &gt;&gt;&gt; df.sort(asc("age")).collect()
  \[Row(age=2, name=u'Alice'), Row(age=5, name=u'Bob')\]
  &gt;&gt;&gt; df.orderBy(desc("age"), "name").collect()
  \[Row(age=5, name=u'Bob'), Row(age=2, name=u'Alice')\]
  &gt;&gt;&gt; df.orderBy(\["age", "name"\], ascending=\[0, 1\]).collect()
  \[Row(age=5, name=u'Bob'), Row(age=2, name=u'Alice')\]
  .. versionadded:: 1.3
  sortWithinPartitions(self, \*cols, \*\*kwargs)
  Returns a new :class:\`DataFrame\` with each partition sorted by the specified column(s).
  :param cols: list of :class:\`Column\` or column names to sort by.
  :param ascending: boolean or list of boolean (default True).
  Sort ascending vs. descending. Specify list for multiple sort orders.
  If a list is specified, length of the list must equal length of the \`cols\`.
  &gt;&gt;&gt; df.sortWithinPartitions("age", ascending=False).show()
  ~~---~~-----+
  ~~---~~-----+
  ~~---~~-----+
  .. versionadded:: 1.6
  subtract(self, other)
  Return a new :class:\`DataFrame\` containing rows in this frame
  but not in another frame.
  This is equivalent to \`EXCEPT\` in SQL.
  .. versionadded:: 1.3
  take(self, num)
  Returns the first \`\`num\`\` rows as a :class:\`list\` of :class:\`Row\`.
  &gt;&gt;&gt; df.take(2)
  \[Row(age=2, name=u'Alice'), Row(age=5, name=u'Bob')\]
  .. versionadded:: 1.3
  toDF(self, \*cols)
  Returns a new class:\`DataFrame\` that with new specified column names
  :param cols: list of new column names (string)
  &gt;&gt;&gt; df.toDF('f1', 'f2').collect()
  \[Row(f1=2, f2=u'Alice'), Row(f1=5, f2=u'Bob')\]
  toJSON(self, use~unicode~=True)
  Converts a :class:\`DataFrame\` into a :class:\`RDD\` of string.
  Each row is turned into a JSON document as one element in the returned RDD.
  &gt;&gt;&gt; df.toJSON().first()
  u'{"age":2,"name":"Alice"}'
  .. versionadded:: 1.3
  toLocalIterator(self)
  Returns an iterator that contains all of the rows in this :class:\`DataFrame\`.
  The iterator will consume as much memory as the largest partition in this DataFrame.
  &gt;&gt;&gt; list(df.toLocalIterator())
  \[Row(age=2, name=u'Alice'), Row(age=5, name=u'Bob')\]
  .. versionadded:: 2.0
  toPandas(self)
  Returns the contents of this :class:\`DataFrame\` as Pandas \`\`pandas.DataFrame\`\`.
  Note that this method should only be used if the resulting Pandas's DataFrame is expected
  to be small, as all the data is loaded into the driver's memory.
  This is only available if Pandas is installed and available.
  &gt;&gt;&gt; df.toPandas() \# doctest: +SKIP
  age name
  0 2 Alice
  1 5 Bob
  .. versionadded:: 1.3
  union(self, other)
  Return a new :class:\`DataFrame\` containing union of rows in this
  frame and another frame.
  This is equivalent to \`UNION ALL\` in SQL. To do a SQL-style set union
  (that does deduplication of elements), use this function followed by a distinct.
  .. versionadded:: 2.0
  unionAll(self, other)
  Return a new :class:\`DataFrame\` containing union of rows in this
  frame and another frame.
  .. note:: Deprecated in 2.0, use union instead.
  .. versionadded:: 1.3
  unpersist(self, blocking=False)
  Marks the :class:\`DataFrame\` as non-persistent, and remove all blocks for it from
  memory and disk.
  .. note:: \`blocking\` default has changed to False to match Scala in 2.0.
  .. versionadded:: 1.3
  where = filter(self, condition)
  :func:\`where\` is an alias for :func:\`filter\`.
  .. versionadded:: 1.3
  withColumn(self, colName, col)
  Returns a new :class:\`DataFrame\` by adding a column or replacing the
  existing column that has the same name.
  :param colName: string, name of the new column.
  :param col: a :class:\`Column\` expression for the new column.
  &gt;&gt;&gt; df.withColumn('age2', df.age + 2).collect()
  \[Row(age=2, name=u'Alice', age2=4), Row(age=5, name=u'Bob', age2=7)\]
  .. versionadded:: 1.3
  withColumnRenamed(self, existing, new)
  Returns a new :class:\`DataFrame\` by renaming an existing column.
  :param existing: string, name of the existing column to rename.
  :param col: string, new name of the column.
  &gt;&gt;&gt; df.withColumnRenamed('age', 'age2').collect()
  \[Row(age2=2, name=u'Alice'), Row(age2=5, name=u'Bob')\]
  .. versionadded:: 1.3
  ----------------------------------------------------------------------
  Data descriptors defined here:
  ****dict****
  dictionary for instance variables (if defined)
  ****weakref****
  list of weak references to the object (if defined)
  columns
  Returns all column names as a list.
  &gt;&gt;&gt; df.columns
  \['age', 'name'\]
  .. versionadded:: 1.3
  dtypes
  Returns all column names and their data types as a list.
  &gt;&gt;&gt; df.dtypes
  \[('age', 'int'), ('name', 'string')\]
  .. versionadded:: 1.3
  isStreaming
  Returns true if this :class:\`Dataset\` contains one or more sources that continuously
  return data as it arrives. A :class:\`Dataset\` that reads data from a streaming source
  must be executed as a :class:\`StreamingQuery\` using the :func:\`start\` method in
  :class:\`DataStreamWriter\`. Methods that return a single answer, (e.g., :func:\`count\` or
  :func:\`collect\`) will throw an :class:\`AnalysisException\` when there is a streaming
  source present.
  .. note:: Experimental
  .. versionadded:: 2.0
  na
  Returns a :class:\`DataFrameNaFunctions\` for handling missing values.
  .. versionadded:: 1.3.1
  rdd
  Returns the content as an :class:\`pyspark.RDD\` of :class:\`Row\`.
  .. versionadded:: 1.3
  schema
  Returns the schema of this :class:\`DataFrame\` as a :class:\`types.StructType\`.
  &gt;&gt;&gt; df.schema
  StructType(List(StructField(age,IntegerType,true),StructField(name,StringType,true)))
  .. versionadded:: 1.3
  stat
  Returns a :class:\`DataFrameStatFunctions\` for statistic functions.
  .. versionadded:: 1.4
  write
  Interface for saving the content of the non-streaming :class:\`DataFrame\` out into external
  storage.
  :return: :class:\`DataFrameWriter\`
  .. versionadded:: 1.4
  writeStream
  Interface for saving the content of the streaming :class:\`DataFrame\` out into external
  storage.
  .. note:: Experimental.
  :return: :class:\`DataStreamWriter\`
  .. versionadded:: 2.0
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------- -------------------- ---------

Read from csv idea
==================

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output" rundoc-tangle="yes" rundoc-tangle="/tmp/read_from_csv.py"}

from pyspark import SparkContext, SparkConf
try:
    sc = SparkContext("local", "my app name")
    from pyspark.sql import SQLContext
    sqlContext = SQLContext(sc)
except:
    pass

filename = '/tmp/daisng_cluster1.csv'

first_cluster = """A\t01-01|02-02|03-03|04-04
B\t05-05|06-06|07-07|08-08
C\t10-10|11-11
Z\t50-50
"""

def write_cluster(filename, filecontents):
    """
    Writes filecontents (string) to filename
    """
    with open(filename, 'w') as f:
        f.write(filecontents)


write_cluster(filename, first_cluster)

def cluster_read_helper(x):
    a, b = x.split('\t')
    c = b.split('|')
    return [[a, d] for d in c]

rdd1 = sc.textFile(filename)
rdd2 = rdd1.flatMap(lambda x: cluster_read_helper(x))
daisng_cluster_jan2017 = rdd2.toDF(['daisngid','item'])
daisng_cluster_jan2017.show()
```

Convert the blockout output to data frame
=========================================

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output" rundoc-tangle="yes" rundoc-tangle="/tmp/find_clusters_in_real_name.py"}
from pyspark import SparkContext, SparkConf
from pyspark.sql.types import *
from pyspark.sql.functions import udf
from pyspark.sql import functions as F

try:
    sc = SparkContext("local", "my app name")
    from pyspark.sql import SQLContext
    sqlContext = SQLContext(sc)
except:
  pass


def get_daisng_cluster_test_data():
  cluster_filename = '/tmp/daisng_cluster1.csv'

  first_cluster = """A\t01-01|02-02|03-03|04-04
  B\t05-05|06-06|07-07|08-08
  C\t10-10|11-11
  D\tWOS:000250933800019-3
  Z\t50-50"""
  return cluster_filename, first_cluster


def get_blockout_test_data():
  filename = '/tmp/block_out1.csv'

  block_out_string = """wang_y|304574466WOS1/WOS:000248320000087|2|<name dais_id="15657181" daisng_id="28404544" role="author" seq_no="2"><display_name>Wang, Y.</display_name><full_name>Wang, Y.</full_name><wos_standard>Wang, Y</wos_standard><first_name>Y.</first_name><last_name>Wang</last_name></name>||145683,26137801,145572,44449635,45283969,289327878,9607544,769652,77425829,8273236,38096655,997172,40304141,3163273,11793431,53592067,1090236,146904,5817362,2540183,3028941,5904152,57964622,6130089,321673869,39602203,771533,54275596,29200373,1001617,2623595,37904495,3963808,704559,147769,54261196,1015906,6354149,3180684,65249584,1091149,287425517,46686151,57532498,148850
  wang_y|79358886WOS1/WOS:000250933800019|3|<name dais_id="15806918" daisng_id="89384565" reprint="Y" role="author" seq_no="3"><display_name>Wang, Yuesi</display_name><full_name>Wang, Yuesi</full_name><wos_standard>Wang, YS</wos_standard><first_name>Yuesi</first_name><last_name>Wang</last_name><email_addr>wys@dq.cern.ac.cn</email_addr></name>|wys@dq.cern.ac.cn|57634036,4292101,17525689,76804443,79358939,46888289,674726,875651,59633537,372178,675737,45209525,79358996,1997459,2381233,2970196,32150724,56971715,10190930,41007706,79359078,73327323,48406428,675865,4477203,2325818,55581992,45546408,322531529,2382077,76806739,79359183,287446226,79359202,73915327,79359237,79359241,43102338,79359257"""

  return filename, block_out_string

def get_ut(fuid_slash_ut):
    """
    Given fuid_slash_ut
    returns everything after /
    fuid/wos:ut-position
    ie: returns wos:ut-position
    """
    try:
        value = fuid_slash_ut.split('/')[1]
    except IndexError:
        value = fuid_slash_ut
    return value

get_ut_udf = udf(get_ut, StringType())


def write_cluster(filename, filecontents):
  """
  Writes filecontents (string) to filename
  """
  with open(filename, 'w') as f:
    f.write(filecontents)

def cluster_read_helper(x):
    a, b = x.split('\t')
    c = b.split('|')
    return [[a, d] for d in c]


def generate_daisng_cluster_test_data():
  cluster_filename, first_cluster = get_daisng_cluster_test_data()
  write_cluster(cluster_filename, first_cluster)
  rdd1 = sc.textFile(cluster_filename)
  rdd2 = rdd1.flatMap(lambda x: cluster_read_helper(x))
  daisng_clusters_df = rdd2.toDF(['daisngid','item'])
  daisng_clusters_df.show()
  return daisng_clusters_df



def block_reader_helper(x):
  c = x.split('|')
  return [c]


def generate_daisng_blockout_test_data():
    filename, block_out_string = get_blockout_test_data()
    write_cluster(filename, block_out_string)

    rdd1 = sc.textFile(filename)
    rdd2 = rdd1.flatMap(lambda x: block_reader_helper(x))
    block_out_df = (rdd2
                  .toDF(['blockid', 'fuid', 'pos', 'xml', 'email', 'citations']
                        )
                  )
    block_out_df.show()
    a_block_out_df = (block_out_df
                    .select('blockid',
                            get_ut_udf(F.col('fuid')),
                            'pos',
                            'xml',
                            'email')
                      .withColumnRenamed('get_ut(fuid)', 'ut')                    
                    )

    b_block_out_df = (a_block_out_df
                    .select('blockid',
                        F.concat(F.col('ut'),
                                 F.lit('-'),
                                 F.col('pos')
                                 ).alias('ut_pos'),
                            'xml',
                            'email'
                    ))
    a_block_out_df.show()
    b_block_out_df.show()

    return b_block_out_df



def process():
    daisng_clusters_df = generate_daisng_cluster_test_data()
    b_block_out_df = generate_daisng_blockout_test_data()

    join_blockout_daisng = (b_block_out_df
                              .join(daisng_clusters_df,
                          on=b_block_out_df.ut_pos == daisng_clusters_df.item
                              )
    )

    #join_blockout_daisng.show()


    outdirectory = '/tmp/spark_data'
    #quick_delete(outdirectory)
    (join_blockout_daisng
     .write
     .format("com.databricks.spark.csv")
     .option("delimiter", "\t")
     .mode("overwrite")
     .save(outdirectory)
    )


process()
```

Save as text file and save in csv file
======================================

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output" rundoc-tangle="yes" rundoc-tangle="~/quicksaves/save_as_text_file.py"}


from pyspark import SparkContext, SparkConf
from pyspark.sql.functions import collect_list, udf
from pyspark.sql.types import StringType

import os
import shutil
try:
    sc = SparkContext("local", "my app name")
    from pyspark.sql import SQLContext
    sqlContext = SQLContext(sc)
except:
    pass

filename = '/tmp/daisng_cluster1.csv'

first_cluster = """A\t01-01|02-02|03-03|04-04
B\t05-05|06-06|07-07|08-08
C\t10-10|11-11
Z\t50-50
"""

def write_cluster(filename, filecontents):
    """
    Writes filecontents (string) to filename
    """
    with open(filename, 'w') as f:
        f.write(filecontents)


write_cluster(filename, first_cluster)

def cluster_read_helper(x):
    a, b = x.split('\t')
    c = b.split('|')
    return [[a, d] for d in c]

rdd1 = sc.textFile(filename)
rdd2 = rdd1.flatMap(lambda x: cluster_read_helper(x))
daisng_cluster_jan2017 = rdd2.toDF(['daisngid','item'])
daisng_cluster_jan2017.show()

def quick_delete(filename):
    try:
        shutil.rmtree(filename)
    except OSError:
        print("Failed to delete", filename)

def quick_print_directory(directory):
    import glob
    files = glob.glob(directory + "/*")
    print("printing ", directory)
    for file1 in files:
        print("...printing", file1)
        with open(file1) as f:
            print(f.read())

written_directory = '/tmp/save_file_test'
quick_delete(written_directory)
daisng_cluster_jan2017.rdd.saveAsTextFile(written_directory)

# os.system('cat {}/*'.format(written_directory))
quick_print_directory(written_directory)

grouped_cluster = (daisng_cluster_jan2017
                   .groupBy('daisngid')
                   .agg(collect_list('item')
                        .alias('items')
                       )
                   )

def formatted_items(cluster_items):
    cluster_string = '|'.join(cluster_items)
    return cluster_string

formatted_items_udf = udf(formatted_items, StringType())

grouped_cluster.show()

changed_grouped_cluster = (grouped_cluster
                           .select('daisngid', formatted_items_udf('items')
                                   .alias('items_string')
                           )
                         )

changed_grouped_cluster.show()
outdirectory = '/tmp/spark_data'
#quick_delete(outdirectory)
(changed_grouped_cluster
 .write
 .format("com.databricks.spark.csv")
 .option("delimiter", "\t")
 .mode("overwrite")
 .save(outdirectory)
)


# os.system('cat {}/*'.format(outdirectory))
quick_print_directory(outdirectory)


```

Help docstring of rdd class
===========================

Help on RDD in module pyspark.rdd object:

class RDD(****builtin****.object)

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
  A Resilient Distributed Dataset (RDD), the basic abstraction in Spark.

  Represents an immutable, partitioned collection of elements that can be

  operated on in parallel.

  Methods defined here:

  \_~add~\_~(self,\ other)~

  Return the union of this RDD and another one.

  &gt;&gt;&gt; rdd = sc.parallelize(\[1, 1, 2, 3\])

  &gt;&gt;&gt; (rdd + rdd).collect()

  \[1, 1, 2, 3, 1, 1, 2, 3\]

  \_~getnewargs~\_~(self)~

  \_~init~\_~(self,\ jrdd,\ ctx,\ jrdd~deserializer~=AutoBatchedSerializer(PickleSerializer()))~

  \_~repr~\_~(self)~

  aggregate(self, zeroValue, seqOp, combOp)

  Aggregate the elements of each partition, and then the results for all

  the partitions, using a given combine functions and a neutral "zero

  value."

  The functions C{op(t1, t2)} is allowed to modify C{t1} and return it

  as its result value to avoid object allocation; however, it should not

  modify C{t2}.

  The first function (seqOp) can return a different result type, U, than

  the type of this RDD. Thus, we need one operation for merging a T into

  an U and one operation for merging two U

  &gt;&gt;&gt; seqOp = (lambda x, y: (x\[0\] + y, x\[1\] + 1))

  &gt;&gt;&gt; combOp = (lambda x, y: (x\[0\] + y\[0\], x\[1\] + y\[1\]))

  &gt;&gt;&gt; sc.parallelize(\[1, 2, 3, 4\]).aggregate((0, 0), seqOp, combOp)

  (10, 4)

  &gt;&gt;&gt; sc.parallelize(\[\]).aggregate((0, 0), seqOp, combOp)

  (0, 0)

  aggregateByKey(self, zeroValue, seqFunc, combFunc, numPartitions=None, partitionFunc=&lt;function portable~hash~&gt;)

  Aggregate the values of each key, using given combine functions and a neutral

  "zero value". This function can return a different result type, U, than the type

  of the values in this RDD, V. Thus, we need one operation for merging a V into

  a U and one operation for merging two U's, The former operation is used for merging

  values within a partition, and the latter is used for merging values between

  partitions. To avoid memory allocation, both of these functions are

  allowed to modify and return their first argument instead of creating a new U.

  cache(self)

  Persist this RDD with the default storage level (C{MEMORY~ONLY~}).

  cartesian(self, other)

  Return the Cartesian product of this RDD and another one, that is, the

  RDD of all pairs of elements C{(a, b)} where C{a} is in C{self} and

  C{b} is in C{other}.

  &gt;&gt;&gt; rdd = sc.parallelize(\[1, 2\])

  &gt;&gt;&gt; sorted(rdd.cartesian(rdd).collect())

  \[(1, 1), (1, 2), (2, 1), (2, 2)\]

  checkpoint(self)

  Mark this RDD for checkpointing. It will be saved to a file inside the

  checkpoint directory set with L{SparkContext.setCheckpointDir()} and

  all references to its parent RDDs will be removed. This function must

  be called before any job has been executed on this RDD. It is strongly

  recommended that this RDD is persisted in memory, otherwise saving it

  on a file will require recomputation.

  coalesce(self, numPartitions, shuffle=False)

  Return a new RDD that is reduced into \`numPartitions\` partitions.

  &gt;&gt;&gt; sc.parallelize(\[1, 2, 3, 4, 5\], 3).glom().collect()

  \[\[1\], \[2, 3\], \[4, 5\]\]

  &gt;&gt;&gt; sc.parallelize(\[1, 2, 3, 4, 5\], 3).coalesce(1).glom().collect()

  *1, 2, 3, 4, 5*

  cogroup(self, other, numPartitions=None)

  For each key k in C{self} or C{other}, return a resulting RDD that

  contains a tuple with the list of values for that key in C{self} as

  well as C{other}.

  &gt;&gt;&gt; x = sc.parallelize(\[("a", 1), ("b", 4)\])

  &gt;&gt;&gt; y = sc.parallelize(\[("a", 2)\])

  &gt;&gt;&gt; \[(x, tuple(map(list, y))) for x, y in sorted(list(x.cogroup(y).collect()))\]

  \[('a', (\[1\], \[2\])), ('b', (\[4\], \[\]))\]

  collect(self)

  Return a list that contains all of the elements in this RDD.

  Note that this method should only be used if the resulting array is expected

  to be small, as all the data is loaded into the driver's memory.

  collectAsMap(self)

  Return the key-value pairs in this RDD to the master as a dictionary.

  Note that this method should only be used if the resulting data is expected

  to be small, as all the data is loaded into the driver's memory.

  &gt;&gt;&gt; m = sc.parallelize(\[(1, 2), (3, 4)\]).collectAsMap()

  &gt;&gt;&gt; m\[1\]

  2

  &gt;&gt;&gt; m\[3\]

  4

  combineByKey(self, createCombiner, mergeValue, mergeCombiners, numPartitions=None, partitionFunc=&lt;function portable~hash~&gt;)

  Generic function to combine the elements for each key using a custom

  set of aggregation functions.

  Turns an RDD\[(K, V)\] into a result of type RDD\[(K, C)\], for a "combined

  type" C. Note that V and C can be different -- for example, one might

  group an RDD of type (Int, Int) into an RDD of type (Int, List\[Int\]).

  Users provide three functions:

  - C{createCombiner}, which turns a V into a C (e.g., creates

  a one-element list)

  - C{mergeValue}, to merge a V into a C (e.g., adds it to the end of

  a list)

  - C{mergeCombiners}, to combine two C's into a single one.

  In addition, users can control the partitioning of the output RDD.

  &gt;&gt;&gt; x = sc.parallelize(\[("a", 1), ("b", 1), ("a", 1)\])

  &gt;&gt;&gt; def add(a, b): return a + str(b)

  &gt;&gt;&gt; sorted(x.combineByKey(str, add, add).collect())

  \[('a', '11'), ('b', '1')\]

  count(self)

  Return the number of elements in this RDD.

  &gt;&gt;&gt; sc.parallelize(\[2, 3, 4\]).count()

  3

  countApprox(self, timeout, confidence=0.95)

  .. note:: Experimental

  Approximate version of count() that returns a potentially incomplete

  result within a timeout, even if not all tasks have finished.

  &gt;&gt;&gt; rdd = sc.parallelize(range(1000), 10)

  &gt;&gt;&gt; rdd.countApprox(1000, 1.0)

  1000

  countApproxDistinct(self, relativeSD=0.05)

  .. note:: Experimental

  Return approximate number of distinct elements in the RDD.

  The algorithm used is based on streamlib's implementation of

  \`"HyperLogLog in Practice: Algorithmic Engineering of a State

  of The Art Cardinality Estimation Algorithm", available here

  <http://dx.doi.org/10.1145/2452376.2452456>\`\_.

  :param relativeSD: Relative accuracy. Smaller values create

  counters that require more space.

  It must be greater than 0.000017.

  &gt;&gt;&gt; n = sc.parallelize(range(1000)).map(str).countApproxDistinct()

  &gt;&gt;&gt; 900 &lt; n &lt; 1100

  True

  &gt;&gt;&gt; n = sc.parallelize(\[i % 20 for i in range(1000)\]).countApproxDistinct()

  &gt;&gt;&gt; 16 &lt; n &lt; 24

  True

  countByKey(self)

  Count the number of elements for each key, and return the result to the

  master as a dictionary.

  &gt;&gt;&gt; rdd = sc.parallelize(\[("a", 1), ("b", 1), ("a", 1)\])

  &gt;&gt;&gt; sorted(rdd.countByKey().items())

  \[('a', 2), ('b', 1)\]

  countByValue(self)

  Return the count of each unique value in this RDD as a dictionary of

  (value, count) pairs.

  &gt;&gt;&gt; sorted(sc.parallelize(\[1, 2, 1, 2, 2\], 2).countByValue().items())

  \[(1, 2), (2, 3)\]

  distinct(self, numPartitions=None)

  Return a new RDD containing the distinct elements in this RDD.

  &gt;&gt;&gt; sorted(sc.parallelize(\[1, 1, 2, 3\]).distinct().collect())

  \[1, 2, 3\]

  filter(self, f)

  Return a new RDD containing only the elements that satisfy a predicate.

  &gt;&gt;&gt; rdd = sc.parallelize(\[1, 2, 3, 4, 5\])

  &gt;&gt;&gt; rdd.filter(lambda x: x % 2 == 0).collect()

  \[2, 4\]

  first(self)

  Return the first element in this RDD.

  &gt;&gt;&gt; sc.parallelize(\[2, 3, 4\]).first()

  2

  &gt;&gt;&gt; sc.parallelize(\[\]).first()

  Traceback (most recent call last):

  ...

  ValueError: RDD is empty

  flatMap(self, f, preservesPartitioning=False)

  Return a new RDD by first applying a function to all elements of this

  RDD, and then flattening the results.

  &gt;&gt;&gt; rdd = sc.parallelize(\[2, 3, 4\])

  &gt;&gt;&gt; sorted(rdd.flatMap(lambda x: range(1, x)).collect())

  \[1, 1, 1, 2, 2, 3\]

  &gt;&gt;&gt; sorted(rdd.flatMap(lambda x: \[(x, x), (x, x)\]).collect())

  \[(2, 2), (2, 2), (3, 3), (3, 3), (4, 4), (4, 4)\]

  flatMapValues(self, f)

  Pass each value in the key-value pair RDD through a flatMap function

  without changing the keys; this also retains the original RDD's

  partitioning.

  &gt;&gt;&gt; x = sc.parallelize(\[("a", \["x", "y", "z"\]), ("b", \["p", "r"\])\])

  &gt;&gt;&gt; def f(x): return x

  &gt;&gt;&gt; x.flatMapValues(f).collect()

  \[('a', 'x'), ('a', 'y'), ('a', 'z'), ('b', 'p'), ('b', 'r')\]

  fold(self, zeroValue, op)

  Aggregate the elements of each partition, and then the results for all

  the partitions, using a given associative function and a neutral "zero value."

  The function C{op(t1, t2)} is allowed to modify C{t1} and return it

  as its result value to avoid object allocation; however, it should not

  modify C{t2}.

  This behaves somewhat differently from fold operations implemented

  for non-distributed collections in functional languages like Scala.

  This fold operation may be applied to partitions individually, and then

  fold those results into the final result, rather than apply the fold

  to each element sequentially in some defined ordering. For functions

  that are not commutative, the result may differ from that of a fold

  applied to a non-distributed collection.

  &gt;&gt;&gt; from operator import add

  &gt;&gt;&gt; sc.parallelize(\[1, 2, 3, 4, 5\]).fold(0, add)

  15

  foldByKey(self, zeroValue, func, numPartitions=None, partitionFunc=&lt;function portable~hash~&gt;)

  Merge the values for each key using an associative function "func"

  and a neutral "zeroValue" which may be added to the result an

  arbitrary number of times, and must not change the result

  (e.g., 0 for addition, or 1 for multiplication.).

  &gt;&gt;&gt; rdd = sc.parallelize(\[("a", 1), ("b", 1), ("a", 1)\])

  &gt;&gt;&gt; from operator import add

  &gt;&gt;&gt; sorted(rdd.foldByKey(0, add).collect())

  \[('a', 2), ('b', 1)\]

  foreach(self, f)

  Applies a function to all elements of this RDD.

  &gt;&gt;&gt; def f(x): print(x)

  &gt;&gt;&gt; sc.parallelize(\[1, 2, 3, 4, 5\]).foreach(f)

  foreachPartition(self, f)

  Applies a function to each partition of this RDD.

  &gt;&gt;&gt; def f(iterator):

  ... for x in iterator:

  ... print(x)

  &gt;&gt;&gt; sc.parallelize(\[1, 2, 3, 4, 5\]).foreachPartition(f)

  fullOuterJoin(self, other, numPartitions=None)

  Perform a right outer join of C{self} and C{other}.

  For each element (k, v) in C{self}, the resulting RDD will either

  contain all pairs (k, (v, w)) for w in C{other}, or the pair

  (k, (v, None)) if no elements in C{other} have key k.

  Similarly, for each element (k, w) in C{other}, the resulting RDD will

  either contain all pairs (k, (v, w)) for v in C{self}, or the pair

  (k, (None, w)) if no elements in C{self} have key k.

  Hash-partitions the resulting RDD into the given number of partitions.

  &gt;&gt;&gt; x = sc.parallelize(\[("a", 1), ("b", 4)\])

  &gt;&gt;&gt; y = sc.parallelize(\[("a", 2), ("c", 8)\])

  &gt;&gt;&gt; sorted(x.fullOuterJoin(y).collect())

  \[('a', (1, 2)), ('b', (4, None)), ('c', (None, 8))\]

  getCheckpointFile(self)

  Gets the name of the file to which this RDD was checkpointed

  getNumPartitions(self)

  Returns the number of partitions in RDD

  &gt;&gt;&gt; rdd = sc.parallelize(\[1, 2, 3, 4\], 2)

  &gt;&gt;&gt; rdd.getNumPartitions()

  2

  getStorageLevel(self)

  Get the RDD's current storage level.

  &gt;&gt;&gt; rdd1 = sc.parallelize(\[1,2\])

  &gt;&gt;&gt; rdd1.getStorageLevel()

  StorageLevel(False, False, False, False, 1)

  &gt;&gt;&gt; print(rdd1.getStorageLevel())

  Serialized 1x Replicated

  glom(self)

  Return an RDD created by coalescing all elements within each partition

  into a list.

  &gt;&gt;&gt; rdd = sc.parallelize(\[1, 2, 3, 4\], 2)

  &gt;&gt;&gt; sorted(rdd.glom().collect())

  \[\[1, 2\], \[3, 4\]\]

  groupBy(self, f, numPartitions=None, partitionFunc=&lt;function portable~hash~&gt;)

  Return an RDD of grouped items.

  &gt;&gt;&gt; rdd = sc.parallelize(\[1, 1, 2, 3, 5, 8\])

  &gt;&gt;&gt; result = rdd.groupBy(lambda x: x % 2).collect()

  &gt;&gt;&gt; sorted(\[(x, sorted(y)) for (x, y) in result\])

  \[(0, \[2, 8\]), (1, \[1, 1, 3, 5\])\]

  groupByKey(self, numPartitions=None, partitionFunc=&lt;function portable~hash~&gt;)

  Group the values for each key in the RDD into a single sequence.

  Hash-partitions the resulting RDD with numPartitions partitions.

  Note: If you are grouping in order to perform an aggregation (such as a

  sum or average) over each key, using reduceByKey or aggregateByKey will

  provide much better performance.

  &gt;&gt;&gt; rdd = sc.parallelize(\[("a", 1), ("b", 1), ("a", 1)\])

  &gt;&gt;&gt; sorted(rdd.groupByKey().mapValues(len).collect())

  \[('a', 2), ('b', 1)\]

  &gt;&gt;&gt; sorted(rdd.groupByKey().mapValues(list).collect())

  \[('a', \[1, 1\]), ('b', \[1\])\]

  groupWith(self, other, \*others)

  Alias for cogroup but with support for multiple RDDs.

  &gt;&gt;&gt; w = sc.parallelize(\[("a", 5), ("b", 6)\])

  &gt;&gt;&gt; x = sc.parallelize(\[("a", 1), ("b", 4)\])

  &gt;&gt;&gt; y = sc.parallelize(\[("a", 2)\])

  &gt;&gt;&gt; z = sc.parallelize(\[("b", 42)\])

  &gt;&gt;&gt; \[(x, tuple(map(list, y))) for x, y in sorted(list(w.groupWith(x, y, z).collect()))\]

  \[('a', (\[5\], \[1\], \[2\], \[\])), ('b', (\[6\], \[4\], \[\], \[42\]))\]

  histogram(self, buckets)

  Compute a histogram using the provided buckets. The buckets

  are all open to the right except for the last which is closed.

  e.g. \[1,10,20,50\] means the buckets are \[1,10) \[10,20) \[20,50\],

  which means 1&lt;=x&lt;10, 10&lt;=x&lt;20, 20&lt;=x&lt;=50. And on the input of 1

  and 50 we would have a histogram of 1,0,1.

  If your histogram is evenly spaced (e.g. \[0, 10, 20, 30\]),

  this can be switched from an O(log n) inseration to O(1) per

  element (where n is the number of buckets).

  Buckets must be sorted, not contain any duplicates, and have

  at least two elements.

  If \`buckets\` is a number, it will generate buckets which are

  evenly spaced between the minimum and maximum of the RDD. For

  example, if the min value is 0 and the max is 100, given \`buckets\`

  as 2, the resulting buckets will be \[0,50) \[50,100\]. \`buckets\` must

  be at least 1. An exception is raised if the RDD contains infinity.

  If the elements in the RDD do not vary (max == min), a single bucket

  will be used.

  The return value is a tuple of buckets and histogram.

  &gt;&gt;&gt; rdd = sc.parallelize(range(51))

  &gt;&gt;&gt; rdd.histogram(2)

  (\[0, 25, 50\], \[25, 26\])

  &gt;&gt;&gt; rdd.histogram(\[0, 5, 25, 50\])

  (\[0, 5, 25, 50\], \[5, 20, 26\])

  &gt;&gt;&gt; rdd.histogram(\[0, 15, 30, 45, 60\]) \# evenly spaced buckets

  (\[0, 15, 30, 45, 60\], \[15, 15, 15, 6\])

  &gt;&gt;&gt; rdd = sc.parallelize(\["ab", "ac", "b", "bd", "ef"\])

  &gt;&gt;&gt; rdd.histogram(("a", "b", "c"))

  (('a', 'b', 'c'), \[2, 2\])

  id(self)

  A unique ID for this RDD (within its SparkContext).

  intersection(self, other)

  Return the intersection of this RDD and another one. The output will

  not contain any duplicate elements, even if the input RDDs did.

  Note that this method performs a shuffle internally.

  &gt;&gt;&gt; rdd1 = sc.parallelize(\[1, 10, 2, 3, 4, 5\])

  &gt;&gt;&gt; rdd2 = sc.parallelize(\[1, 6, 2, 3, 7, 8\])

  &gt;&gt;&gt; rdd1.intersection(rdd2).collect()

  \[1, 2, 3\]

  isCheckpointed(self)

  Return whether this RDD has been checkpointed or not

  isEmpty(self)

  Returns true if and only if the RDD contains no elements at all. Note that an RDD

  may be empty even when it has at least 1 partition.

  &gt;&gt;&gt; sc.parallelize(\[\]).isEmpty()

  True

  &gt;&gt;&gt; sc.parallelize(\[1\]).isEmpty()

  False

  join(self, other, numPartitions=None)

  Return an RDD containing all pairs of elements with matching keys in

  C{self} and C{other}.

  Each pair of elements will be returned as a (k, (v1, v2)) tuple, where

  (k, v1) is in C{self} and (k, v2) is in C{other}.

  Performs a hash join across the cluster.

  &gt;&gt;&gt; x = sc.parallelize(\[("a", 1), ("b", 4)\])

  &gt;&gt;&gt; y = sc.parallelize(\[("a", 2), ("a", 3)\])

  &gt;&gt;&gt; sorted(x.join(y).collect())

  \[('a', (1, 2)), ('a', (1, 3))\]

  keyBy(self, f)

  Creates tuples of the elements in this RDD by applying C{f}.

  &gt;&gt;&gt; x = sc.parallelize(range(0,3)).keyBy(lambda x: x\*x)

  &gt;&gt;&gt; y = sc.parallelize(zip(range(0,5), range(0,5)))

  &gt;&gt;&gt; \[(x, list(map(list, y))) for x, y in sorted(x.cogroup(y).collect())\]

  \[(0, \[\[0\], \[0\]\]), (1, \[\[1\], \[1\]\]), (2, \[\[\], \[2\]\]), (3, \[\[\], \[3\]\]), (4, \[\[2\], \[4\]\])\]

  keys(self)

  Return an RDD with the keys of each tuple.

  &gt;&gt;&gt; m = sc.parallelize(\[(1, 2), (3, 4)\]).keys()

  &gt;&gt;&gt; m.collect()

  \[1, 3\]

  leftOuterJoin(self, other, numPartitions=None)

  Perform a left outer join of C{self} and C{other}.

  For each element (k, v) in C{self}, the resulting RDD will either

  contain all pairs (k, (v, w)) for w in C{other}, or the pair

  (k, (v, None)) if no elements in C{other} have key k.

  Hash-partitions the resulting RDD into the given number of partitions.

  &gt;&gt;&gt; x = sc.parallelize(\[("a", 1), ("b", 4)\])

  &gt;&gt;&gt; y = sc.parallelize(\[("a", 2)\])

  &gt;&gt;&gt; sorted(x.leftOuterJoin(y).collect())

  \[('a', (1, 2)), ('b', (4, None))\]

  lookup(self, key)

  Return the list of values in the RDD for key \`key\`. This operation

  is done efficiently if the RDD has a known partitioner by only

  searching the partition that the key maps to.

  &gt;&gt;&gt; l = range(1000)

  &gt;&gt;&gt; rdd = sc.parallelize(zip(l, l), 10)

  &gt;&gt;&gt; rdd.lookup(42) \# slow

  \[42\]

  &gt;&gt;&gt; sorted = rdd.sortByKey()

  &gt;&gt;&gt; sorted.lookup(42) \# fast

  \[42\]

  &gt;&gt;&gt; sorted.lookup(1024)

  \[\]

  &gt;&gt;&gt; rdd2 = sc.parallelize(\[(('a', 'b'), 'c')\]).groupByKey()

  &gt;&gt;&gt; list(rdd2.lookup(('a', 'b'))\[0\])

  \['c'\]

  map(self, f, preservesPartitioning=False)

  Return a new RDD by applying a function to each element of this RDD.

  &gt;&gt;&gt; rdd = sc.parallelize(\["b", "a", "c"\])

  &gt;&gt;&gt; sorted(rdd.map(lambda x: (x, 1)).collect())

  \[('a', 1), ('b', 1), ('c', 1)\]

  mapPartitions(self, f, preservesPartitioning=False)

  Return a new RDD by applying a function to each partition of this RDD.

  &gt;&gt;&gt; rdd = sc.parallelize(\[1, 2, 3, 4\], 2)

  &gt;&gt;&gt; def f(iterator): yield sum(iterator)

  &gt;&gt;&gt; rdd.mapPartitions(f).collect()

  \[3, 7\]

  mapPartitionsWithIndex(self, f, preservesPartitioning=False)

  Return a new RDD by applying a function to each partition of this RDD,

  while tracking the index of the original partition.

  &gt;&gt;&gt; rdd = sc.parallelize(\[1, 2, 3, 4\], 4)

  &gt;&gt;&gt; def f(splitIndex, iterator): yield splitIndex

  &gt;&gt;&gt; rdd.mapPartitionsWithIndex(f).sum()

  6

  mapPartitionsWithSplit(self, f, preservesPartitioning=False)

  Deprecated: use mapPartitionsWithIndex instead.

  Return a new RDD by applying a function to each partition of this RDD,

  while tracking the index of the original partition.

  &gt;&gt;&gt; rdd = sc.parallelize(\[1, 2, 3, 4\], 4)

  &gt;&gt;&gt; def f(splitIndex, iterator): yield splitIndex

  &gt;&gt;&gt; rdd.mapPartitionsWithSplit(f).sum()

  6

  mapValues(self, f)

  Pass each value in the key-value pair RDD through a map function

  without changing the keys; this also retains the original RDD's

  partitioning.

  &gt;&gt;&gt; x = sc.parallelize(\[("a", \["apple", "banana", "lemon"\]), ("b", \["grapes"\])\])

  &gt;&gt;&gt; def f(x): return len(x)

  &gt;&gt;&gt; x.mapValues(f).collect()

  \[('a', 3), ('b', 1)\]

  max(self, key=None)

  Find the maximum item in this RDD.

  :param key: A function used to generate key for comparing

  &gt;&gt;&gt; rdd = sc.parallelize(\[1.0, 5.0, 43.0, 10.0\])

  &gt;&gt;&gt; rdd.max()

  43.0

  &gt;&gt;&gt; rdd.max(key=str)

  5.0

  mean(self)

  Compute the mean of this RDD's elements.

  &gt;&gt;&gt; sc.parallelize(\[1, 2, 3\]).mean()

  2.0

  meanApprox(self, timeout, confidence=0.95)

  .. note:: Experimental

  Approximate operation to return the mean within a timeout

  or meet the confidence.

  &gt;&gt;&gt; rdd = sc.parallelize(range(1000), 10)

  &gt;&gt;&gt; r = sum(range(1000)) / 1000.0

  &gt;&gt;&gt; abs(rdd.meanApprox(1000) - r) / r &lt; 0.05

  True

  min(self, key=None)

  Find the minimum item in this RDD.

  :param key: A function used to generate key for comparing

  &gt;&gt;&gt; rdd = sc.parallelize(\[2.0, 5.0, 43.0, 10.0\])

  &gt;&gt;&gt; rdd.min()

  2.0

  &gt;&gt;&gt; rdd.min(key=str)

  10.0

  name(self)

  Return the name of this RDD.

  partitionBy(self, numPartitions, partitionFunc=&lt;function portable~hash~&gt;)

  Return a copy of the RDD partitioned using the specified partitioner.

  &gt;&gt;&gt; pairs = sc.parallelize(\[1, 2, 3, 4, 2, 4, 1\]).map(lambda x: (x, x))

  &gt;&gt;&gt; sets = pairs.partitionBy(2).glom().collect()

  &gt;&gt;&gt; len(set(sets\[0\]).intersection(set(sets\[1\])))

  0

  persist(self, storageLevel=StorageLevel(False, True, False, False, 1))

  Set this RDD's storage level to persist its values across operations

  after the first time it is computed. This can only be used to assign

  a new storage level if the RDD does not have a storage level set yet.

  If no storage level is specified defaults to (C{MEMORY~ONLY~}).

  &gt;&gt;&gt; rdd = sc.parallelize(\["b", "a", "c"\])

  &gt;&gt;&gt; rdd.persist().is~cached~

  True

  pipe(self, command, env=None, checkCode=False)

  Return an RDD created by piping elements to a forked external process.

  &gt;&gt;&gt; sc.parallelize(\['1', '2', '', '3'\]).pipe('cat').collect()

  \[u'1', u'2', u'', u'3'\]

  :param checkCode: whether or not to check the return value of the shell command.

  randomSplit(self, weights, seed=None)

  Randomly splits this RDD with the provided weights.

  :param weights: weights for splits, will be normalized if they don't sum to 1

  :param seed: random seed

  :return: split RDDs in a list

  &gt;&gt;&gt; rdd = sc.parallelize(range(500), 1)

  &gt;&gt;&gt; rdd1, rdd2 = rdd.randomSplit(\[2, 3\], 17)

  &gt;&gt;&gt; len(rdd1.collect() + rdd2.collect())

  500

  &gt;&gt;&gt; 150 &lt; rdd1.count() &lt; 250

  True

  &gt;&gt;&gt; 250 &lt; rdd2.count() &lt; 350

  True

  reduce(self, f)

  Reduces the elements of this RDD using the specified commutative and

  associative binary operator. Currently reduces partitions locally.

  &gt;&gt;&gt; from operator import add

  &gt;&gt;&gt; sc.parallelize(\[1, 2, 3, 4, 5\]).reduce(add)

  15

  &gt;&gt;&gt; sc.parallelize((2 for \_ in range(10))).map(lambda x: 1).cache().reduce(add)

  10

  &gt;&gt;&gt; sc.parallelize(\[\]).reduce(add)

  Traceback (most recent call last):

  ...

  ValueError: Can not reduce() empty RDD

  reduceByKey(self, func, numPartitions=None, partitionFunc=&lt;function portable~hash~&gt;)

  Merge the values for each key using an associative and commutative reduce function.

  This will also perform the merging locally on each mapper before

  sending results to a reducer, similarly to a "combiner" in MapReduce.

  Output will be partitioned with C{numPartitions} partitions, or

  the default parallelism level if C{numPartitions} is not specified.

  Default partitioner is hash-partition.

  &gt;&gt;&gt; from operator import add

  &gt;&gt;&gt; rdd = sc.parallelize(\[("a", 1), ("b", 1), ("a", 1)\])

  &gt;&gt;&gt; sorted(rdd.reduceByKey(add).collect())

  \[('a', 2), ('b', 1)\]

  reduceByKeyLocally(self, func)

  Merge the values for each key using an associative and commutative reduce function, but

  return the results immediately to the master as a dictionary.

  This will also perform the merging locally on each mapper before

  sending results to a reducer, similarly to a "combiner" in MapReduce.

  &gt;&gt;&gt; from operator import add

  &gt;&gt;&gt; rdd = sc.parallelize(\[("a", 1), ("b", 1), ("a", 1)\])

  &gt;&gt;&gt; sorted(rdd.reduceByKeyLocally(add).items())

  \[('a', 2), ('b', 1)\]

  repartition(self, numPartitions)

  Return a new RDD that has exactly numPartitions partitions.

  Can increase or decrease the level of parallelism in this RDD.

  Internally, this uses a shuffle to redistribute data.

  If you are decreasing the number of partitions in this RDD, consider

  using \`coalesce\`, which can avoid performing a shuffle.

  &gt;&gt;&gt; rdd = sc.parallelize(\[1,2,3,4,5,6,7\], 4)

  &gt;&gt;&gt; sorted(rdd.glom().collect())

  \[\[1\], \[2, 3\], \[4, 5\], \[6, 7\]\]

  &gt;&gt;&gt; len(rdd.repartition(2).glom().collect())

  2

  &gt;&gt;&gt; len(rdd.repartition(10).glom().collect())

  10

  repartitionAndSortWithinPartitions(self, numPartitions=None, partitionFunc=&lt;function portable~hash~&gt;, ascending=True, keyfunc=&lt;function &lt;lambda&gt;&gt;)

  Repartition the RDD according to the given partitioner and, within each resulting partition,

  sort records by their keys.

  &gt;&gt;&gt; rdd = sc.parallelize(\[(0, 5), (3, 8), (2, 6), (0, 8), (3, 8), (1, 3)\])

  &gt;&gt;&gt; rdd2 = rdd.repartitionAndSortWithinPartitions(2, lambda x: x % 2, 2)

  &gt;&gt;&gt; rdd2.glom().collect()

  \[\[(0, 5), (0, 8), (2, 6)\], \[(1, 3), (3, 8), (3, 8)\]\]

  rightOuterJoin(self, other, numPartitions=None)

  Perform a right outer join of C{self} and C{other}.

  For each element (k, w) in C{other}, the resulting RDD will either

  contain all pairs (k, (v, w)) for v in this, or the pair (k, (None, w))

  if no elements in C{self} have key k.

  Hash-partitions the resulting RDD into the given number of partitions.

  &gt;&gt;&gt; x = sc.parallelize(\[("a", 1), ("b", 4)\])

  &gt;&gt;&gt; y = sc.parallelize(\[("a", 2)\])

  &gt;&gt;&gt; sorted(y.rightOuterJoin(x).collect())

  \[('a', (2, 1)), ('b', (None, 4))\]

  sample(self, withReplacement, fraction, seed=None)

  Return a sampled subset of this RDD.

  :param withReplacement: can elements be sampled multiple times (replaced when sampled out)

  :param fraction: expected size of the sample as a fraction of this RDD's size

  without replacement: probability that each element is chosen; fraction must be \[0, 1\]

  with replacement: expected number of times each element is chosen; fraction must be &gt;= 0

  :param seed: seed for the random number generator

  &gt;&gt;&gt; rdd = sc.parallelize(range(100), 4)

  &gt;&gt;&gt; 6 &lt;= rdd.sample(False, 0.1, 81).count() &lt;= 14

  True

  sampleByKey(self, withReplacement, fractions, seed=None)

  Return a subset of this RDD sampled by key (via stratified sampling).

  Create a sample of this RDD using variable sampling rates for

  different keys as specified by fractions, a key to sampling rate map.

  &gt;&gt;&gt; fractions = {"a": 0.2, "b": 0.1}

  &gt;&gt;&gt; rdd = sc.parallelize(fractions.keys()).cartesian(sc.parallelize(range(0, 1000)))

  &gt;&gt;&gt; sample = dict(rdd.sampleByKey(False, fractions, 2).groupByKey().collect())

  &gt;&gt;&gt; 100 &lt; len(sample\["a"\]) &lt; 300 and 50 &lt; len(sample\["b"\]) &lt; 150

  True

  &gt;&gt;&gt; max(sample\["a"\]) &lt;= 999 and min(sample\["a"\]) &gt;= 0

  True

  &gt;&gt;&gt; max(sample\["b"\]) &lt;= 999 and min(sample\["b"\]) &gt;= 0

  True

  sampleStdev(self)

  Compute the sample standard deviation of this RDD's elements (which

  corrects for bias in estimating the standard deviation by dividing by

  N-1 instead of N).

  &gt;&gt;&gt; sc.parallelize(\[1, 2, 3\]).sampleStdev()

  1.0

  sampleVariance(self)

  Compute the sample variance of this RDD's elements (which corrects

  for bias in estimating the variance by dividing by N-1 instead of N).

  &gt;&gt;&gt; sc.parallelize(\[1, 2, 3\]).sampleVariance()

  1.0

  saveAsHadoopDataset(self, conf, keyConverter=None, valueConverter=None)

  Output a Python RDD of key-value pairs (of form C{RDD\[(K, V)\]}) to any Hadoop file

  system, using the old Hadoop OutputFormat API (mapred package). Keys/values are

  converted for output using either user specified converters or, by default,

  L{org.apache.spark.api.python.JavaToWritableConverter}.

  :param conf: Hadoop job configuration, passed in as a dict

  :param keyConverter: (None by default)

  :param valueConverter: (None by default)

  saveAsHadoopFile(self, path, outputFormatClass, keyClass=None, valueClass=None, keyConverter=None, valueConverter=None, conf=None, compressionCodecClass=None)

  Output a Python RDD of key-value pairs (of form C{RDD\[(K, V)\]}) to any Hadoop file

  system, using the old Hadoop OutputFormat API (mapred package). Key and value types

  will be inferred if not specified. Keys and values are converted for output using either

  user specified converters or L{org.apache.spark.api.python.JavaToWritableConverter}. The

  C{conf} is applied on top of the base Hadoop conf associated with the SparkContext

  of this RDD to create a merged Hadoop MapReduce job configuration for saving the data.

  :param path: path to Hadoop file

  :param outputFormatClass: fully qualified classname of Hadoop OutputFormat

  (e.g. "org.apache.hadoop.mapred.SequenceFileOutputFormat")

  :param keyClass: fully qualified classname of key Writable class

  (e.g. "org.apache.hadoop.io.IntWritable", None by default)

  :param valueClass: fully qualified classname of value Writable class

  (e.g. "org.apache.hadoop.io.Text", None by default)

  :param keyConverter: (None by default)

  :param valueConverter: (None by default)

  :param conf: (None by default)

  :param compressionCodecClass: (None by default)

  saveAsNewAPIHadoopDataset(self, conf, keyConverter=None, valueConverter=None)

  Output a Python RDD of key-value pairs (of form C{RDD\[(K, V)\]}) to any Hadoop file

  system, using the new Hadoop OutputFormat API (mapreduce package). Keys/values are

  converted for output using either user specified converters or, by default,

  L{org.apache.spark.api.python.JavaToWritableConverter}.

  :param conf: Hadoop job configuration, passed in as a dict

  :param keyConverter: (None by default)

  :param valueConverter: (None by default)

  saveAsNewAPIHadoopFile(self, path, outputFormatClass, keyClass=None, valueClass=None, keyConverter=None, valueConverter=None, conf=None)

  Output a Python RDD of key-value pairs (of form C{RDD\[(K, V)\]}) to any Hadoop file

  system, using the new Hadoop OutputFormat API (mapreduce package). Key and value types

  will be inferred if not specified. Keys and values are converted for output using either

  user specified converters or L{org.apache.spark.api.python.JavaToWritableConverter}. The

  C{conf} is applied on top of the base Hadoop conf associated with the SparkContext

  of this RDD to create a merged Hadoop MapReduce job configuration for saving the data.

  :param path: path to Hadoop file

  :param outputFormatClass: fully qualified classname of Hadoop OutputFormat

  (e.g. "org.apache.hadoop.mapreduce.lib.output.SequenceFileOutputFormat")

  :param keyClass: fully qualified classname of key Writable class

  (e.g. "org.apache.hadoop.io.IntWritable", None by default)

  :param valueClass: fully qualified classname of value Writable class

  (e.g. "org.apache.hadoop.io.Text", None by default)

  :param keyConverter: (None by default)

  :param valueConverter: (None by default)

  :param conf: Hadoop job configuration, passed in as a dict (None by default)

  saveAsPickleFile(self, path, batchSize=10)

  Save this RDD as a SequenceFile of serialized objects. The serializer

  used is L{pyspark.serializers.PickleSerializer}, default batch size

  is 10.

  &gt;&gt;&gt; tmpFile = NamedTemporaryFile(delete=True)

  &gt;&gt;&gt; tmpFile.close()

  &gt;&gt;&gt; sc.parallelize(\[1, 2, 'spark', 'rdd'\]).saveAsPickleFile(tmpFile.name, 3)

  &gt;&gt;&gt; sorted(sc.pickleFile(tmpFile.name, 5).map(str).collect())

  \['1', '2', 'rdd', 'spark'\]

  saveAsSequenceFile(self, path, compressionCodecClass=None)

  Output a Python RDD of key-value pairs (of form C{RDD\[(K, V)\]}) to any Hadoop file

  system, using the L{org.apache.hadoop.io.Writable} types that we convert from the

  RDD's key and value types. The mechanism is as follows:

  1\. Pyrolite is used to convert pickled Python RDD into RDD of Java
  objects.

  2\. Keys and values of this Java RDD are converted to Writables and
  written out.

  :param path: path to sequence file

  :param compressionCodecClass: (None by default)

  saveAsTextFile(self, path, compressionCodecClass=None)

  Save this RDD as a text file, using string representations of elements.

  @param path: path to text file

  @param compressionCodecClass: (None by default) string i.e.

  "org.apache.hadoop.io.compress.GzipCodec"

  &gt;&gt;&gt; tempFile = NamedTemporaryFile(delete=True)

  &gt;&gt;&gt; tempFile.close()

  &gt;&gt;&gt; sc.parallelize(range(10)).saveAsTextFile(tempFile.name)

  &gt;&gt;&gt; from fileinput import input

  &gt;&gt;&gt; from glob import glob

  &gt;&gt;&gt; ''.join(sorted(input(glob(tempFile.name + "/part-0000\*"))))

  '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'

  Empty lines are tolerated when saving to text files.

  &gt;&gt;&gt; tempFile2 = NamedTemporaryFile(delete=True)

  &gt;&gt;&gt; tempFile2.close()

  &gt;&gt;&gt; sc.parallelize(\['', 'foo', '', 'bar', ''\]).saveAsTextFile(tempFile2.name)

  &gt;&gt;&gt; ''.join(sorted(input(glob(tempFile2.name + "/part-0000\*"))))

  '\n\n\nbar\nfoo\n'

  Using compressionCodecClass

  &gt;&gt;&gt; tempFile3 = NamedTemporaryFile(delete=True)

  &gt;&gt;&gt; tempFile3.close()

  &gt;&gt;&gt; codec = "org.apache.hadoop.io.compress.GzipCodec"

  &gt;&gt;&gt; sc.parallelize(\['foo', 'bar'\]).saveAsTextFile(tempFile3.name, codec)

  &gt;&gt;&gt; from fileinput import input, hook~compressed~

  &gt;&gt;&gt; result = sorted(input(glob(tempFile3.name + "/part\*.gz"), openhook=hook~compressed~))

  &gt;&gt;&gt; b''.join(result).decode('utf-8')

  u'bar\nfoo\n'

  setName(self, name)

  Assign a name to this RDD.

  &gt;&gt;&gt; rdd1 = sc.parallelize(\[1, 2\])

  &gt;&gt;&gt; rdd1.setName('RDD1').name()

  u'RDD1'

  sortBy(self, keyfunc, ascending=True, numPartitions=None)

  Sorts this RDD by the given keyfunc

  &gt;&gt;&gt; tmp = \[('a', 1), ('b', 2), ('1', 3), ('d', 4), ('2', 5)\]

  &gt;&gt;&gt; sc.parallelize(tmp).sortBy(lambda x: x\[0\]).collect()

  \[('1', 3), ('2', 5), ('a', 1), ('b', 2), ('d', 4)\]

  &gt;&gt;&gt; sc.parallelize(tmp).sortBy(lambda x: x\[1\]).collect()

  \[('a', 1), ('b', 2), ('1', 3), ('d', 4), ('2', 5)\]

  sortByKey(self, ascending=True, numPartitions=None, keyfunc=&lt;function &lt;lambda&gt;&gt;)

  Sorts this RDD, which is assumed to consist of (key, value) pairs.

  \# noqa

  &gt;&gt;&gt; tmp = \[('a', 1), ('b', 2), ('1', 3), ('d', 4), ('2', 5)\]

  &gt;&gt;&gt; sc.parallelize(tmp).sortByKey().first()

  ('1', 3)

  &gt;&gt;&gt; sc.parallelize(tmp).sortByKey(True, 1).collect()

  \[('1', 3), ('2', 5), ('a', 1), ('b', 2), ('d', 4)\]

  &gt;&gt;&gt; sc.parallelize(tmp).sortByKey(True, 2).collect()

  \[('1', 3), ('2', 5), ('a', 1), ('b', 2), ('d', 4)\]

  &gt;&gt;&gt; tmp2 = \[('Mary', 1), ('had', 2), ('a', 3), ('little', 4), ('lamb', 5)\]

  &gt;&gt;&gt; tmp2.extend(\[('whose', 6), ('fleece', 7), ('was', 8), ('white', 9)\])

  &gt;&gt;&gt; sc.parallelize(tmp2).sortByKey(True, 3, keyfunc=lambda k: k.lower()).collect()

  \[('a', 3), ('fleece', 7), ('had', 2), ('lamb', 5),...('white', 9), ('whose', 6)\]

  stats(self)

  Return a L{StatCounter} object that captures the mean, variance

  and count of the RDD's elements in one operation.

  stdev(self)

  Compute the standard deviation of this RDD's elements.

  &gt;&gt;&gt; sc.parallelize(\[1, 2, 3\]).stdev()

  0.816...

  subtract(self, other, numPartitions=None)

  Return each value in C{self} that is not contained in C{other}.

  &gt;&gt;&gt; x = sc.parallelize(\[("a", 1), ("b", 4), ("b", 5), ("a", 3)\])

  &gt;&gt;&gt; y = sc.parallelize(\[("a", 3), ("c", None)\])

  &gt;&gt;&gt; sorted(x.subtract(y).collect())

  \[('a', 1), ('b', 4), ('b', 5)\]

  subtractByKey(self, other, numPartitions=None)

  Return each (key, value) pair in C{self} that has no pair with matching

  key in C{other}.

  &gt;&gt;&gt; x = sc.parallelize(\[("a", 1), ("b", 4), ("b", 5), ("a", 2)\])

  &gt;&gt;&gt; y = sc.parallelize(\[("a", 3), ("c", None)\])

  &gt;&gt;&gt; sorted(x.subtractByKey(y).collect())

  \[('b', 4), ('b', 5)\]

  sum(self)

  Add up the elements in this RDD.

  &gt;&gt;&gt; sc.parallelize(\[1.0, 2.0, 3.0\]).sum()

  6.0

  sumApprox(self, timeout, confidence=0.95)

  .. note:: Experimental

  Approximate operation to return the sum within a timeout

  or meet the confidence.

  &gt;&gt;&gt; rdd = sc.parallelize(range(1000), 10)

  &gt;&gt;&gt; r = sum(range(1000))

  &gt;&gt;&gt; abs(rdd.sumApprox(1000) - r) / r &lt; 0.05

  True

  take(self, num)

  Take the first num elements of the RDD.

  It works by first scanning one partition, and use the results from

  that partition to estimate the number of additional partitions needed

  to satisfy the limit.

  Note that this method should only be used if the resulting array is expected

  to be small, as all the data is loaded into the driver's memory.

  Translated from the Scala implementation in RDD\#take().

  &gt;&gt;&gt; sc.parallelize(\[2, 3, 4, 5, 6\]).cache().take(2)

  \[2, 3\]

  &gt;&gt;&gt; sc.parallelize(\[2, 3, 4, 5, 6\]).take(10)

  \[2, 3, 4, 5, 6\]

  &gt;&gt;&gt; sc.parallelize(range(100), 100).filter(lambda x: x &gt; 90).take(3)

  \[91, 92, 93\]

  takeOrdered(self, num, key=None)

  Get the N elements from a RDD ordered in ascending order or as

  specified by the optional key function.

  Note that this method should only be used if the resulting array is expected

  to be small, as all the data is loaded into the driver's memory.

  &gt;&gt;&gt; sc.parallelize(\[10, 1, 2, 9, 3, 4, 5, 6, 7\]).takeOrdered(6)

  \[1, 2, 3, 4, 5, 6\]

  &gt;&gt;&gt; sc.parallelize(\[10, 1, 2, 9, 3, 4, 5, 6, 7\], 2).takeOrdered(6, key=lambda x: -x)

  \[10, 9, 7, 6, 5, 4\]

  takeSample(self, withReplacement, num, seed=None)

  Return a fixed-size sampled subset of this RDD.

  Note that this method should only be used if the resulting array is expected

  to be small, as all the data is loaded into the driver's memory.

  &gt;&gt;&gt; rdd = sc.parallelize(range(0, 10))

  &gt;&gt;&gt; len(rdd.takeSample(True, 20, 1))

  20

  &gt;&gt;&gt; len(rdd.takeSample(False, 5, 2))

  5

  &gt;&gt;&gt; len(rdd.takeSample(False, 15, 3))

  10

  toDF(self, schema=None, sampleRatio=None)

  Converts current :class:\`RDD\` into a :class:\`DataFrame\`

  This is a shorthand for \`\`spark.createDataFrame(rdd, schema, sampleRatio)\`\`

  :param schema: a StructType or list of names of columns

  :param samplingRatio: the sample ratio of rows used for inferring

  :return: a DataFrame

  &gt;&gt;&gt; rdd.toDF().collect()

  \[Row(name=u'Alice', age=1)\]

  toDebugString(self)

  A description of this RDD and its recursive dependencies for debugging.

  toLocalIterator(self)

  Return an iterator that contains all of the elements in this RDD.

  The iterator will consume as much memory as the largest partition in this RDD.

  &gt;&gt;&gt; rdd = sc.parallelize(range(10))

  &gt;&gt;&gt; \[x for x in rdd.toLocalIterator()\]

  \[0, 1, 2, 3, 4, 5, 6, 7, 8, 9\]

  top(self, num, key=None)

  Get the top N elements from a RDD.

  Note that this method should only be used if the resulting array is expected

  to be small, as all the data is loaded into the driver's memory.

  Note: It returns the list sorted in descending order.

  &gt;&gt;&gt; sc.parallelize(\[10, 4, 2, 12, 3\]).top(1)

  \[12\]

  &gt;&gt;&gt; sc.parallelize(\[2, 3, 4, 5, 6\], 2).top(2)

  \[6, 5\]

  &gt;&gt;&gt; sc.parallelize(\[10, 4, 2, 12, 3\]).top(3, key=str)

  \[4, 3, 2\]

  treeAggregate(self, zeroValue, seqOp, combOp, depth=2)

  Aggregates the elements of this RDD in a multi-level tree

  pattern.

  :param depth: suggested depth of the tree (default: 2)

  &gt;&gt;&gt; add = lambda x, y: x + y

  &gt;&gt;&gt; rdd = sc.parallelize(\[-5, -4, -3, -2, -1, 1, 2, 3, 4\], 10)

  &gt;&gt;&gt; rdd.treeAggregate(0, add, add)

  -5

  &gt;&gt;&gt; rdd.treeAggregate(0, add, add, 1)

  -5

  &gt;&gt;&gt; rdd.treeAggregate(0, add, add, 2)

  -5

  &gt;&gt;&gt; rdd.treeAggregate(0, add, add, 5)

  -5

  &gt;&gt;&gt; rdd.treeAggregate(0, add, add, 10)

  -5

  treeReduce(self, f, depth=2)

  Reduces the elements of this RDD in a multi-level tree pattern.

  :param depth: suggested depth of the tree (default: 2)

  &gt;&gt;&gt; add = lambda x, y: x + y

  &gt;&gt;&gt; rdd = sc.parallelize(\[-5, -4, -3, -2, -1, 1, 2, 3, 4\], 10)

  &gt;&gt;&gt; rdd.treeReduce(add)

  -5

  &gt;&gt;&gt; rdd.treeReduce(add, 1)

  -5

  &gt;&gt;&gt; rdd.treeReduce(add, 2)

  -5

  &gt;&gt;&gt; rdd.treeReduce(add, 5)

  -5

  &gt;&gt;&gt; rdd.treeReduce(add, 10)

  -5

  union(self, other)

  Return the union of this RDD and another one.

  &gt;&gt;&gt; rdd = sc.parallelize(\[1, 1, 2, 3\])

  &gt;&gt;&gt; rdd.union(rdd).collect()

  \[1, 1, 2, 3, 1, 1, 2, 3\]

  unpersist(self)

  Mark the RDD as non-persistent, and remove all blocks for it from

  memory and disk.

  values(self)

  Return an RDD with the values of each tuple.

  &gt;&gt;&gt; m = sc.parallelize(\[(1, 2), (3, 4)\]).values()

  &gt;&gt;&gt; m.collect()

  \[2, 4\]

  variance(self)

  Compute the variance of this RDD's elements.

  &gt;&gt;&gt; sc.parallelize(\[1, 2, 3\]).variance()

  0.666...

  zip(self, other)

  Zips this RDD with another one, returning key-value pairs with the

  first element in each RDD second element in each RDD, etc. Assumes

  that the two RDDs have the same number of partitions and the same

  number of elements in each partition (e.g. one was made through

  a map on the other).

  &gt;&gt;&gt; x = sc.parallelize(range(0,5))

  &gt;&gt;&gt; y = sc.parallelize(range(1000, 1005))

  &gt;&gt;&gt; x.zip(y).collect()

  \[(0, 1000), (1, 1001), (2, 1002), (3, 1003), (4, 1004)\]

  zipWithIndex(self)

  Zips this RDD with its element indices.

  The ordering is first based on the partition index and then the

  ordering of items within each partition. So the first item in

  the first partition gets index 0, and the last item in the last

  partition receives the largest index.

  This method needs to trigger a spark job when this RDD contains

  more than one partitions.

  &gt;&gt;&gt; sc.parallelize(\["a", "b", "c", "d"\], 3).zipWithIndex().collect()

  \[('a', 0), ('b', 1), ('c', 2), ('d', 3)\]

  zipWithUniqueId(self)

  Zips this RDD with generated unique Long ids.

  Items in the kth partition will get ids k, n+k, 2\*n+k, ..., where

  n is the number of partitions. So there may exist gaps, but this

  method won't trigger a spark job, which is different from

  L{zipWithIndex}

  &gt;&gt;&gt; sc.parallelize(\["a", "b", "c", "d", "e"\], 3).zipWithUniqueId().collect()

  \[('a', 0), ('b', 1), ('c', 4), ('d', 2), ('e', 5)\]

  ----------------------------------------------------------------------

  Data descriptors defined here:

  ****dict****

  dictionary for instance variables (if defined)

  ****weakref****

  list of weak references to the object (if defined)

  context

  The L{SparkContext} that this RDD was created on.
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

How to use Window in pyspark?
=============================

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf
from pyspark.sql import Row
sc = SparkContext("local", "my app name")

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

import numpy as np
np.random.seed(1)

keys = ["foo"] * 10 + ["bar"] * 10
values = np.hstack([np.random.normal(0, 1, 10), np.random.normal(10, 1, 100)])

df = sqlContext.createDataFrame([
   {"k": k, "v": round(float(v), 3)} for k, v in zip(keys, values)])
df.show()

from pyspark.sql.window import Window

w =  Window.partitionBy(df.k).orderBy(df.v)

print(w)
```

Databricks error
================

java.rmi.RemoteException: com.databricks.s3.S3Exception:
org.jets3t.service.S3ServiceException: S3 HEAD request failed for
&apos;/AuthorClusterWorkDir-20160121%2FDNG~HPCitemflatTable~&apos; -
ResponseCode=403, ResponseMessage=Forbidden; nested exception is:

This was because I did not enable the databricks role in the notebook.
After enabling this the issue went away.

Dbutils widget
==============

Db utils is a databricks specific thing. Databricks utilities

Learning spark
==============

How to learn?
-------------

<https://www.quora.com/Which-book-is-good-to-learn-Spark-and-Scala-for-beginners>

The best way to learn is read spark documentation.
<https://spark.apache.org/documentation.html>

Databricks being one of the committer to spark
<https://sparkhub.databricks.com/resources/>

And also start experimenting on spark shell (download and install spark
). Start with pyspark then move to spark-shell (scala).

To learn scala take coursera scala course
<https://www.coursera.org/learn/progfun1>

to know upcoming developments or if you want to contribute go to jira
(Spark - ASF JIRA)

<https://issues.apache.org/jira/browse/spark/?selectedTab=com.atlassian.jira.jira-projects-plugin%3Asummary-panel>

Go through Sameer Farooqui (Databricks) other videos on youtube
<https://www.youtube.com/results?search_query=sameer+farooqui>

For spark you could follow:

1.  Learning Spark: This books is good for spark fundamentals and spark
    architecture. It explains very efficiently the nuts and bolts behind
    the working of spark. It also gives a single chapter level
    introduction to various spark ecosystem frameworks like: Spark SQL,
    Spark Streaming, MLlib etc.
2.  Advanced Analytics with Spark: This book is mainly dedicated to
    Machine Learning. Each chapter in this book takes a use case and
    maps it to a Machine Learning algorithm and then solves the use case
    using that algorithm. This is not a beginners book, it needs basic
    understanding of Machine Learning and basics of Spark (like RDDs),
    if you are comfortable with these concepts and want to start with
    Data Science aspects then this is a great book as of now.

For Scala you could follow:

1.  Learning Scala: This is a great book to understand the basics and
    syntax of scala.
2.  Manning: Scala in Action: This book is like a complete reference. It
    starts from basics and then also covers advance concepts like:
    database connections, building web applications using scala,
    interoperability between java and scala etc.

Amit Padwal's reply in above quora link

There are a lot of books available in the market for Spark. But I would
suggest reading up a lot of free resources available on the internet
before you actually buy a book on Spark.

I have listed a few resources below for your convenience.. Hope this
helps you! :)

5 Things One Must Know About Spark Apache Spark vs Hadoop MapReduce Your
Guide To Career Opportunities In Spark Apache Spark & Scala - Edureka
Blog Spark SQL | Apache Spark Spark and Scala Online Training | Spark
Certification Course | Edureka

[DONE]{.done .DONE} \[\#B\] Revise spark tutorial {#b-revise-spark-tutorial}
-------------------------------------------------

SCHEDULED: &lt;2017-12-16 Sat 09:30&gt;

-   State "DONE" from "TODO" \[2017-12-15 Fri 11:31\]
-   State "DONE" from "TODO" \[2017-10-27 Fri 11:06\]
-   State "DONE" from "TODO" \[2017-10-23 Mon 11:17\]
-   State "DONE" from "TODO" \[2017-10-11 Wed 11:09\]
-   State "DONE" from "TODO" \[2017-09-14 Thu 10:28\]
-   State "DONE" from "TODO" \[2017-08-23 Wed 14:14\]
-   State "DONE" from "TODO" \[2017-08-17 Thu 10:07\]
-   State "DONE" from "TODO" \[2017-08-16 Wed 14:35\]
-   State "DONE" from "TODO" \[2017-07-20 Thu 14:37\]
-   State "DONE" from "TODO" \[2017-07-19 Wed 15:18\]
-   State "DONE" from "TODO" \[2017-06-22 Thu 13:21\]
-   State "DONE" from "TODO" \[2017-06-14 Wed 14:53\]

CLOCK: \[2017-06-14 Wed 13:56\]--\[2017-06-14 Wed 14:53\] =&gt; 0:57

-   State "DONE" from "TODO" \[2017-06-09 Fri 11:33\] CLOCK:
    \[2017-06-09 Fri 11:01\]--\[2017-06-09 Fri 11:33\] =&gt; 0:32

    -   State "DONE" from "TODO" \[2017-06-08 Thu 12:21\]

    CLOCK: \[2017-06-08 Thu 11:49\]--\[2017-06-08 Thu 12:21\] =&gt; 0:32
    -   State "DONE" from "TODO" \[2017-06-06 Tue 15:20\]

    CLOCK: \[2017-06-06 Tue 14:55\]--\[2017-06-06 Tue 15:19\] =&gt; 0:24
    -   State "DONE" from "TODO" \[2017-06-01 Thu 12:22\]

    CLOCK: \[2017-06-01 Thu 11:55\]--\[2017-06-01 Thu 12:22\] =&gt; 0:27
    -   State "DONE" from "TODO" \[2017-05-31 Wed 19:35\]

    :PROPERTIES:

:LAST~REPEAT~: \[2017-12-15 Fri 11:31\]

:END:

### [DONE]{.done .DONE} Subtask Play with emacs notebook or ipython notebook with same code {#subtask-play-with-emacs-notebook-or-ipython-notebook-with-same-code}

SCHEDULED: &lt;2017-12-22 Mon&gt;

Notes from databricks tutorial
==============================

Spark partition RDD creation
----------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")

data = list(range(1,10))
rDD = sc.parallelize(data, 4) # 4 partitions
print(rDD.collect())


```

Map on a spark RDD
------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")

data = list(range(1,10))
rDD = sc.parallelize(data, 4) # 4 partitions
print(rDD.collect())

rdd1 = rDD.map(lambda x: x * 2)
print(rdd1.collect())
```

Filter on a spark RDD
---------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")

data = list(range(1,10))
rDD = sc.parallelize(data, 4) # 4 partitions
print(rDD.collect())

even_rdd = rDD.filter(lambda x: x % 2 == 0)
print(even_rdd.collect())
```

Removing duplicate with distinct
--------------------------------

Default number of partitions is probably 1

### With 4 partitions distinct changes the output order

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")

data = list(range(1,10) + range(10)) # duplicate the same list twice
rDD = sc.parallelize(data, 4) # 4 partitions
print(rDD.collect())

distinct_rdd = rDD.distinct()
print(distinct_rdd.collect())
```

### With 1 partition distinct gives output in same ascending order

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")

data = list(range(1,10) + range(10)) # duplicate the same list twice
rDD = sc.parallelize(data)
print(rDD.collect())

distinct_rdd = rDD.distinct()
print(distinct_rdd.collect())
```

Usage of map like lambda x: \[x, x+1\]
--------------------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}

from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")

data = list(range(0, 10, 2))
odd_rdd = sc.parallelize(data, 4) # 4 partitions
print(odd_rdd.collect())

all_numbers_rdd = odd_rdd.map(lambda x: [x, x + 1])

print(all_numbers_rdd.collect())

```

Usage of flatMap like lambda x: \[x, x+1\]
------------------------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}

from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")

data = list(range(0, 10, 2))
odd_rdd = sc.parallelize(data, 4) # 4 partitions
print(odd_rdd.collect())

all_numbers_rdd = odd_rdd.flatMap(lambda x: [x, x + 1])

print(all_numbers_rdd.collect())

```

Usage of reduce
---------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")

data = list(range(1, 10 + 1))
rdd = sc.parallelize(data, 4) # 4 partitions
print(rdd.collect())

sum_of_rdd = rdd.reduce(lambda a, b: a + b)

print(sum_of_rdd)
print(sum(data))

```

Rdd take elements from take method
----------------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")

data = list(range(1, 10 + 1))
rdd = sc.parallelize(data, 4) # 4 partitions
print(rdd.collect())

taken_from_rdd = rdd.take(2)

print(taken_from_rdd)

```

Rdd collect elements collect method
-----------------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")

data = list(range(1, 10 + 1))
rdd = sc.parallelize(data, 4) # 4 partitions
print(rdd.collect())


```

Rdd take elements in ordered form takeOrdered method
----------------------------------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf
import random
sc = SparkContext("local", "my app name")

data = list(range(1, 10 + 1))
random.shuffle(data)
rdd = sc.parallelize(data, 4) # 4 partitions
print(rdd.collect())

takeordered_from_rdd = rdd.takeOrdered(5, lambda x: x)
print(takeordered_from_rdd)
takeordered_from_rdd = rdd.takeOrdered(5, lambda x: -x)
print(takeordered_from_rdd)
```

Rdd reduce elements by key reduceByKey method
---------------------------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf
import random
sc = SparkContext("local", "my app name")

data_list = [(1,2), (3,4), (3, 6), (1, 5), (2,4), (2, 3), (2, 3), (1, 3)]
data_list.sort()
rdd = sc.parallelize(data_list)
print(rdd.collect())

reduced_list = rdd.reduceByKey(lambda x, y: x + y).collect()
print(reduced_list)


```

Rdd sort elements by key sortByKey method
-----------------------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf
import random
sc = SparkContext("local", "my app name")

data_list = [(1,2), (3,4), (3, 6), (1, 5), (2,4), (2, 3), (2, 3), (1, 3)]
random.shuffle(data_list)
rdd = sc.parallelize(data_list)
print(rdd.collect())

sorted_list = rdd.sortByKey().collect()
print(sorted_list)

print((sorted(data_list, cmp=lambda x, y: cmp(x, y), key=lambda x: x[0])))

```

Rdd group elements by key groupByKey method
-------------------------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf
import random
sc = SparkContext("local", "my app name")

data_list = [(1,2), (3,4), (3, 6), (1, 5), (2,4), (2, 3), (2, 3), (1, 3)]
random.shuffle(data_list)
rdd = sc.parallelize(data_list)
print(rdd.collect())

grouped_list = rdd.groupByKey().collect()

for x, y in grouped_list:
    print("{}: ".format(x),)
    print(list(y))

```

Broadcast variables of spark
----------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf
import random
sc = SparkContext("local", "my app name")

broadcastVar = sc.broadcast([1,2,3])
print(broadcastVar.value)

```

Word count example
------------------

I should be expanding on the word count example. Read the spark tutorial
module 2 word count example

### Writing an example text file for testing

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
wordsworth="""My heart leaps up when I behold 
   A rainbow in the sky:
So was it when my life began; 
So is it now I am a man; 
So be it when I shall grow old, 
   Or let me die!
The Child is father of the Man;
And I could wish my days to be
Bound each to each by natural piety.
"""
filename = '/tmp/wordsworth.txt'
with open(filename, 'w') as f:
    f.write(wordsworth)
```

### Word count example

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")


def tostrings(str1):
    str2 = str1.strip()
    str_list = str2.split()
    return str_list


def towordcountpair(string1):
    return (string1, 1)

filename = "/tmp/wordsworth.txt"
lines = sc.textFile(filename)

words_list = lines.flatMap(tostrings)
print(words_list.collect())

wordcount_pair = words_list.map(towordcountpair)
print(wordcount_pair.collect())

final_word_count = wordcount_pair.reduceByKey(lambda a, b : a + b)

print(final_word_count.collect())

final_word_count = (lines.flatMap(tostrings).
                    map(towordcountpair).
                    reduceByKey(lambda a, b: a + b))

print(final_word_count.collect())

```

### Wordcount all displayed together

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")


def towordcountpair(string1):
    return (string1, 1)

filename = "/tmp/wordsworth.txt"

final_word_count = (sc.textFile(filename).
                    flatMap(lambda x: x.strip().split()).
                    map(lambda x: (x, 1)).
                    reduceByKey(lambda a, b: a + b))

print(final_word_count.collect())

```

Spark search
============

``` {.bash}
binisearch.py "spark"
```

Interesting spark stuff to look at
==================================

<https://discuss.analyticsvidhya.com/t/spark-cheatsheet/14278/2>

Quick cheatsheet
================

Loading data
------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output" rundoc-tangle="yes" rundoc-tangle="/tmp/spark_cheatsheet.py"}
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)

ls1 = [('a', 7), ('a', 2), ('b', 2)]
ls2 = [('a', 2), ('d', 1), ('b', 1)]
ls3 = [range(100)]
ls4 = [('a', ['x', 'y', 'z']), ('b', ['p', 'r'])]

rdd1 = sc.parallelize(ls1)
rdd2 = sc.parallelize(ls2)
rdd3 = sc.parallelize(ls3)
rdd4 = sc.parallelize(ls4)


```

FlatmapValues
-------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output" rundoc-tangle="yes" rundoc-tangle="/tmp/spark_cheatsheet.py"}

print((rdd4.)
flatMapValues(lambda x: x)
.collect())




```

Simulating flatmap values with flatmap
--------------------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output" rundoc-tangle="yes" rundoc-tangle="/tmp/spark_cheatsheet.py"}

print((rdd4.)
flatMapValues(lambda x: x)
.collect())


print((rdd4.)
map(lambda x: [(x[0], i) for i in x[1]])
.collect())


print((rdd4.)
flatMap(lambda x: [(x[0], i) for i in x[1]])
.collect())


```

iterating over rdd
------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output" rundoc-tangle="yes" rundoc-tangle="/tmp/spark_cheatsheet.py"}

def g(x):
    print(x)
# print(rdd1)
rdd1.foreach(g)
# print(help(rdd1))
def f(x): print(x)
sc.parallelize([1, 2, 3, 4, 5]).foreach(f)

```

Executing cheatsheets
---------------------

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}
2>&1 python /tmp/spark_cheatsheet.py
```

What are the methods in sqlcontext?
===================================

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
from pyspark import SparkContext, SparkConf

sc = SparkContext("local", "my app name")

from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)
print(help(sqlContext))
```
