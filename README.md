Simple interview script for sonos with the following requirements:

"Using your favorite language, create a tool which uses AWS API access to list all EC2 instances in a single account/region, sorted by the value of a tag each instance has called ‘Owner’.

The tool should display the results in an easy to read format which includes the instance id, tag value, instance type and launch time.

The tool should work for any number of instances, and should display any instances without an Owner tag as type 'unknown' with the instance id, type and launch time.

Design the tool so it could be used later to find tags with other names and print other instance details in the report."

A few notes:
1) The creds used will be emailed but have been limited to *only* have access to list against the EC2 api.

2) Instances are *not* currently running, as I didn't want to pay for keeping the instances running

3) This by default checks us-east-1, but will check *any* region

4) Output is by default csv, I thought that would be the easiest to translate into any usable format later:

```
% ./get_instances.py AWS_KEY AWS_SECRET us-east-1 --tag Owner
id,instance_type,launch_time,Owner
i-0e743cf7,t2.micro,2016-02-02T22:17:07.000Z,Akira
i-1d743ce4,t2.nano,2016-02-02T22:18:11.000Z,Clancy
i-456821bc,t2.micro,2016-02-01T21:03:08.000Z,Homer
i-596821a0,t2.micro,2016-02-01T21:03:08.000Z,Ziff
i-586821a1,t2.micro,2016-02-01T21:03:08.000Z,undefined
i-b2561f4b,t2.micro,2016-02-01T20:59:19.000Z,undefined
```

5) Script has -v and -h options, which spit out indepth logging and help entries respectively

6) The attributes that were given are directly available from the boto ec2 instance object, and are listed at the top of the script.


