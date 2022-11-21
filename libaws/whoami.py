import boto3

def whoami():
    sts = boto3.client('sts')
    print(sts.get_caller_identity())
