
# Finetuning the LLAMA3.1 Model using Unsloth

This repository provides a step-by-step guide to fine-tuning the LLAMA3.1 model using the Unsloth library. The dataset for fine-tuning is generated with `dataset_gen_for_fine_tuning.ipynb` and contains 1000 document splits. The fine-tuned model will be uploaded to Hugging Face Hub.

Here is the link to the fine trained model:https://huggingface.co/abhi1006/snowflake_lora_model



![image](https://github.com/user-attachments/assets/500b29ed-d0ff-4f2a-be88-c5d52c08a575)


## Table of Contents

- [Prerequisites](#prerequisites)
- [Generating the Dataset](#generating-the-dataset)
- [Uploading the Dataset to Hugging Face](#uploading-the-dataset-to-hugging-face)
- [Fine-Tuning the Model](#fine-tuning-the-model)
- [Uploading the Fine-Tuned Model](#uploading-the-fine-tuned-model)


## Prerequisites

Before starting, ensure you have the following installed:

- Python 3.8+
- Jupyter Notebook
- Unsloth library
- Hugging Face `datasets` and `transformers` libraries
- Access to a Hugging Face account and an access token

## Generating the Dataset

1. Open the `dataset_gen_for_fine_tuning.ipynb` notebook.
2. Run the cells to generate the dataset. This notebook uses the LLAMA3 model to create instructions for document splits.
3. The output will be a CSV file containing 1000 document splits.

## Uploading the Dataset to Hugging Face

1. Create a new dataset repository on Hugging Face.
2. Upload the generated CSV file to the repository.

## Fine-Tuning the Model

1. Clone the fine-tuning notebook from this repository.
2. Replace the dataset link in the notebook with the link to your uploaded dataset on Hugging Face.
3. Run the notebook to fine-tune the LLAMA3.1 model using Unsloth.

## Uploading the Fine-Tuned Model

1. Once fine-tuning is complete, save the model locally.
2. Use your Hugging Face access token to authenticate and upload the model to your Hugging Face Hub.

