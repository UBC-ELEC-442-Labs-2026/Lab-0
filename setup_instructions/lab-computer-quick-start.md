# ELEC 442 QArm Lab Computer Quick Start

**Last updated:** September 25, 2026  

> This guide is for a configured ELEC 442 **lab computer**. Do not reinstall Python, create a virtual environment, or install course software.

## Before the Lab

Your team should already have created its shared repository as described in [Personal Computer Setup](personal-computer-setup.md).

## 1. Open Your Team Repository

Open **PowerShell** or a VS Code terminal and go to your Documents folder:

```text
cd ~/Documents
```

If this is the first time your team repository has been used on this computer, clone it:

```text
git clone <repository-URL>
cd <repository-name>
code .
```

If the repository is already on this computer, do not clone it again. Open the existing repository and make sure it is up to date before starting work.

Refer to [Using Git and the Command Line](personal-computer-setup.md#using-git-and-the-command-line) for an example of a typical Git workflow.

## 2. Trust the Repository

The first time VS Code opens the repository, it may enter Restricted Mode.

1. Click **Manage**.
2. Confirm that this is your team's lab repository.
3. Click **Trust**.

## 3. Complete the Lab

Follow the lab instructions for QArm startup, operation, and shutdown.

The lab computer is already configured. Do not install Python packages, create another environment, or modify shared files. You may add additional VS Code Extensions. 

If the preconfigured environment does not work as expected, tell a TA. For an interpreter or import fail, see [troubleshooting](#python-interpreter-is-missing-or-incorrect).

There is a desktop shortcut to `lab-machine-env` which contains some read-only demo files.

## 4. Before Signing Out

Commit and sync your work to GitHub before signing out of the lab computer.

Confirm on GitHub that your latest commit appears in the team repository.

Then close the lab programs and sign out of Windows.

## Troubleshooting

### Python interpreter is missing or incorrect

The lab computer should automatically use the shared ELEC 442 Python environment.

You may need to select it manually if:

- VS Code asks you to **Select Interpreter**;
- the Python file does not run because no interpreter is selected;
- imports fail with `ModuleNotFoundError`; or
- VS Code shows unresolved-import warnings for packages that should already be installed.

To select the shared course interpreter:

1. Press `Ctrl+Shift+P` to open the Command Palette.
2. Search for and select **Python: Select Interpreter**.
3. If this path already appears, select it:

   ```text
   C:\ProgramData\Qarm\Python\venv\Scripts\python.exe
   ```

4. If it does not appear, choose **Enter interpreter path…**.
5. Choose **Find…** or paste/type the full path:

   ```text
   C:\ProgramData\Qarm\Python\venv\Scripts\python.exe
   ```

6. Press Enter.

If you are unsure which interpreter VS Code is using, run:

```python
import sys
print(sys.executable)
```

It should print:

```text
C:\ProgramData\Qarm\Python\venv\Scripts\python.exe
```