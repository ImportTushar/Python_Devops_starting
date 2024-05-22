import boto3
import csv

ec2_cli = boto3.client(service_name='ec2')
print(ec2_cli = boto3.describe_regions())
