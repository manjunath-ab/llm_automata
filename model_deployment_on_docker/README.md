# Running Local LLM Models on Docker
<div>
    <a href="https://www.loom.com/share/19a628142168414c8d463c102d240a31">
      <p>Running Local LLM models on docker 🦙 - Watch Video</p>
    </a>
    <a href="https://www.loom.com/share/19a628142168414c8d463c102d240a31">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/19a628142168414c8d463c102d240a31-with-play.gif">
    </a>
</div>

This repository guides you through running local LLM (Large Language Models) models using Docker. By following the steps outlined below, you can set up and interact with LLM models on your local machine.

## Prerequisites

- Docker Desktop installed on your system.
- Basic knowledge of Docker commands and terminal usage.

## Getting Started

### Step 1: Download Docker Desktop

If you don't have Docker Desktop installed, download and install it from the [Docker official website](https://www.docker.com/products/docker-desktop/). Follow the installation instructions for your operating system.

### Step 2: Search for the Ollama Image

Open your terminal or command prompt and search for the Ollama image on Docker Hub:

```sh
docker search ollama/ollama
```
### Step 3: Pull the Ollama Image
Once you have identified the correct image, pull it using the following command:

```sh
docker pull ollama/ollama
```

### Step 4: Run the Ollama Image
After pulling the image, run a container from the image:


```sh

docker run -it ollama/ollama
```
### Step 5: Access the Container Terminal
To interact with the container, you need to access its terminal or use the exec command. Open a new terminal and run:

```sh
docker exec -it <container_id> /bin/bash
```
Replace <container_id> with the actual container ID or name.

### Step 6: Download the LLM Models
Inside the container terminal, you can download the desired LLM models using the following command:

```sh
ollama pull <model_name>
```
Replace <model_name> with the name of the model you wish to download.

## Running the Models
### Step 1: Run the Model
To run the downloaded model, use the following command inside the container terminal:

```sh
ollama run <model_name>
```
This will open an interface for you to interact with the model through dialogue.

### Step 2: Making API Calls
You can also make API calls to the models using the curl commandas showm in this demo below

https://www.loom.com/share/19a628142168414c8d463c102d240a31?sid=37efbc43-082f-461a-8149-c8ebe595f03d
