#!/usr/local/bin/python
from __future__ import print_function
import argparse
import boto.ec2
import logging
import sys

access_key = ''
secret_key = ''
region = ''
tag = ''

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')

logger = logging.getLogger('report_instance_info')

# Top level attributes of the boto ec2 instance object to print
attributes_to_print = ['id', 'instance_type', 'launch_time']

# Some of boto logic from here:
# https://cloudpages.wordpress.com/2013/12/18/listing-all-of-your-ec2-instances-using-boto/

def get_ec2_instances(access_key, secret_key, region):
    instances_unsorted = []
    logger.info("Establishing connection with EC2")
    try:
        ec2_conn = boto.ec2.connect_to_region(region,
                                              aws_access_key_id=access_key,
                                              aws_secret_access_key=secret_key)
        reservations = ec2_conn.get_all_reservations()
        logger.info("Getting all reservations in %s" % region)
    except:
        logger.critical("There are issues with your EC2 connection")
        sys.exit(1)
    for reservation in reservations:
        logger.info("Getting all instances for reservation: %s" % reservation)
        for instance in reservation.instances:
            logger.info("Getting info for instance: %s" % instance.id)
            instances_unsorted.append(instance)
            if tag not in instances_unsorted[-1] .tags:
                instances_unsorted[-1] .tags[tag] = "undefined"
    return instances_unsorted


def present_ec2_instances(instances_unsorted, attributes_to_print, tag):
    logger.info("Printing header csv line")
    for attribute in attributes_to_print:
        print("%s," % attribute, end="")
    print(tag)
    logger.info("Printing instance info sorted")
    instances_sorted = sorted(instances_unsorted, key=lambda k: k.tags[tag])
    for instance in instances_sorted:
        for attribute in attributes_to_print:
            print("%s," % (getattr(instance, attribute)), end="")
        print("%s" % instance.tags[tag])


def main():
    global access_key
    global secret_key
    global region
    global tag
    global attributes_to_print

    parser = argparse.ArgumentParser()
    parser.add_argument('access_key', type=str, help='AWS Access Key')
    parser.add_argument('secret_key', type=str, help='AWS Secret Key')
    parser.add_argument('region', type=str, default='us-east-1',
                        help='Region to investigate')
    parser.add_argument("--tag", type=str, default='owner',
                        help="instance tag to sort by")
    parser.add_argument('-v', '--verbose', action='store_true',
                        help="print log entries")
    args = parser.parse_args()
    access_key = args.access_key
    secret_key = args.secret_key
    region = args.region
    tag = args.tag

    if args.verbose is True:
        logger.setLevel('INFO')

    logger.info("Running with AWS Cred %s:%s to the %s endpoint, tag %s" %
                (access_key, secret_key, region, tag))

    instances_unsorted = get_ec2_instances(access_key, secret_key, region)

    if len(instances_unsorted) > 0:
        present_ec2_instances(instances_unsorted, attributes_to_print, tag)
    else:
        logger.info("No instances found in %s" % region)

    sys.exit(0)

if __name__ == '__main__':
    main()
