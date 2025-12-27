import boto3
import json
import argparse
import botocore
import logging
import sys

class AwsResource:
    """Handles fetching EC2 instances and S3 buckets from AWS."""

    def __init__(self, region, output_file):
        self.ec2 = self.get_connection("ec2", region)
        self.s3 = self.get_connection("s3", region)
        self.data = {"Instances": [], "Buckets": []}
        self.output_file = output_file

    def get_connection(self, client_type, region):
        try:
            return boto3.client(client_type, region_name = region)
        except Exception as e:
            logging.error(f"{client_type} Error: {e}")
            sys.exit()

    def show_report(self):
        self.show_buckets()
        self.show_instances()
        self.print_data()
        self.write_data()

    def show_buckets(self):
        try:
            response = self.s3.list_buckets()
            for bucket in response['Buckets']:
                self.data['Buckets'].append({"name":bucket['Name']})
        except botocore.exceptions.ClientError as e:
            logging.error(f"s3 Error: {e}")

    def show_instances(self):
        try:
            paginator = self.ec2.get_paginator("describe_instances")
            for page in paginator.paginate():
                for reservation in page["Reservations"]:
                    for instance in reservation["Instances"]:
                        instance_id = instance["InstanceId"]
                        name = "N/A"
                        for tag in instance.get("Tags", []):
                            if tag["Key"] == "Name":
                                name = tag["Value"]
                        self.data['Instances'].append({"id": instance_id, "name" : name})
        except botocore.exceptions.ClientError as e:
            logging.error(f"ec2 Error: {e}")

    def print_data(self):
        for section, values in self.data.items():
            print(f"\n{section}:")
            if not values:
                print("None found")
            else:
                for items in values:
                    for key, value in items.items():
                        print(f"{key} : {value}", end="    ")
                    print()

    def write_data(self):
        with open(self.output_file, "w") as file:
            json.dump(self.data, file, indent=4)

def main():
    parser = argparse.ArgumentParser(description="AWS report script")
    parser.add_argument("--region", default="ap-south-1", help="AWS region")
    parser.add_argument("--out", default="aws_report.json", help="Output JSON file")
    args = parser.parse_args()

    aws = AwsResource(args.region, args.out)
    aws.show_report()

if __name__ == "__main__":
    main()