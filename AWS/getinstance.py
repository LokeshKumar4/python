import boto3
import contactkeys


ec2=boto3.client('ec2',
			'us-east-1',
			aws_access_key_id=contactkeys.vals["access_key"],
			aws_secret_access_key=contactkeys.vals["secret_access_key"])

all_ec2_instances=ec2.describe_instances()
for reservation in all_ec2_instances["Reservations"]:
    for instance in reservation["Instances"]:
        print("Instance Id : {}".format(instance["InstanceId"]))
        print("Instance Type : {}".format(instance["InstanceType"]))
        print("Launch Time : {}".format(instance["LaunchTime"]))
        