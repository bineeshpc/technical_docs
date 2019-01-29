Installation git-lfs on ubuntu
==============================

``` {.bash .rundoc-block rundoc-language="sh" rundoc-dir="/sudo::" rundoc-results="output"}
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install git-lfs
git lfs install

```

How to disable color in git
===========================

git -c color.status=false status
