import boto3
import contactkey


ec2=boto3.client('ec2',
			'us-east-1',
			aws_access_key_id=contactkey.vals["access_key"],
			aws_secret_access_key=contactkey.vals["secret_access_key"])

instances=["i-0fb9e279202d847f4"]

#ec2.stop_instances(InstanceIds=instances)
#ec2.start_instances(InstanceIds=instances)
ec2.terminate_instances(InstanceIds=instances)
