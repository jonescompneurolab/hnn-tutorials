# Installing HNN docker on macOS (Sonoma 14.4.1)

## Pre-requisites

### 1) GitHub Account

Set up a github account following the instructions on the website. [https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github 
](url)

Once set-up, check if git is installed on your Mac:

1. Open terminal/command line interface (CLI; command + space and type in "terminal")
2. In the terminal, execute ```git version```. If the output looks something this, continue to pre-requisite **2) Docker desktop.**
```
Last login: Mon Apr 22 11:17:56 on ttys000
(base) katharinaduecker@Katharinas-MacBook-Pro ~ % git version
git version 2.44.0

```
3. If git is an unknown command, install the latest version of git. If you have python and homebrew installed on your mac, run the following command in the terminal. *
```
brew install git
```
If homebrew is not installed on your mac, run
```pip install brew``` first.


Alternatively, you can follow the instructions here to download the most recent installer
[https://github.com/git-guides/install-git
](url)

4. Set your github username and email adress, be executing
```
git config --global user.name "YOUR USERNAME"
git config --global user.email "YOUR EMAIL"
```

5. Repeat step 1. and 2. to double-check if git is installed correctly. 

For more helpful tips and suggestions on how to set up git, see: [https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](url)

### 2) Docker desktop

Simply follow the instructions on the website to install Docker desktop. [https://www.docker.com/products/docker-desktop/](url)

You don't need to create an account.

### 3) Xquartz

Download the installer from [https://www.xquartz.org/](url)

Once downloaded, open up Settings > Security, and press the checkmark for “Allow connections from network clients” to allow connection for the HNN-GUI.

## Cloning the HNN repository

1. Open the terminal/CLI (command + space and type "terminal") if you haven't already.
2. Navigate to the directory where you want to clone the repository using  ```cd "directory"```
3. Execute ``` git clone https://github.com/jonescompneurolab/hnn ```

## Start HNN-GUI
Once you have completed all of the above, you will only need execute the following steps everytime you want to start the HNN-GUI.
- Make sure Docker desktop is runinng
[perhaps insert docker screenshot here]
- Open the terminal/CLI if you haven't already.
- Navigate to the folder where you have cloned the HNN repository
- Enter the HNN folder using ```cd hnn```
- Start the GUI using ```./hnn_docker.sh start```

[insert screenshot HNN]

**Troubleshooting**
If you receive an error, try running ```./hnn_docker.sh uninstall``` first before running ```./hnn_docker.sh start```
(This could happen if you're trying to run an old version of HNN).