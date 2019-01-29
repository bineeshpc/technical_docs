Configuration file is here
==========================

/work/u/bpananga-sesadmin/run~incremental~/s3learn/s3cfg.liang

How to run an example s3 command in daisng1?
============================================

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}

ssh sesadmin@daisng01.int.thomsonreuters.com <<'EOF'
source .bpanangat/.zshrc
#Added my own keyst s3cfg.liang
#I might need to use the defaults that are in sesadmin home 
cd /work/u/bpananga-sesadmin/run_incremental/s3learn/
ls
s3cmd -c s3cfg.liang get s3://dais-ng/work_bineesh/block_out-unsorted/part.txt froms3.txt
echo '--------------'
ls
echo 'printing contents of s3'
head froms3.txt
echo '**************'
rm froms3.txt
ls
EOF
```

Info from Brian about s3 automation
===================================

Hi Bineesh, I think you may only be able to create/save Notebooks in
your own home directory. Maybe "/." is the root directory? I did make
one change, please let me know if you still have trouble creating a
notebook in your home directory.

&gt;

a) copy data from unix machine to aws / databricks node
-------------------------------------------------------

file:../only~storedlocally~/aws.org

### b) run the spark code(might be from notebook)

Sounds good

### c) copy the output back to the unix machine

OK.

&gt; &gt;Is there another way to run apart from using notebook? Like ssh
to the &gt;cluster node and run code from there. Is the cluster ssh
enabled?

For Qubole you can ssh, but Databricks does not allow it. Running code from Notebook is the way to go there.
------------------------------------------------------------------------------------------------------------

&gt;Can I invoke code in notebook from outside unix machine using
python?

There is an IDE plugin, but I think it's only for Scala. For python it
looks like you have to run it from Databricks Notebook page directly.

&gt;I am thinking about using command

aws cp &lt;localpath&gt; &lt;awspath&gt;
----------------------------------------

AWS cli is good - I think you have to have a credentials file set up
with the above keys, maybe you already do. If you run into problems
there's also a hadoop distcp command, but this can be more difficult to
set up.

Thanks, let me know if you run into problems. Brian

s3 command help
===============

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}
ssh sesadmin@daisng01.int.thomsonreuters.com <<'EOF'
source .bpanangat/.zshrc
s3cmd -h
EOF
```

s3 command used by Linge
========================

/work/u/lbai-sesadmin

s3cmd -c .key put --recursive
*daisng1/work/AuthorClusterWorkDir-20160121/collected~hpc~/HPC.0002
s3://dais-ng/AuthorClustering-Core-20160121/collected~hpc~*

How to connect to ec2 instance created by me
============================================

Open an SSH client. (find out how to connect using PuTTY) Locate your
private key file (ec2~bineesh~.pem). The wizard automatically detects
the key you used to launch the instance. Your key must not be publicly
viewable for SSH to work. Use this command if needed: chmod 400
ec2~bineesh~.pem Connect to your instance using its Public DNS:
ec2-35-163-236-9.us-west-2.compute.amazonaws.com Example: ssh -i
"\~/.ssh/ec2~bineesh~.pem"
ec2-user@ec2-35-163-236-9.us-west-2.compute.amazonaws.com Please note
that in most cases the username above will be correct, however please
ensure that you read your AMI usage instructions to ensure that the AMI
owner has not changed the default AMI username.

My private key file
===================

``` {.bash .rundoc-block rundoc-language="sh" rundoc-results="output"}
ls ~/.ssh/ec2_bineesh.pem
```

Yum install as usual
====================

<http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/install-software.html>

Pip install
===========

<http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-linux.html>
