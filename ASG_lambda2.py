import json
import boto3

def lambda_handler():

    client = boto3.client('autoscaling')
    describe_asg = client.describe_auto_scaling_groups()    

    all_asg = describe_asg['AutoScalingGroups']

    with_tags = []
    without_tags = []

    for i in range(len(all_asg)):
        all_tags = all_asg[i]['Tags']
        keylist = []
        for j in range(len(all_tags)):
            # print(all_asg[i]['AutoScalingGroupName'],all_tags[j]['Key'])
            keylist.append(all_tags[j]['Key'])

        if 'owner' in keylist and 'purpose' in keylist:
            with_tags.append(all_asg[i]['AutoScalingGroupName'])    

        else :
            without_tags.append(all_asg[i]['AutoScalingGroupName'])    

    for name in without_tags:
        delete_asg = client.delete_auto_scaling_group(AutoScalingGroupName=name)

    return delete_asg    

if __name__ == '__main__':
    lambda_handler()


# name = 'pratyush'

# delete_asg = client.delete_auto_scaling_group(AutoScalingGroupName=name)

# print(delete_asg)
# print(with_tags)
# print(without_tags)




