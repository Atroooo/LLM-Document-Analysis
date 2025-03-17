This project aims to use a LLM to answer questions related to documents provided by the user. This project is made in Python with vLLM, huggingface and pandas.

### LLM
The LLM used is Mistral-7B-Instruct-v0.2-GPTQ, which is a model trained on the Instruct dataset. 
The model is available on [huggingface](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GPTQ). 

This is a custom version of the Mistral-7B-Instruct-v0.2 that is lighter than the original one, allowing it to be used in less powerful machines.

### Hardware
The project as been tested on an instance EC2 of AWS. 
The instance used was a [g4dn.2xlarge](https://aws.amazon.com/ec2/instance-types/g4/). 
It has 8 vCPUs, 32 Go of memory, 1 x 150 GB of storage and a GPU NVIDIA T4 with 15Go VRAM.

The AMI used was the [Deep Learning OSS Nvidia Driver AMI GPU Pytorch 2.6 Amazon Linux 2023](https://aws.amazon.com/releasenotes/aws-deep-learning-ami-gpu-pytorch-2-6-amazon-linux-2023/).

### Installation
To install the project, you need to clone the repository and install the requirements. 
```bash
git clone https://github.com/Atroooo/LLM-Document-Analysis.git
cd LLM-Document-Analysis
```
    
Then, you can install the requirements with the following command:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Usage
To use the project, you can run the following command: 
```bash
python main.py help
```

There is 2 possibilities for providing the documents to the model:
- You can put all the documents in the documents/ folder and run the following command:
```bash
python main.py
```
- You can provide the path to the documents with the following command:
```bash
python main.py documents ...
```

You can also turn on the logging with the following command:
```bash
python main.py 1 documents ...
```

Recap of the possible commands:
```bash
python main.py help # Display the help
python main.py # Run the model with the documents in the documents/ folder
python main.py 1 # Run the model with the documents in the documents/ folder and turn on the logging
python main.py documents ... # Run the model with the documents provided
python main.py 1 documents ... # Run the model with the documents provided and turn on the logging
```