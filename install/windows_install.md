## Prerequisites for Windows

- Github Account

- Docker, recommended docker desktop https://www.docker.com/products/docker-desktop/
    No need to create an account

- Visual Studio Code (recommended to run WSL)

- WSL (Windows Subsystem for Linux) https://learn.microsoft.com/en-us/windows/wsl/install

    Open PowerShell or Windows Command Prompt in administrator mode by right clicking and selecting “Run as administrator”, then run the command “wsl —install”

- VcXsrv (x-server for Windows)
    https://sourceforge.net/projects/vcxsrv/

- Once downloaded, need to configure to allow connections https://sourceforge.net/p/vcxsrv/wiki/VcXsrv%20%26%20Win10/
    
    Just follow instructions under step 1 to create magiccookie key inside the .Xauthority file


## Windows Installation Process

### Part 1

1) Open command Prompt

2) Run the following command to install Windows Subsystem for Linux (WSL)

        wsl --install

![alt text](image.png)


### Starting up HNN application for Windows
- Make sure, you have Docker up and running. Recommend installing Docker through the Docker Desktop so you can an interface to check that it is running.

- Install required packages including VcXsrv and WSL
    Follow original instructions to set up VcXsv server (disable access control step)

- Make sure to follow additional instructions to create maggiccookie key inside .Xauthority file.

- Navigate to hnn folder, and run ./hnn_docker.sh start to start the script, which should start up the GUI


### TO-DO make these more clear:
A couple of notes here:

- Weirdly "~/.Xauthority" "\${userprofile}/." did not work for me - I had to specify the path to .Xauthority directly (cp "/home/dylansdaniels/.Xauthority" "\${userprofile}/.")
The first time I did this, I mis-specified the IP address, missing the ":0" at the end of "DISPLAY=NN.NN.NN.NN:0" in part 3 -> we might want to highlight that more, as I feel like it's an easy thing to miss
the instructions in update-pre-hnn-core reference the configure_vcxsrv.sh file. However, the instructions also have you clone / work from the master branch, which doesn't have that file so far as I can tell?

