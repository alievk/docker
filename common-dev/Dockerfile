FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive

# Install SSH server and other dependencies
RUN apt-get update && apt-get install -y \
    openssh-server \
    python3 \
    python3-pip \
    && mkdir /var/run/sshd

# Create a non-root user with the same UID and GID as the host user
ARG USER_ID=1000
ARG GROUP_ID=1000
RUN groupadd -g ${GROUP_ID} user && \
    useradd -m -u ${USER_ID} -g user -s /bin/bash user

# Set up SSH configuration
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

# Copy public key for SSH
RUN mkdir /home/user/.ssh
COPY id_rsa.pub /home/user/.ssh/authorized_keys
RUN chmod 700 /home/user/.ssh && chmod 600 /home/user/.ssh/authorized_keys

# Install JupyterLab
RUN pip3 install jupyterlab

# Set up Jupyter configuration for the new user
RUN mkdir -p /home/user/.jupyter
COPY jupyter_lab_config.py /home/user/.jupyter/

# Create Trash directory and set permissions
RUN mkdir -p /home/user/.local/share/Trash
RUN chown -R user:user /home/user

# Copy start script and make it executable for the new user
COPY start.sh /root/start.sh
RUN chmod +x /root/start.sh

# Expose necessary ports
EXPOSE 22
EXPOSE 8555

# Start bash shell by default
CMD ["/bin/bash", "/root/start.sh"]