import boto3

def show_buckets():
    s3 = boto3.client("s3", region_name = "ap-south-1")
    response = s3.list_buckets()
    s3_data = {"Buckets": []}
    for bucket in response['Buckets']:
        s3_data['Buckets'].append({"name":bucket['Name']})
    return s3_data

def show_instances():
    ec2 = boto3.client("ec2", region_name = "ap-south-1")
    ec2_data = {"Instances": []}
    paginator = ec2.get_paginator("describe_instances")
    for page in paginator.paginate():
        for reservation in page["Reservations"]:
            for instance in reservation["Instances"]:
                instance_id = instance["InstanceId"]
                name = "N/A"
                for tag in instance.get("Tags", []):
                    if tag["Key"] == "Name":
                        name = tag["Value"]
                ec2_data['Instances'].append({"id": instance_id, "name" : name})
    return ec2_data