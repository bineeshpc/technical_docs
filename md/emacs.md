---
results: 'files_list'
---

Installation on ubuntu
======================

``` {.bash .rundoc-block rundoc-language="sh" rundoc-dir="/sudo::" rundoc-results="output"}
2>&1 apt install emacs-goodies-el

```

Things to know
==============

Moving around
-------------

C - control M - Meta (In no meta Esc release then type character) C-x
C-c (quit emacs) C-g (quit a partially entered command)

C-v next screen M-v previous screen C-l

C-p C-b C-f C-n

Getting help
------------

You can get help for a command by typing

C-h c command-name

This will usually tell you if it is bound to a key. (If multiple
bindings are set for the command they will all be listed.)

Given a key sequence, you can type

C-h k key-sequence

To get the command that would run.

You can get detailed information about a command, also any
non-interactive function defined, by typing

C-h f function-name

Which give you detailed information about a function, which will include
any key bindings for it.

C-h f variable-name

Key-maps are kept in variables, however the key codes are stored in a
raw format. Try C-h v isearch-mode-map for an example.

For more help on getting help, you can type

C-h ?

[DONE]{.done .DONE} How to schedule recurring meeting {#how-to-schedule-recurring-meeting}
=====================================================

SCHEDULED: &lt;2016-10-20 Thu&gt; +1d, +1w, +1m etc can be added to
schedule recurring meeting

++1d to shift time to future .+1d to shift time to today + 1d future

TODO Empty kitchen trash 2008-02-15 Wed 20:00 ++1d Marking this DONE
will shift the date by at least one day, and also by as many days as it
takes to get the timestamp into the future. Since there is a time in the
timestamp, the next deadline in the future will be on today's date if
you complete the task before 20:00. Check the batteries in the smoke
detectors 2008-02-15 Wed 20:00 .+1d

Marking this DONE will shift the date to one month after today.

How to add tags?
================

C-c C-q and add the tag

Global visual line mode for line wrap
=====================================

M-x global-visual-line-mode

Toggle truncate lines
=====================

M-x toggle-truncate-lines

[DONE]{.done .DONE} How to save or tangle a source yes {#how-to-save-or-tangle-a-source-yes}
======================================================

in org mode? org-babel-tangle Tangle the current file. Bound to C-c C-v
t.

With prefix argument only tangle the current 'src' code block.

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output" rundoc-tangle="yes" rundoc-tangle="/tmp/source_code134.py"}
print 1
```

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}
cat /tmp/source_code134.py
```

How to hide body in org mode?
=============================

M-x hide-body

``` {.elisp}
(hide-body)
```

Install elpy
============

<https://github.com/jorgenschaefer/elpy>

``` {.elisp}
(require 'package)
(add-to-list 'package-archives
             '("elpy" . "https://jorgenschaefer.github.io/packages/"))
(package-refresh-contents)

```

Followed by M-x package-install RET elpy RET

[DONE]{.done .DONE} Install a separate emacs compiled from source {#install-a-separate-emacs-compiled-from-source}
=================================================================

SCHEDULED: &lt;2017-07-14 Fri&gt;

Did this but had a few issues Probably png will not work in emacs.
Because I used libpng12-dev because other versions were giving me
problems I went ahead with libpng12-dev and with-png=no option for the
time being. Installation worked. I should probably test it and slowly
migrate to this version of emacs.

``` {.bash .rundoc-block rundoc-language="sh" rundoc-dir="/sudo::" rundoc-results="output"}
#2>&1 apt install libxpm-dev 
apt install libjpeg-dev lib-gif libtiff libpng12-dev

```

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}
cd ~/temp
rm -rf emacs
mkdir -p emacs
cd emacs-25.2
make clean > /dev/null
make distclean > /dev/null
./autogen.sh > /tmp/autogen.out
echo $?
#./configure --prefix=$HOME/temp/emacs
./configure --with-x-toolkit=gtk3 --with-png=no --prefix=$HOME/temp/emacs > /tmp/configure.out
#./configure --with-x-toolkit=gtk3 --prefix=$HOME/temp/emacs > /tmp/configure.out
echo $?
make > /tmp/make.out
echo $?
make install > /tmp/install.out
echo $?
```

[DONE]{.done .DONE} Play around with new version of emacs {#play-around-with-new-version-of-emacs}
=========================================================

SCHEDULED: &lt;2017-12-30 Sat 13:30&gt;

Literate programming Test tangle with multiple source tangled to same output file
=================================================================================

This can be used for literate programming

Part 1
------

This is part one of the program

``` {.python .rundoc-block rundoc-language="python" rundoc-tangle="yes" rundoc-tangle="/tmp/test_tangle123.py"}
print "part 1"
```

Part 2
------

This is part two of the program

``` {.python .rundoc-block rundoc-language="python" rundoc-tangle="yes" rundoc-tangle="/tmp/test_tangle123.py"}
print "part 2"
```

Part 3
------

This is part three of the program

``` {.python .rundoc-block rundoc-language="python" rundoc-tangle="yes" rundoc-tangle="/tmp/test_tangle123.py"}
print "part 3"
```

Part 4
------

This is part one of the program

``` {.python .rundoc-block rundoc-language="python" rundoc-tangle="yes" rundoc-tangle="/tmp/test_tangle123.py"}
print "part 4"
```

Remote editing of files
=======================

For GNU Emacs

C-x C-f /remotehost:filename RET (or /method:user@remotehost:filename)

For XEmacs use the syntax

C-x C-f /\[method/user@remotehost\]/filename

You can also edit local files as root with either of the following (note
the double colon, which is required)

C-x C-f /su::/etc/hosts C-x C-f /sudo::/etc/hosts

Good tutorial
=============

<http://ehneilsen.net/notebook/orgExamples/org-examples.html>

Insert file contents in emacs
=============================

<https://www.gnu.org/software/emacs/manual/html_node/elisp/Reading-from-Files.html>
M x insert-fil (insert-file-contents /tmp/c.sh nil)

Org mode batch execution
========================

This script can be used to execute an entire org mode file from
commandline Output cannot be seen But I will figure out that

Org security is overridden with (setq org-confirm-babel-evaluate nil)
<https://orgmode.org/manual/Code-evaluation-security.html>
<https://orgmode.org/manual/Batch-execution.html>

\#!/bin/sh

\# emacs -Q --batch --eval " (progn (require 'ob-tangle) ;; programming
languages supported in org mode (org-babel-do-load-languages
'org-babel-load-languages '( (python . t) (sh . t) (scala . t) (C . t)
(java . t) (plantuml . t) (scheme . t) (latex . t) ;;(ipython . t) ))
(setq org-confirm-babel-evaluate nil) (dolist (file
command-line-args-left) (with-current-buffer (find-file-noselect file)
(org-babel-execute-buffer)))) " "\$@"

Interesting cheatsheet about org babel
======================================

<https://necromuralist.github.io/posts/org-babel-cheat-sheet/>

Learned about org-babel-execute-buffer from above link

Literate devops in org mode
===========================

<http://www.howardism.org/Technical/Emacs/literate-devops.html>

Idea is to check the movies in my raspberry pi
----------------------------------------------

``` {#files_list .bash .rundoc-block rundoc-language="sh" rundoc-results="list"}
ls | head -3
```

```

``` {.bash .rundoc-block rundoc-language="sh" rundoc-var="my_list=files_list"}
echo $my_list

```

``` {.bash .rundoc-block rundoc-language="sh" rundoc-dir="/usr"}
ls
```

``` {.bash .rundoc-block rundoc-language="sh" rundoc-dir="/ssh:pi@10.47.47.10:/usr"}
ls
```

``` {.bash .rundoc-block rundoc-language="sh" rundoc-session="client"}
ssh pi@10.47.47.10
```

``` {.bash .rundoc-block rundoc-language="sh" rundoc-session="client"}
hostname
```

``` {.bash .rundoc-block rundoc-language="sh" rundoc-session="client"}
filename=/tmp/read_movies.py
cat > $filename << 'delim'
import os
filename = '/tmp/movies.txt'
lines = [line.strip() for line in open(filename)]
print('')
s = set()
for i in range(0, len(lines), 4):
    filmname = lines[i]
    to_search = filmname.strip().split()[0]
    s.add(to_search)
s.remove('excuted')
os.system('mkdir /tmp/movies')
cmd = '/usr/bin/python ~/agile/get_movie_links/analyse.py {word} > /tmp/movies/{word}.txt'
for word in s:
    cmd_concrete = cmd.format(word=word)
    print(cmd_concrete)
    os.system(cmd_concrete)
delim
cd ~/agile/get_movie_links
python $filename
```

``` {.bash .rundoc-block rundoc-language="sh" rundoc-session="client"}
cd /tmp
cat ~/bin/get_movies.sh
#python3 -m http.server
```

Show inline images
==================

Adding a hook to execute after C-c C-c (add-hook
'org-babel-after-execute-hook 'org-redisplay-inline-images)

<https://orgmode.org/manual/In_002dbuffer-settings.html>

<https://emacs.stackexchange.com/questions/30520/org-mode-c-c-c-c-to-display-inline-image>

<https://stackoverflow.com/questions/17621495/emacs-org-display-inline-images>

<https://orgmode.org/manual/Handling-links.html#Handling-links>

Test the session
================

Initialize session
------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-session="yes" rundoc-results="output"}
x = 1

```

Since session was used in the code it worked
--------------------------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-session="yes" rundoc-results="output"}
print(x)

```

Since session was not used in the code it failed
------------------------------------------------

``` {.python .rundoc-block rundoc-language="python" rundoc-results="output"}
print(x)

```
