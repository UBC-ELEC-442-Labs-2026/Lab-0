# ELEC 442 QArm Lab Computer Quick Start

**Last updated:** September 28, 2026

> Lab computers are already configured. Do not reinstall Python, install packages, or run the personal-computer setup scripts.

## 1. Open Your Team Repository

Your team should have a [private shared repository](personal-computer-setup.md#in-class-lab) with access for all teammates and the required TA(s).

Copy the team's HTTPS URL from GitHub using **Code > HTTPS**. Open **PowerShell**, or choose **Terminal > New Terminal** in VS Code, and run:

```text
cd ~/Documents
git clone <repository-URL>
cd <repository-name>
code .
```

Replace the placeholders, including the angle brackets, with your team's URL and folder name (e.g. `ELEC442-Lab1-Team03`). If prompted to sign into GitHub, use an account with access to the team repository.

If already cloned, skip `git clone` and open the existing folder. Use the repository's **top-level folder**, not just its `code` subfolder, so VS Code loads the lab's workspace settings. If `code .` is not recognized, use **File > Open Folder**. Choose **Trust** if prompted, after checking that this is your team's folder.

## 2. Get the Latest Code

From inside the repository, run:

```text
git fetch
git status
```

If your branch is behind GitHub and you have no uncommitted changes, run:

```text
git pull --ff-only
```

If there are changes left from an earlier session, review them with your team before continuing. For uncommitted changes or a failed pull, follow the [Git troubleshooting steps](personal-computer-setup.md#if-the-pull-does-not-succeed).

## 3. Complete the Lab

Follow the lab instructions for QArm startup, operation, and shutdown. Edit your team's files; the support code and demos in the desktop `lab-machine-env` shortcut are read-only.

If Python is missing or imports fail, use the [interpreter steps below](#python-interpreter-is-missing-or-incorrect).

Save and share useful progress throughout the session using VS Code's **Source Control** panel: review your changes, stage them with **+**, enter a commit message, then **Commit** and **Sync Changes**. See [Saving and sharing your work](personal-computer-setup.md#saving-and-sharing-your-work) for details.

## 4. Before Signing Out

- Shut down the QArm as instructed and stop running scripts.
- Save, stage, **Commit**, and **Sync Changes** in VS Code. Confirm your latest commit and files appear on GitHub before leaving. If syncing fails, resolve the error or save a separate copy of your work.
- Submit your work to Canvas when required by the lab instructions. Pushing to GitHub does not submit your lab; see the [submission instructions](personal-computer-setup.md#code-submission).
- Close the lab programs and sign out of Windows.

## Troubleshooting

### Python interpreter is missing or incorrect

1. Open a `.py` file, press `Ctrl+Shift+P`, and select **Python: Select Interpreter**.
2. Select the following interpreter, or use **Enter interpreter path** to paste it:

   ```text
   C:\ProgramData\Qarm\Python\venv\Scripts\python.exe
   ```

3. Close existing VS Code terminals, open a new one, and retry.

To check which Python VS Code actually runs, put these lines in a temporary `.py` file and choose **Run Python File in Terminal** from the play button:

```python
import sys
print(sys.executable)
```

The output should match the path above. If that interpreter is missing or imports still fail with it selected, tell a TA rather than reinstalling packages.

For `QARM_LAB_ENV` or missing support-file errors, reopen VS Code and retry. If the error persists, show it to a TA.

### Git asks for your name and email

Set these for the current repository, using your own details:

```text
git config user.name "Your Name"
git config user.email "your-email@example.com"
```

These details label your commits; they do not sign you into GitHub. Omit `--global` on lab computers so the settings apply only to this repository. For other Git questions, see [Using Git and the Command Line](personal-computer-setup.md#using-git-and-the-command-line).
