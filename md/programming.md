---
headers: ':classname HelloWorld'
---

Hello world
===========

Hello World program is the first program to write in any programming
language.

Python
------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
print "hello world"
```

Shell
-----

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}
echo "hello world"
```

Scala
-----

``` {.scala .rundoc-block rundoc-language="scala" rundoc-results="output"}
println("Hello World")
```

Java
----

Java classname should be given in header

``` {.java .rundoc-block rundoc-language="java" rundoc-results="output" rundoc-exports="both"}

public class HelloWorld {
    public static void main(String[] args){
        System.out.println("Hello World");
    }
}
```

``` {.example}
Hello World
```

Trying a C program
------------------

This is more difficult because this is a compiled language Main is not
required. If you don't give main an implicit main is included.

``` {.c .rundoc-block rundoc-language="C" rundoc-results="output" rundoc-tangle="yes" rundoc-tangle="/tmp/hello.c"}

printf("Hello World\n");

```

Using implicit main again to add 2 numbers.

``` {.c .rundoc-block rundoc-language="C" rundoc-results="output"}
int a=1;
int b=1;
printf("%d\n", a+b);

```

Here I have added an explicit main function. It is working fine.

``` {.c .rundoc-block rundoc-language="C" rundoc-results="output"}

print_one_to_maxnum(int max_num)
{
   int i;
   for(i=1; i < max_num ; i++)
       printf("%d, ", i);
   printf("%d\n", max_num);
}
int main()
{
   print_one_to_maxnum(5);
   return 0;
}
```

Java script
===========




Elisp
=====

``` {.elisp .rundoc-block rundoc-language="elisp" rundoc-results="output"}
(print "hello world")

```

``` {.elisp .rundoc-block rundoc-language="elisp" rundoc-results="output"}
(defun print-string (s count maxvalue)
  (print s)
  (cond ((< count maxvalue) (print-string s (+ count 1) maxvalue)))
  )
(print-string "hello world" 1 5)
(cond ((< 4 5) (print "True" )))
```

Scala
=====

Hello world
-----------

``` {.scala .rundoc-block rundoc-language="scala" rundoc-results="output"}
object HelloWorld {
  def main(args: Array[String]): Unit = {
    println("Hello, world!")
  }
}


```

Basic types
-----------

Variables
---------

``` {.scala .rundoc-block rundoc-language="scala" rundoc-results="output"}
val x = 10
println(x)
var y = 10

y = 11
println(y)

val z: Int = 10
val a: Double = 1.0

// Notice automatic conversion from Int to Double, result is 10.0, not 10
val b: Double = 10

var h:String = "hello world"
println(h.length)
println(h.replace('h' , 'H'))
```

Control structures
------------------

### Conditional statements

1.  Trivial conditional

    ``` {.scala .rundoc-block rundoc-language="scala" rundoc-results="output"}
    val foo = false
    val bar = "bar"
    val baz = "baz"    
    val res = if (foo) bar else baz
    print(res) 
    ```

    ``` {.scala .rundoc-block rundoc-language="scala" rundoc-results="output"}
    var x = 0
    while (x < 5)
    {
    println(x)
    x += 1
    }

    val terminate = 5
    var i = 0
    do {
      println(s"$i is still less than $terminate")
      i += 1
    } while (i < terminate)

    val r = 1 to 5
    println(r)
    r.foreach(println)

    r foreach println
    ```

functions
---------

### Simple function

``` {.scala .rundoc-block rundoc-language="scala" rundoc-results="output"}
def SimpleFunction = 3
println(SimpleFunction)

```

### Function with one variable

``` {.scala .rundoc-block rundoc-language="scala" rundoc-results="output"}

```

``` {.scala .rundoc-block rundoc-language="scala" rundoc-results="output"}
def oneVariable_cube(a: Int) = a * a * a

println(oneVariable_cube(3))
```

### Function with two variables

``` {.scala .rundoc-block rundoc-language="scala" rundoc-results="output"}

def subtract(x: Int, y: Int): Int = x - y

def hypotenuse(base: Double, altitude: Double): Double = math.sqrt(base * base + altitude * altitude)

println(hypotenuse(3, 4))
println(subtract(5, 4))


```

Inbuilt data structures
-----------------------

File IO
-------

Command line arguments
----------------------

Data structures
---------------

Learn x in y minutes
====================

<https://learnxinyminutes.com/>

[DONE]{.done .DONE} Read elisp section first pass {#read-elisp-section-first-pass}
-------------------------------------------------

SCHEDULED: &lt;2016-10-26 Wed&gt;

[DONE]{.done .DONE} Read scala section first pass {#read-scala-section-first-pass}
-------------------------------------------------

SCHEDULED: &lt;2016-10-27 Thu&gt;

[DONE]{.done .DONE} \[\#B\] Read java section first pass {#b-read-java-section-first-pass}
--------------------------------------------------------

SCHEDULED: &lt;2016-11-01 Tue&gt;

Decorator
=========

Python
------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
def funA(a):
    def wrapper():
        print 'entering funA'
        a()
        print 'exiting from funA'
    return wrapper

def funB(b):
    def wrapper():
        print 'entering funB'
        b()
        print 'exiting from funB'
    return wrapper



@funA
@funB
def funC():
    print 'inside funC'


funC()

```

guile scheme
============

This is partially working. Mic scheme is not working properly with emacs
org mode Even guile is not working properly

``` {.scheme}
(car (cdr (list 'singam 'karthi 'bini)))
```

``` {.scheme .rundoc-block rundoc-language="scheme" rundoc-tangle="yes" rundoc-tangle="/tmp/zdefine.ss"}
(define pi 3.14)
(define (square x) (* x x))

```

What is pig latin?
------------------

Piglatin(scheme) = emeschay scheme chemes hemesc emesch emeschay

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output" rundoc-tangle="yes" rundoc-tangle="/tmp/piglatin.ss"}

(define (vowel letter)
(if (memq letter (list 'a 'e 'i 'o 'u))
#t
#f
))

(define lst1 (list 'a 'b 'c 'd))
(define lst2 (list 'e 'f 'g))

(define (extend lst1 lst2)
(let ((first (car lst2))
      (rest (cdr lst2))
     )
      (if (eq? rest ())
        (append lst1 first)
        (append (append lst1 first) rest)
      )
))

(extend lst1 lst2)

(pigl word
(let ((first (car word))
      (rest (cdr word))
      )
     (if (vowel first)
         (word)
         (pigl word (list rest first)))
)
(vowel 'a)

(pigl (list 'korea))
```
