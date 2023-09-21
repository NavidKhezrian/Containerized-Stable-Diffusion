
# Use the TensorFlow GPU image as the base image with version 2.10.0
FROM tensorflow/tensorflow:2.10.0-gpu
# Set the working directory inside the container to /user/source
WORKDIR /user/source
#Used to copy your local files/directories to Docker Container.
COPY requirements.txt /user/source
COPY main.py /user/source
# Install Python packages listed in requirements.txt and specify an extra index URL for PyTorch
RUN pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu117

# Define the default command to run when the container is started
CMD ["python", "/user/source/main.py"]
