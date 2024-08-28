**Table of Contents**

- [Workshop Sign-In (Optional but Encouraged)](#workshop-sign-in-optional-but-encouraged)
- [Cloning the HNN-Data Repository](#cloning-the-hnn-data-repository)
- [Preferred Installation Method: Google CoLab](#preferred-installation-method-google-colab)
- [Alternative Installation Methods](#alternative-installation-methods)
  - [Oscar On Demand (OOD) Virtual Desktop](#oscar-on-demand-ood-virtual-desktop)
    - [Logging in to OOD](#logging-in-to-ood)
    - [Launching the Desktop App on Oscar](#launching-the-desktop-app-on-oscar)
    - [Launching HNN-Core GUI via Oscar](#launching-hnn-core-gui-via-oscar)
    - [Launching HNN-Core (Python) via Oscar](#launching-hnn-core-python-via-oscar)
  - [Installing HNN-Core GUI on Your Local Machine without Conda](#installing-hnn-core-gui-on-your-local-machine-without-conda)
  - [Installing HNN-Core GUI on Your Local Machine via Conda](#installing-hnn-core-gui-on-your-local-machine-via-conda)
    - [Creating a Conda Env and Installing Dependencies](#creating-a-conda-env-and-installing-dependencies)
    - [Installing MPI for Parallel Simulations](#installing-mpi-for-parallel-simulations)
    - [Launch the GUI](#launch-the-gui)

# Workshop Sign-In (Optional but Encouraged)

Please consider 'signing in' to the workshop by providing your institution/location, position, and field of study. This information is used in reporting on milestones for the grants that continue to fund our dissemination and development. We don't ask for name or email, and the form should take no more than 30 seconds to complete.

Click [here](https://forms.gle/YnZX9ZRm8WvWpAGU7) to navigate to our Virtual Sign-In Form.

<p>Thanks for your support. &#128513;</p>


# Cloning the HNN-Data Repository
To follow along with the workshop, you'll need the [hnn-data repository](https://github.com/jonescompneurolab/hnn-data) on your local machine / virtual environment.

You can download the file [here](https://github.com/jonescompneurolab/hnn-data/archive/refs/heads/main.zip) or you can run the following command to clone the repository.

```bash
git clone https://github.com/jonescompneurolab/hnn-data.git
```

If you already cloned the hnn-data repository on your machine, be sure to update it to include the latest changes.

```bash
cd hnn-data
git pull
```

# Preferred Installation Method: Google CoLab

This installation method is the quickest way to get up and running with the HNN-Core GUI, though it does require a Google Account. If you do not have a Google account, you can either create one for free to run the notebook, or try one of the other installation methods listed below.

We have created a Google CoLab notebook that allows you to run the HNN-Core GUI out of your browser, with access to your local filesystem. Click <a href="https://colab.research.google.com/drive/1CvNTB_puonJiVvHmFhKhrr_CjmrfbgVB?usp=sharing">here</a> to open the notebook, which includes instructions on how to get set up.

# Alternative Installation Methods

**Warning**: You may experience considerable lag in navigating the virtual desktop environment if you do not have a strong WiFi connection. If you experience this issue, we encourage you to try one of the other installation methods here to get started.

## Oscar On Demand (OOD) Virtual Desktop

### Logging in to OOD
1. Go to Oscar-on-Demand (OOD): [ood.ccv.brown.edu/pun/sys/dashboard/batch_connect/sessions](https://ood.ccv.brown.edu/pun/sys/dashboard/batch_connect/sessions)

2. Select a username from the <a href="https://docs.google.com/spreadsheets/d/1NQuCULv6Nmo1n7cHnsD5ZnEYtnxPeYUWzRBvaXFvliA/edit?usp=sharing">following spreadsheet</a> and add an "X" to the appropriate cell. The "X" is to indicate that the username you selected is "in use" so another participant doesn't try to log in with the same username/bypass code

3. Enter your selected username into 'Username' field of the login page

4. Enter the password: HNNws2024*

![](imgs/oscar_login.png){ width=400px }


5. <p>From the DUO authentication screen, select "Other options" and then choose "Bypass code"</p>

| ![](imgs/duo_01.png){ width=200px } | ![](imgs/duo_02.png){ width=200px } |
|-----------------------------|-----------------------------|

6. <p>Enter the bypass code associated with the username you selected in Step 2</p>


### Launching the Desktop App on Oscar
1. Choose the "Desktop (Advanced)" application. Note that this is different form the regular "Desktop" app.

2. You will see a form. Enter the following in the fields.

   - Account: [Leave Blank]
   - Desktop Environment: xfce
   - Number of Hours: 3
   - Partition: batch
   - Num Cores: 8
   - Num GPUs: 1 [This number does not matter]
   - Memory (GB): 8
   - Reservation: hnn-workshop
   - Slurm Features: [Leave Blank]

3. Click "Launch" . It may take a minute before the “Launch Desktop” button appears.

### Launching HNN-Core GUI via Oscar
With the Oscar desktop instance open, launch a Terminal via the “Terminal Emulator” at the bottom of the Desktop or via the Applications drop-down at the top-left of the Desktop.

Type the following into the terminal to activate the environment.

```bash
module purge
module load python/3.11
module load  hpcx-mpi/4.1.5rc2
source /oscar/data/ccv_workshop/hnn_env/bin/activate
```

Within the same terminal with the `hnn_env` activated, type the following to launch the GUI.
```bash
hnn-gui
```

### Launching HNN-Core (Python) via Oscar
From the Oscar virtual desktop, open a new terminal and run the following commands.

```bash
module purge
module load python/3.11
module load  hpcx-mpi/4.1.5rc2
source /oscar/data/ccv_workshop/hnn_env/bin/activate

git clone https://github.com/jasmainak/hnn-workshop-materials.git
cd hnn-workshop-materials/
jupyter lab # or `jupyter notebook` alternatively
```

## Installing HNN-Core GUI on Your Local Machine without Conda

You can easily install HNN-Core GUI on your local machine with pip.

To do so, open a Terminal and and enter the following command:

**For bash/Powershell**
```bash
pip install --pre hnn-core[gui]
```

**For zsh**
```bash
pip install --pre hnn-core'[gui]'
```

Once installed, you can launch the GUI with the following command.

```bash
hnn-gui
```

Note that you will not be able to utilize the MPI backend to run simulation in parallel without also installing MPI on your machine. We recommend using the Conda install method below if you would like to utilize MPI, as it significantly streamlines the MPI setup process.

For our workshops, we will be running simulations with only a few trials at most, and so MPI is not strictly necessary to keep up with the materials.



## Installing HNN-Core GUI on Your Local Machine via Conda

### Creating a Conda Env and Installing Dependencies

**Note**: We recommend using use Windows Subsystem for Linux (WSL) to run HNN on Windows machines. Installation instructions can be found <a href="https://learn.microsoft.com/en-us/windows/wsl/install">here</a>

Start by creating a new conda environment. We recommend creating an environment with the fewest number of dependencies to speed up the installation process.

```bash
conda create --name hnn_core_gui python=3.11 --no-default-packages
conda activate hnn_core_gui
pip install --pre hnn-core[gui]
```

### Installing MPI for Parallel Simulations

To run simulations in parallel across multiple cores, which dramatically speeds up siuations, you'll need to set up the MPI backend.

```bash
conda activate hnn_core_gui # activate the environment if needed
conda install -y openmpi mpi4py
pip install psutil
```

Additionally, for MacOS, run the following command.
```bash
export DYLD_FALLBACK_LIBRARY_PATH=${CONDA_PREFIX}/lib
```

More detailedd instructions are available on our <a href="https://jonescompneurolab.github.io/hnn-core/stable/parallel.html">parallel backends</a> page. 

### Launch the GUI

You can now launch the GUI from within your conda environemnt.

```bash
conda activate hnn_core_gui # activate the environment if needed
hnn-gui
```

