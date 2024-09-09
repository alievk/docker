# Common Docker for development

I hate root files popping up here and there after working in a development Docker container. That's why I created this Docker environment. It has the following features:
- Inherits the host user as `user` (forget about the `root`)
- Essential Python libs installed, like `torch` and `numpy`
- Properly installed Node.js for web development
- You can ssh into the container from a remote computer, like `ssh -p 2222 user@host_address`
- GPU, CPU and RAM limit control
- Deploys a Jupyter Lab (`https://host_address:8500`)
- Inherits Cursor settings

Build & run
```bash
USER_ID=$(id -u) GROUP_ID=$(id -g) docker-compose up -d --build
```
