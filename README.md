This project aims to use a LLM to answer questions related to documents provided by the user. This project is made in Python with vLLM, huggingface and pandas.

### LLM
The LLM used is Mistral-7B-Instruct-v0.2-GPTQ, which is a model trained on the Instruct dataset. 
The model is available on [huggingface](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GPTQ). 

This is a custom version of the Mistral-7B-Instruct-v0.2 that is lighter than the original one, allowing it to be used in less powerful machines.

### Hardware
The project as been tested on an instance EC2 of AWS. 
The instance used was a [g4dn.2xlarge](https://aws.amazon.com/ec2/instance-types/g4/). 
It has 8 vCPUs, 32 GiB of memory, 1 x 150 GB of storage and a GPU NVIDIA T4 with 15 VRAM.

The AMI used was the [Deep Learning OSS Nvidia Driver AMI GPU Pytorch 2.6 Amazon Linux 2023](https://aws.amazon.com/releasenotes/aws-deep-learning-ami-gpu-pytorch-2-6-amazon-linux-2023/).