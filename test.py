ec2_instances_info = [
    {
    "id": "instance-001",
    "type": "t2.micro"
},
{
   "id": "instance-002",
    "type": "t2.medium"
},
{
    "id": "instance-003",
    "type": "t2.large"
},
{
    "id": "instance-004",
    "type": "t2.x-large"
}]

print(ec2_instances_info[0]["id"], ec2_instances_info[1]["type"])

