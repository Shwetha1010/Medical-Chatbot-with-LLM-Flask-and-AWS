# Medical-Chatbot-with-LLM-Flask-and-AWS

''' bash

 conda create -n medibot python=3.11.0 -y
'''

'''bash

conda activate medibot
'''

## AWS-CICD-Deployment-with-Github-Actions

# 1.Login to AWS console

# 2.Create IAM user for deployment

#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
