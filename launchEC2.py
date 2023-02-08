import boto3
import contactkeys


ec2=boto3.client('ec2',
			'us-east-1',
			aws_access_key_id=contactkeys.vals["access_key"],
			aws_secret_access_key=contactkeys.vals["secret_access_key"])

conn=ec2.run_instances(
                InstanceType="t2.micro",
			    MaxCount=1,	
			    MinCount=1,
			    ImageId="ami-0aa7d40eeae50c9a9")

conn
print(" Virtual machine created Successfully ")



