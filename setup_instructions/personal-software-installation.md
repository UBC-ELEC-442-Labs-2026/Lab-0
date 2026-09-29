# ELEC 442 QArm Lab Software Installation for Student Computers

**Last updated:** September 28, 2026

> This guide is for a **personal computer**. Complete the basic setup first, then the optional Windows setup if you want to use the virtual QArm on your own computer. Lab computers have already been configured.

> This guide assumes you are familiar with Python code, but does not assume that you are familiar with installing Python, the VS Code IDE, or using Git.

## Choose your setup

| Setup                                              | Steps to complete                 |
| -------------------------------------------------- | --------------------------------- |
| Virtual QArm on Windows (recommended if available) | All steps, in order               |
| Basic Python work (Windows, macOS, or Linux)       | Steps 1, 3 (inc. NumPy), 4, and 9 |

The virtual QArm setup is optional for work outside the labs. A preconfigured Windows laptop will be provided for each QArm during the in-person labs.

### Before you start

- Use **PowerShell** on Windows or **Terminal** on macOS/Linux. The `.bat` commands in this guide are Windows-only.
- Type commands into the terminal, not the Python `>>>` prompt. Run each command separately and check for errors before continuing.
- `~` means your home folder, `cd` changes the current folder, and `Tab` can autocomplete paths. Put paths containing spaces in quotes.
- The Windows Quanser setup below uses `~/Documents/Quanser` (usually `C:/Users/<your-user-name>/Documents/Quanser`). Use this exact location: the supplied `configure_python.bat` sets library paths to it. A redirected OneDrive Documents folder is not necessarily the same location.

## 1. Install Git

Git is a free and open source distributed version control system that you will be using to download lab material and upload work to share with teammates, instructors, and TAs.

1. Download and install [Git for Windows](https://git-scm.com/install/windows), or follow the [Git installation instructions for macOS/Linux](https://git-scm.com/install/).

2. Open a new terminal and run `git --version`. A version number confirms that Git is available.

3. Take a glance at the [Git Cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf) if you are unfamiliar with Git.

## 2. Clone the Quanser Academic Resources repository

**Windows virtual QArm setup only.** Skip to Step 3 if you only need the basic Python setup. This repository contains Quanser libraries and setup scripts; it is separate from the repositories where you will write your lab code.

1. Open the Windows Start menu.

2. Search for **PowerShell** and open it. Administrator privileges are not required.

3. Go to the Documents folder under your home directory (create it first if it does not exist):

   ```text
   cd ~/Documents
   ```

   `cd` (change directory) changes the folder the terminal is working in. `~` is your home directory.

   Hit `Tab` while typing to autocomplete.

4. Clone the repository:

   ```text
   git clone https://github.com/quanser/Quanser_Academic_Resources.git Quanser
   ```

   `git clone` downloads the repository and its history into a new folder named `Quanser`. If you already cloned it there, use the existing copy instead of cloning it again.

## 3. Install Python

> Do not use Python downloaded from the Microsoft Store. If you have it, it is recommended you uninstall it first. Do not use the Python Installation Manager.

For the Windows Quanser setup, [Quanser supports Python 3.11 to 3.14](https://github.com/quanser/Quanser_Academic_Resources/blob/dev-windows/docs/pc_setup.md). This guide uses Python 3.13; the Windows installer below is the version linked by Quanser.

1. Download [Python 3.13.11](https://www.python.org/ftp/python/3.13.11/python-3.13.11-amd64.exe) for Windows.

   On macOS, use the [Python 3.13.11 release page](https://www.python.org/downloads/release/python-31311/) and choose the macOS installer. On Linux, use your distribution's Python 3 installation instructions.

2. Install. When prompted, select the _Add Python to PATH_ option in the first menu of the installer.

   The **Add Python to PATH** option applies to Windows. Keep the Python launcher selected as well: Quanser's scripts use the `py` command.

3. Open a new terminal and check the installation with `py -3.13 --version` on Windows, or `python3 --version` on macOS/Linux. If you are using another supported Windows version, substitute that version for `3.13`.

### Install NumPy if you are skipping the virtual QArm setup

NumPy is required for the basic Python exercises. If you will complete Step 8, skip this subsection because that step installs it for you.

On Windows, run:

```powershell
py -3.13 -m pip install numpy
```

On macOS/Linux, run:

```sh
python3 -m pip install numpy
```

If your Python installation reports an **externally managed environment**, create an environment for the basic exercises and install NumPy there:

```sh
python3 -m venv ~/elec442-venv
source ~/elec442-venv/bin/activate
python -m pip install numpy
```

Select that environment in VS Code when you reach the next guide. If `venv` is unavailable, install your distribution's Python `venv` package first.

## 4. Install Visual Studio Code

You can use any local IDE you like, but we recommend VS Code. Cloud-based code editors will not work.

1. Download [Visual Studio Code](https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user) for Windows and install.

   On macOS/Linux, download [Visual Studio Code](https://code.visualstudio.com/download) and install the version for your operating system.

## 5. Install Quanser SDK and Quanser Interactive Labs

These steps adapt [Quanser's PC setup guide](https://github.com/quanser/Quanser_Academic_Resources/blob/dev-windows/docs/pc_setup.md) for **Python with the virtual QArm**. They also install the course's shared `lab-machine-env` code.

1. Download the [Quanser SDK](https://github.com/quanser/quanser_sdk_win64/releases/download/v26.0.5256/install_quanser_sdk.exe) and install.

2. Download [Quanser Interactive Labs](https://download.quanser.com/qlabs/latest/Install%20QLabs.exe) and install.

3. Create a Quanser account using your UBC email through their [Quanser Academic Portal at https://portal.quanser.com](https://portal.quanser.com/Accounts/Register).

4. Open Quanser Interactive Labs and log in. Select QArm. If QArm is not available yet, contact a TA; you can still complete the remaining installation steps.

## 6. Clone the `lab-machine-env` repository

This repository lab-machine-env contains shared support code for all Labs. Treat it as read-only; write your solutions in your own lab repository. Clone it alongside `Quanser`, not inside it:

1. Open **PowerShell**, or choose **Terminal > New Terminal** in VS Code.

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
   .\setup_personal_computer.bat
   ```

   In PowerShell, `.\` means "run the script in the current folder."

3. Check that the script prints `QARM_LAB_ENV was configured successfully.` Close **all VS Code windows and terminals**, then reopen PowerShell so it can see the new variable.

4. Verify the saved path:

   ```powershell
   $env:QARM_LAB_ENV
   Test-Path "$env:QARM_LAB_ENV/QArm-control/QArm_functions.py"
   Test-Path "$env:QARM_LAB_ENV/Lab-1/QArm_traj_controllers.py"
   ```

   The first command should print your `lab-machine-env` folder; both checks should print `True`. You do not need to edit `constants.py`. If you move the repository later, rerun the setup script from its new location and reopen VS Code and your terminals.

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
   .\step_1_check_requirements.bat
   ```

4. Read the results in the terminal or `software_requirements.log`. For this setup, Python, Quanser SDK (or QUARC), and QLabs must be detected; MATLAB is not required. Note the detected Python version: you will select that same version in VS Code. If several supported versions are installed, the checker selects the highest supported version it finds.

5. Once those requirements are detected, run the configuration script **from the same `1_setup` folder**:

   ```text
   .\configure_python.bat
   ```

6. Check the output for installation errors. If packages failed to install, resolve the reported error before continuing. Restart your computer after a successful setup.

**Python environment:** Quanser's script installs packages into the global Python installation reported by the requirements checker and sets the Quanser library paths. Use that interpreter in VS Code. Creating a new virtual environment does not copy these packages; configuring one for Quanser is outside this guide.

## 9. Continue to repository and VS Code setup

Continue to [Personal Computer Setup](personal-computer-setup.md) to open your lab repository, select the correct Python interpreter, and test your installation.
