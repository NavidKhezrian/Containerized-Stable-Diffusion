# Containerized Stable-Diffusion on FAU's High-Performance Computing (HPC) System

Welcome to the "Containerized Stable-Diffusion" repository, your comprehensive guide to running the Stable-Diffusion algorithm on FAU's High-Performance Computing (HPC) system. This repository includes essential files and instructions to facilitate a seamless experience:

## Repository Files

1. **Dockerfile**: Contains the instructions to build a Docker container for running the Stable-Diffusion algorithm. Docker serves as one of the containerization methods.

2. **jobfile.sh**: A script designed for executing a Singularity container on the HPC system. It handles resource requests and commands to run the Singularity container.

3. **main.py**: Your primary Python script for executing the Stable-Diffusion algorithm. This is the core of your application.

4. **requirements.txt**: Lists the Python dependencies necessary for your application to function correctly.

5. **singularity.def**: A Singularity definition file used to create a Singularity container for running the Stable-Diffusion algorithm. Singularity is the recommended containerization method for execution within the HPC environment.

## Getting Started

To run the Stable-Diffusion algorithm on the FAU HPC system using this repository, follow these general steps:

### 1. Select the Containerization Method

You have two approaches to choose from:

- **Method A**: Directly create a Singularity image.
- **Method B**: First, create a Docker image and then convert it to a Singularity image.

### 2. Create the Container Image

- **Direct Singularity Image Creation (Method A)**:

  Use the provided `singularity.def` file to build a Singularity image directly with the following command:

  ```bash
  sudo singularity build my_container.sif singularity.def
  ```

- **Create Docker Image and Convert to Singularity (Method B)**:

  Follow these steps to create a Docker image and then convert it into a Singularity image:

  1. Build the Docker image:

     ```bash
     sudo docker build -t my_container .
     ```

  2. Convert the Docker image to a Singularity image:

     ```bash
     sudo docker run -v /var/run/docker.sock:/var/run/docker.sock -v /tmp/test:/output --privileged -t --rm quay.io/singularity/docker2singularity my_container
     ```

### 3. Resource Request in HPC System

When running your Singularity container on the FAU HPC system, ensure you request the necessary resources appropriately. There are two primary methods to do this:

- **Interactive Job (Method A)**:

  In this method, request the required resources with the following command:

  ```bash
  salloc --gres=gpu:a100:1 --partition=a100 --time=01:00:00
  ```

  This allocates the specified GPU resources for one hour. After obtaining the allocated resources, you can run the Singularity container using a command similar to the following:

  ```bash
  singularity run --bind /home/vault/b116ba/b116ba17/workshop/output:/user/source/output \
  --bind /home/vault/b116ba/b116ba17/workshop/stable-diffusion-v1-5:/user/source \
  /stable-diffusion-v1-5 workshop.sif --prompt "Iron Man, (Arnold Tsang, Toru Nakayama), Masterpiece, Studio Quality, 6k , toa, toaair, 1boy, glowing, axe, mecha, science_fiction, solo, weapon , jungle , green_background, nature, outdoors, solo, tree, weapon, mask, dynamic lighting, detailed shading, digital texture painting"
  ```

  Customize the paths and commands to suit your specific job requirements.

- **Jobfile (Method B)**:

  In this method, you specify the required resources and the command to run the Singularity container within a `jobfile.sh`. You can then run this file with the following command:

  ```bash
  srun jobfile.sh
  ```

  This approach is suitable for batch processing and encapsulates resource requests and job execution in a script.
