# ELEC 442 QArm Lab Software Installation for Student Computers

**Last updated:** September 25, 2026  

> This guide is for a **personal computer**. The first part takes you through core components which all students will need. The second part will setup Quanser and virtual arm components which only windows computers will be able to use. Lab computers have already been configured.

> This guide assumes you are familiar with Python code, but does not assume that you are familiar with installing Python, the VS Code IDE, or using Git.

# For all students
These are core software components that you will need for this class. Lab 0 will give you a chance to install, then test these to ensure you are prepared for the upcoming labs.

## 1. Install Git

Git is a free and open source distributed version control system that you will be using to download lab material and upload work to share with teammates, instructors, and TAs.

1. Download [Git](https://git-scm.com/install/windows) and install.

2. Take a glance at the [Git Cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf) while your software installs if unfamiliar with Git.

## 2. Clone the Quanser Academic Resources repository

The install location is up to you. However, Quanser recommends downloading their resources in a `C:/Users/user/Documents/Quanser` folder.

1. Open the Windows Start menu.

2. Search for **PowerShell** and open it. Administrator privileges are not required.

3. Go to your Documents folder:

   ```text
   cd ~/Documents
   ```

   `cd` (change directory) changes the folder the terminal is working in. `~` is your home directory.

   Hit `Tab` while typing to autocomplete.

4. Clone the repository:

   ```text
   git clone https://github.com/quanser/Quanser_Academic_Resources.git Quanser
   ```

   `git clone` downloads the repository and its history into a new folder.

## 3. Install Python

> Do not use Python downloaded from the Microsoft Store. If you have it, it is recommended you uninstall it first. Do not use the Python Installation Manager.

If you already have Python, Quanser supports versions 3.11 to 3.14. Otherwise we recommend Python 3.13.

1. Download [Python 3.13.11](https://www.python.org/ftp/python/3.13.11/python-3.13.11-amd64.exe).

2. Install. When prompted, select the *Add Python to PATH* option in the first menu of the installer.

### Set up Python Libraries

The only key library required to be installed for all users is numpy:
+ Open a terminal instance anywhere
+ run: `pip install numpy`

## 4. Install Visual Studio Code

You can use any local IDE you like, but we recommend VS Code. Cloud-based code editors will not work.

1. Download [Visual Studio Code](https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user) and install.

# Windows Computers Only
> This guide is an adapation of Quanser's own [PC setup guide](https://github.com/quanser/Quanser_Academic_Resources/blob/dev-windows/docs/pc_setup.md). This version is intended to be more streamlined for ELEC 442. It also includes the cloning of `lab-machine-env`, a custom respository that supporst this course's labs. If you intend to use MATLAB or connect to the QArm hardware, follow their guide first.

The following sections take you through installing tools used to run the virtual QArm. Unfortunately, this is only possible on a windows machine. While it will be a useful tool and is strongly recommended, it is not necessary for any exercises outside the labs. Inside the labs, one windows laptop per QArm will be provided.

## 5. Install Quanser SDK and Quanser Interactive Labs

Note that the installation of the Quanser SDK and Quanser Interactive Labs are only for computers without QUARC and without use of MATLAB, respectively. If you require MATLAB support and/or control of the QArm hardware, please see Quanser's [PC setup guide](https://github.com/quanser/Quanser_Academic_Resources/blob/dev-windows/docs/pc_setup.md). For users using only the virtual arm with only python:

1. Download the [Quanser SDK](https://github.com/quanser/quanser_sdk_win64/releases/download/v26.0.5256/install_quanser_sdk.exe) and install. 

2. Download [Quanser Interactive Labs](https://download.quanser.com/qlabs/latest/Install%20QLabs.exe) and install.

3. Create a Quanser account using your UBC email through their [portal](https://portal.quanser.com/Accounts/Register).

4. Open Quanser Interactive Labs and log in. The next step will be to select QArm. However, you won't be able to complete this step until you are added to the course by an instructor or TA.

## 6. Clone the `lab-machine-env` repository

This repository contains read-only code that suppports Lab 1 and Lab 2. The install location is, again, up to you. However, we recommend cloning to the same parent folder as your labs. Specifically, your documents folder `C:/Users/user/Documents`.

1. Open **PowerShell** again, or a **VS Code terminal** from VS Code with   `` CTRL + ` ``!

2. Go to your Documents folder:

   ```text
   cd ~/Documents
   ```

   `cd` (change directory) changes the folder the terminal is working in. `~` is your home directory.

   Hit `Tab` while typing to autocomplete.

3. Clone the repository:

   ```text
   git clone https://github.com/UBC-ELEC-442-Labs-2026/lab-machine-env
   ```

   `git clone` downloads the repository and its history into a new folder.

4. Keep your terminal open for **Section 7**.

## 7. Configure the Lab Environment Path

This script tells Windows where your local `lab-machine-env` repository is stored by setting the `QARM_LAB_ENV` environment variable. The lab code (`constants.py`) uses that variable to locate shared course files without hard-coding a path specific to your computer.

1. Using your terminal from **Section 6**, which is still working in the parent folder of `lab-machine-env`, navigate into the `lab-machine-env` folder:

   ```text
   cd lab-machine-env
   ```

   You can type `ls` to list the contents of the directory.

2. Run the script:

   ```text
   setup_personal_computer.bat
   ```

3. If VS Code was open, close it for changes to take effect.


## 8. Completing the Installation

You're almost there!

1. Restart your computer if you've installed any new software.

2. Using your terminal, navigate to the Quanser setup folder:

    ```text
    cd ~/Documents/Quanser/1_setup
    ```

    Hit `Tab` while typing to autocomplete.

3. Check that you've successfully met the requirements by running:

    ```text
    step_1_check_requirements.bat
    ```
4. If everything looks good, complete the software setup with:
    ```text
    configure_python.bat
    ```
5. Restart your computer one more time.

Note: This guide follows Quanser’s default setup and installs the required Python packages into your global Python installation. If you prefer to use a virtual environment, you will need to install the same Quanser packages and requirements into that environment instead; the provided `configure_python.bat` is not configured to do this automatically.

## 9. Next Step: Configure Software Setup

Congrats! That's all the software you needed to install. Navigate to [personal computer setup](#personal-computer-setup.md) to continue the setup.
