Installing robotframework using anaconda
========================================

Search for a package
--------------------

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}
anaconda search -t conda robotframework
```

Show a package
--------------

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}
anaconda show chen/robotframework
```

Installing a package
--------------------

Installed robot framwork 2.8.\* because our code was validating for
robotframework version bigger than 2.7 but not 3

``` {.bash}
conda install --channel https://conda.anaconda.org/userzimmermann robotframework
```

Knowledge repo
==============

Commit
------

``` {.bash}
hg status
```

``` {.bash}
commit_message='attempting a fix for images not displayed in generated md files'
python move_data.py
#hg commit -m $commit_message
cd ~/Dropbox/technical_docs
python make_md.py
git status
#git commit -a -m $commit_message
```

Git
---

<file:git.org>

Mercurial
---------

hg commit -m "\$(date +'%c')"

abort: no username supplied (use "hg config --edit" to set your
username)

Status
------

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}


status1()
{
dir1=$HOME/temp/$1
cd $dir1
echo I am in directory $dir1
hg status
cd -

}



status1 projects
status1 projects/tr_clarivate_work
```

Diff
----

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}


diff1()
{
dir1=$HOME/temp/$1
cd $dir1
echo I am in directory $dir1
hg diff
cd -

}


diff1 projects > /tmp/projects_diff
diff1 projects/tr_clarivate_work > /tmp/stability_diff
emacs /tmp/projects_diff /tmp/stability_diff &
```

Commit
------

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}


commit1()
{
dir1=$HOME/temp/$1
cd $dir1
2>&1 hg commit -m "$(date)"
cd -

}



commit1 projects
commit1 projects/tr_clarivate_work
```

check log
---------

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}


log1()
{
dir1=$HOME/temp/$1
cd $dir1
pwd
hg log -l 2

}



log1 projects
log1 stability_daisid_dn57
```

Status Diff Commit and check log all done together
--------------------------------------------------

### StatusDiff

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}


status1()
{
dir1=$HOME/temp/$1
cd $dir1
hg status
cd -

}



status1 projects
status1 stability_daisid_dn57

diff1()
{
dir1=$HOME/temp/$1
cd $dir1
hg diff
cd -

}


diff1 projects > /tmp/projects_diff
diff1 stability_daisid_dn57 > /tmp/stability_diff

commit1()
{
dir1=$HOME/temp/$1
cd $dir1
2>&1 hg commit -m "$(date)"
cd -

}



commit1 projects
commit1 stability_daisid_dn57


log1()
{
dir1=$HOME/temp/$1
cd $dir1
pwd
hg log -l 2

}



log1 projects
log1 stability_daisid_dn57

```

Mercurial server in daisng01
----------------------------

Clone the mercurial repo here. Add a new mercurial repo remotely. Make
this repo pushable remotely.

This can be done easily manually. Only thing to be added in .hgrc is

bineesh@ubuntu14:\~/dn185/AuthorCluster/AuthorClusterComponents\$ cat
.hg/hgrc \[paths\] default =
/home/bineesh/AuthorCluster/AuthorClusterComponents daisng01 =
<ssh://sesadmin@daisng01.int.thomsonreuters.com//work/u/bpananga-sesadmin/dn185/AuthorCluster/AuthorClusterComponents>

Emacs
=====

<file:emacs.org>

Amazon web services
===================

<file:aws.org>

Things to install on a new machine
==================================

ubuntu~16~.04~1~

When dns is not working on Guest Do this where ubuntu~16~.04~1~ is the
vm name VBoxManage modifyvm "ubuntu~16~.04~1~" --natdnshostresolver1 on
VBoxManage setextradata global natdnshostresolver1 on

ssh keys id~rsa~ id~rsa~.pub

firefox settings

emacs settings elpa in emacs .emacs link to dropbox emacs folder

Install all packages

Enable workspaces Change number of workspaces using compiz config
manager or unity tweak tool For me compiz worked on ubuntu 16.04

configure bashrc paths copy bash~history~

Link screenrc to Dropbox

List the installed things in ubuntu
-----------------------------------

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}
my_packages=/tmp/installed-packages
just_packages=/tmp/just-packages
apt list --installed > $my_packages
awk -F '/' '{print $1}' $my_packages | tail -n +2 | tee $just_packages 
```

Install things
--------------

``` {.bash .rundoc-block rundoc-language="sh" rundoc-dir="/sudo::" rundoc-results="output"}
apt install detox emacs vim

```

some common config files
------------------------

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}
cd ~/
files=".emacs .bash_history .screenrc"

for file1 in $files
do
ls -l $file1
done
```

Tried to install davmail
------------------------

<http://davmail.sourceforge.net/gettingstarted.html>
<http://davmail.sourceforge.net/thunderbirdmailsetup.html>

How to send vacation requests
=============================

Outlook vacation request
<https://support.office.com/en-us/article/Add-time-away-from-the-office-to-coworkers-Outlook-calendars-69FE38AA-7B5F-4225-8B69-47F47092E65E#ID0EAACAAA=2016,_2013,_2010>

How to share files between host and guest in virtual box?
=========================================================

Shared folders
--------------

Create a shared folder name in my example I am trying to share a folder
named C:\shared~withvm~

In the shared folder settings add this folder. Give whatever name you
want to give

Go to the guest and type

mount -t vboxsf shared~withvm~ *home/bineesh/host*

shared~withvm~ is the name I gave on shared folder settings

/home/bineesh/host is the folder I want it mounted on.

These folders are mounted as root.

### Backing up anaconda2 to make room for upgrade

drwxrwxr-x 20 bineesh bineesh 4096 Sep 18 2017 anaconda2

bineesh@ubuntu-16:\~\$ ls -l anaconda2/ total 144 drwxrwxr-x 2 bineesh
bineesh 12288 Jun 12 18:06 bin drwxrwxr-x 2 bineesh bineesh 12288 Sep 18
2017 conda-meta drwxrwxr-x 3 bineesh bineesh 4096 Feb 9 2017 doc
drwxrwxr-x 2 bineesh bineesh 4096 Feb 9 2017 envs drwxrwxr-x 7 bineesh
bineesh 4096 Feb 9 2017 etc drwxrwxr-x 26 bineesh bineesh 4096 Feb 9
2017 include drwxrwxr-x 14 bineesh bineesh 32768 Feb 9 2017 lib
drwxrwxr-x 3 bineesh bineesh 4096 Feb 9 2017 libexec -rw-rw-r-- 1
bineesh bineesh 4524 Feb 5 2016 LICENSE.txt drwxrwxr-x 97 bineesh
bineesh 4096 Feb 9 2017 mkspecs drwxrwxr-x 2 bineesh bineesh 4096 Feb 9
2017 phrasebooks drwxrwxr-x 210 bineesh bineesh 12288 Sep 18 2017 pkgs
drwxrwxr-x 15 bineesh bineesh 4096 Feb 9 2017 plugins drwxrwxr-x 14
bineesh bineesh 4096 Feb 9 2017 qml drwxrwxr-x 2 bineesh bineesh 4096
Feb 9 2017 sbin drwxrwxr-x 18 bineesh bineesh 4096 Feb 9 2017 share
drwxrwxr-x 3 bineesh bineesh 4096 Feb 9 2017 ssl drwxrwxr-x 2 bineesh
bineesh 12288 Feb 9 2017 translations drwxrwxr-x 3 bineesh bineesh 4096
Feb 9 2017 var

Use winscp to share
-------------------

Use samba to share
------------------

Use http to share
-----------------

Apache
======

sudo apt install apache2 sudo systemctl restart apache2.service

``` {.bash .rundoc-block rundoc-language="sh" rundoc-dir="/sudo::" rundoc-results="output"}
apt install libapache2-mod-wsgi  

```

Converting tex to org
=====================

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}
pandoc -f latex -t org << END
 \documentclass{paper}
 \begin{document}
 \section{Heading}

 Hello

 \subsection{Sub-heading}

 \textbf{World}!
 \end{document}
 END


```

Docker
======

[DONE]{.done .DONE} Install docker on my machine {#install-docker-on-my-machine}
------------------------------------------------

SCHEDULED: &lt;2017-06-28 Wed 11:00&gt;

### Step 1 Apt get update and install dependencies

``` {.bash .rundoc-block rundoc-language="sh" rundoc-dir="/sudo::" rundoc-results="output"}
apt-get update
apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

```

### Step 2 Add dockers official GPG Key

``` {.bash .rundoc-block rundoc-language="sh" rundoc-dir="/sudo::" rundoc-results="output"}
pwd
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
apt-key fingerprint 0EBFCD88
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

### Step 3 Add a stable repository

``` {.bash .rundoc-block rundoc-language="sh" rundoc-dir="/sudo::" rundoc-results="output"}
pwd

add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

```

### Step 3 Update packages and install docker

``` {.bash .rundoc-block rundoc-language="sh" rundoc-dir="/sudo::" rundoc-results="output"}
pwd
apt-get update
apt-get install docker-ce
#docker run hello-world

```

### Step 4 Test docker with hello world

``` {.bash .rundoc-block rundoc-language="sh" rundoc-dir="/sudo::" rundoc-results="output"}
docker run hello-world

```

[DONE]{.done .DONE} Go through the docker tutorial {#go-through-the-docker-tutorial}
--------------------------------------------------

SCHEDULED: &lt;2017-07-17 Mon 11:00&gt; CLOCK: \[2017-07-14 Fri
12:35\]--\[2017-07-14 Fri 12:38\] =&gt; 0:03

### Orientation

<https://docs.docker.com/get-started/>

### Containers

<https://docs.docker.com/get-started/part2/>

1.  Dockerfile

2.  App

3.  Build app

4.  Run app

5.  Share image

6.  Publish image

7.  Pull and run image

### Services

### Swarm

### Stacks

### Deploy your app

Rsycnc and scp choice
=====================

Use rsync when there are large number of files or if the data is huge

This is the one I used.

rsync -avzhe ssh --progress /home/rpmpkgs
root@192.168.0.100:/root/rpmpkgs -a archive -v verbose -z compress -h
human readable -e specify the remote shell to use

rsync -avzhe ssh --progress incremental
ec2-user@10.152.54.25:incremental

<https://www.tecmint.com/rsync-local-remote-file-synchronization-commands/>

Passwordless ssh
================

cat .ssh/id~rsa~.pub | ssh sheena@192.168.0.11 'cat &gt;&gt;
.ssh/authorized~keys~'

cat .ssh/id~rsa~.pub | ssh
bineesh.panangat@bastion.prod.cc.oneplatform.build 'cat &gt;&gt;
.ssh/authorized~keys~'
