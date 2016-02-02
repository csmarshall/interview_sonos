# interview_sonos

Simple interview script for sonos with the following requirements:

"Using your favorite language, create a tool which uses AWS API access to list all EC2 instances in a single account/region, sorted by the value of a tag each instance has called ‘Owner’.

The tool should display the results in an easy to read format which includes the instance id, tag value, instance type and launch time.

The tool should work for any number of instances, and should display any instances without an Owner tag as type 'unknown' with the instance id, type and launch time.

Design the tool so it could be used later to find tags with other names and print other instance details in the report."

A few notes:
1) The creds used will be emailed but have been limited to *only* have access to list against the EC2 api.

2) Instances are *not* currently running, as I didn't want to pay for keeping the instances running :)_

3) This by default checks us-east-1, but will check *any* region


