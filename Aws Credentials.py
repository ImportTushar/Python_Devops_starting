import boto3

def list_ec2_instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    instances = response['Reservations']
    ec2_inventory = []

    for reservation in instances:
        for instance in reservation['Instances']:
            ec2_inventory.append({
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name'],
                'LaunchTime': instance['LaunchTime'],
                'PublicIpAddress': instance.get('PublicIpAddress'),
                'PrivateIpAddress': instance.get('PrivateIpAddress'),
            })
    return ec2_inventory

def list_s3_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    buckets = response['Buckets']
    s3_inventory = [{'Name': bucket['Name'], 'CreationDate': bucket['CreationDate']} for bucket in buckets]
    return s3_inventory

def list_rds_instances():
    rds = boto3.client('rds')
    response = rds.describe_db_instances()
    instances = response['DBInstances']
    rds_inventory = []

    for instance in instances:
        rds_inventory.append({
            'DBInstanceIdentifier': instance['DBInstanceIdentifier'],
            'DBInstanceClass': instance['DBInstanceClass'],
            'Engine': instance['Engine'],
            'DBInstanceStatus': instance['DBInstanceStatus'],
            'Endpoint': instance['Endpoint']['Address'],
            'AllocatedStorage': instance['AllocatedStorage'],
            'InstanceCreateTime': instance['InstanceCreateTime'],
        })
    return rds_inventory

if __name__ == "__main__":
    print("EC2 Instances:")
    ec2_instances = list_ec2_instances()
    for instance in ec2_instances:
        print(instance)

    print("\nS3 Buckets:")
    s3_buckets = list_s3_buckets()
    for bucket in s3_buckets:
        print(bucket)

    print("\nRDS Instances:")
    rds_instances = list_rds_instances()
    for instance in rds_instances:
        print(instance)