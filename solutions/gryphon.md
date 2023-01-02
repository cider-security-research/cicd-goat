Let's explore what we have when signing in to the compromised GitLab:
You are tha maintainer of *pygryphon* package, there are also public projects *nest-of-gold* and *awesome-app* which we have a read-only access.
<BR><BR>
As the instructions of this challenge hint us, let's try to see if we can find any reference to *Flag11*, 
After doing a simple search, we can learn it is being referenced by *nest-of-gold* project 

![grpyhon](../images/gryphon-1.png "grpyhon")

  

We can see that *Flag11* is used in a pipeline that ships a container used in production.
Let's go to this pipeline scheduling, we can see that user named "gryphon" is the owner of this pipeline, and this user is also the owner of the *awesome-app* project's pipeline.
  
Diving into *awesome-app*, it is using our pygrphon package as a dependecy!  
this is what the *requirments.txt* file looks like:
  
 <pre><code>
 
 --extra-index-url http://token:cd79dd622c6d463a574635e874765c0b@gitlab/api/v4/projects/pygryphon%2Fpygryphon/packages/pypi/simple --trusted-host gitlab

pytest==7.2.0
flask==2.0.3
Werkzeug==2.0.3
pygryphon==1.0.13
 
</code></pre> 
  
This means we can influence *awesome-app* pipeline by uploading a new maclious python package of *pygrphon*.
Our end goal is within *nest-of-gold* project, how can we influence it's pipeline?
  
GitLab has a special setting whether or not a pipeline "CI_JOB_TOKEN" is limited to the specific project or have access to the other projects under the same user.
This mean if this setting is disabled, we might be able 
  
![grpyhon2](../images/gryphon-2.png "grpyhon2")  
  
