# ELEC 442 QArm Lab Setup for Personal Computers

**Last updated:** September 28, 2026

> This guide is for a **personal computer**. Lab computers have already been configured.

> Complete [Personal Computer Software Installation](personal-software-installation.md) first, choosing either the basic Python setup or the Windows virtual QArm setup.

This guide explains how to download your lab files, select Python in VS Code, share code with your team, and submit your work. No prior Git or VS Code experience is required.

**For Lab 0:** you may practise these steps by creating your own repository from the [Lab 0 template](https://github.com/UBC-ELEC-442-Labs-2026/Lab-0). If you already have the Lab 0 files open in VS Code, start at [interpreter selection](#6-select-the-python-interpreter). Lab 0 has no team repository or submission requirement.

## Contents

- **Repository and VS Code setup:** choose the [short version](#short-version-for-familiar-users) or the [detailed steps](#1-create-a-repository-on-github); you do not need to do both.
- **[Using Git and the Command Line](#using-git-and-the-command-line):** how to save and share changes.
- **[Code Submission](#code-submission):** individual and team submission formats for Labs 1 and 2.

In command examples, replace placeholders such as `<lab_num>`, `<student_num>`, and `<repository-URL>` with your own values, without the angle brackets.

# Repository and VS Code Setup

## Short version for familiar users

If you are already comfortable with VS Code, Python interpreters, Git, and GitHub, you may follow these condensed steps.

1. Create a **private** repository from the appropriate [lab template](https://github.com/UBC-ELEC-442-Labs-2026) and name it:

   ```text
   ELEC442-Lab<lab_num>-ID<student_num>
   ```

   Add the required TA(s) as collaborators.
   - For Winter 2026, your TA is Louis with GitHub username `13bytes`.

2. Clone the repository to your computer, preferably under `~/Documents`, and open the repository root in VS Code:

   ```text
   cd ~/Documents
   git clone <repository-URL>
   cd ELEC442-Lab<lab_num>-ID<student_num>
   code .
   ```

3. Trust the workspace if prompted.

4. Install the VS Code **Python** extension published by **Microsoft**. The `vscode-pdf` extension is optional.

5. Select the interpreter configured in the [installation guide](personal-software-installation.md): the global Python version reported by the Quanser setup script, or the interpreter where you installed NumPy for the basic setup. Follow the [verification steps](#verify-your-setup) before starting the lab.

6. Complete the **Pre-Lab individually** in this repository. Commit and push your work when finished, and follow the individual Pre-Lab [submission](#code-submission) instructions below.

7. For the **In-Class Lab and shared Post-Lab code**, switch to one repository for the whole team. Either:
   - create a new repository named `ELEC442-Lab<lab_num>-Team<2_digit_team_num>` (e.g. `ELEC442-Lab1-Team03`) from the lab template and copy over any required Pre-Lab code; or
   - rename one teammate's existing Pre-Lab repository to `ELEC442-Lab<lab_num>-Team<2_digit_team_num>` and add the other teammates as collaborators.

   Submit each individual Pre-Lab before repurposing a repository for team work. If an existing repository is renamed, its owner does not need to clone it again. Updating the saved remote URL is optional:

   ```text
   git remote set-url origin https://github.com/your-user-name/ELEC442-Lab<lab_num>-Team<2_digit_team_num>
   ```

8. Keep the team repository **private** and give all teammates and the required TA(s) access. Everyone else should clone that team repository and open it in VS Code. From this point onward, use it for shared lab code and keep it synced with GitHub.

9. Read the section on [submission](#code-submission).

If you completed the short version, skip the detailed steps and continue to [Using Git and the Command Line](#using-git-and-the-command-line) or [Code Submission](#code-submission).

## Detailed version

## 1. Create a repository on GitHub

Each lab has a repository (repo) template in the organization [UBC-ELEC-442-Labs-2026](https://github.com/UBC-ELEC-442-Labs-2026). Fer example [Lab 1](https://github.com/UBC-ELEC-442-Labs-2026/Lab-1) and [Lab 2](https://github.com/UBC-ELEC-442-Labs-2026/Lab-2).

Each person should:

1. Open the appropriate lab template link in a web browser and sign into GitHub.

2. Click **Use this template**, then **Create a new repository**.

3. Name the repository in the format `ELEC442-Lab<lab_num>-ID<student_num>`, where `<student_num>` is your student number and `<lab_num>` is the lab number. For example, `ELEC442-Lab1-ID12345678`.

4. Set the visibility to **Private**. Because the repository is private, GitHub may ask you to authenticate when cloning or pushing.

5. Create the repository.

6. Open the new repository's **Settings** and find **Collaborators**.

7. Invite the required TA(s) by their GitHub username.
   - For Winter 2026, your TA is Louis with GitHub username `13bytes`.

## 2. Find the repository's clone URL

Your new repository has its own URL. Copy this URL, rather than the course template URL, so that you can push your work to your own repository. It will look like:

```text
https://github.com/your-user-name/ELEC442-Lab<lab_num>-ID<student_num>
```

To copy it from your GitHub repository page:

1. Click the green **Code** button.

2. Select **HTTPS**.

3. Copy the URL.

## 3. Clone the repository

1. Open **PowerShell** on Windows or **Terminal** on macOS/Linux. In VS Code, you can use **Terminal > New Terminal**.

2. Go to your Documents folder:

   ```text
   cd ~/Documents
   ```

   `cd` changes the current folder and `~` is your home directory. If your lab files are elsewhere, use that location instead; quote paths containing spaces.

   Hit `Tab` while typing to autocomplete.

3. Clone the repository using the URL you just copied from GitHub:

   ```text
   git clone https://github.com/<your_github_user_name>/ELEC442-Lab<lab_num>-ID<student_num>
   ```

   `git clone` downloads the repository and its history into a new folder.

   If GitHub asks you to sign in, follow the browser/Git Credential Manager prompt.

4. Enter the new repository folder:

   ```text
   cd ELEC442-Lab<lab_num>-ID<student_num>
   ```

5. Open this folder in VS Code:

   ```powershell
   code .
   ```

   If `code` is not recognized, use **File > Open Folder** in VS Code and select the cloned repository.

   `code .` opens the current folder in VS Code; the dot means “this folder.” Opening the top-level repository folder ensures that VS Code applies the repository's `.vscode` workspace settings.

## 4. Trust the cloned lab folder

The first time VS Code opens a newly cloned repository, it may enter Restricted Mode.

1. Click **Manage** on the Workspace Trust banner.

2. Confirm that the folder shown is your cloned lab repository.

3. Click **Trust**.

## 5. Add VS Code extensions

Python itself is the interpreter that runs your `.py` files. The VS Code Python extension adds Python-specific IDE features such as interpreter selection, code completion, linting, debugging, and the `Run Python File` button found at the top right.

1. Select the `Extensions` menu from the leftmost panel of VS Code.

2. Search for **Python** (extension ID `ms-python.python`) and install the extension published by **Microsoft**.

3. You may also want to search for and install the third-party extension `vscode-pdf` to view PDFs from within VS Code.

4. You can go back by selecting `Explorer`.

## 6. Select the Python Interpreter

VS Code may automatically select the Python installation configured in the previous guide. To ensure the correct interpreter is being used:

1. Open a `.py` file, then press `Ctrl+Shift+P` (`Cmd+Shift+P` on macOS).

2. Search for **Python: Select Interpreter**.

3. Select the interpreter you configured in the [installation guide](personal-software-installation.md):
   - **Windows virtual QArm setup:** select the global Python version reported by Quanser's requirements checker. This is usually 3.13, but can be a newer supported version if you have several installed.
   - **Basic Python setup:** select the interpreter where you installed NumPy. If you created `~/elec442-venv`, select that environment.

4. If the interpreter is missing from the list, choose **Enter interpreter path** and browse to its Python executable. Close any existing VS Code terminals and open a new one after changing interpreters.

For the Quanser setup, do not create a new empty virtual environment: it will not contain the packages installed by the setup script. Use the configured global interpreter unless you have deliberately set up all dependencies in another environment.

### Verify your setup

In your Lab 0 folder, open [`code/Lab_0-python_test.py`](../code/Lab_0-python_test.py) and choose **Run Python File in Terminal** using the play button at the top right of the editor. It should print `hello world` and a number close to zero (small floating-point rounding error is normal).

If NumPy cannot be imported, check the selected interpreter first. To identify the interpreter actually running your code, run these lines in a temporary Python file using the same button:

```python
import sys
print(sys.executable)
```

For the **Windows virtual QArm setup**, continue with the simulator startup and test steps in the [Lab 0 instructions](../Lab_0.pdf). When [`Lab_0-QLabs_test.py`](../code/Lab_0-QLabs_test.py) asks for a mode, enter **`0` for simulation**. The basic Python test alone does not verify QLabs.

| Problem                                                | What to check                                                                                                                                                    |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `QARM_LAB_ENV is not configured`                       | Complete [installation Step 7](personal-software-installation.md#7-configure-the-lab-environment-path), then close and reopen all VS Code windows and terminals. |
| Controller or interface file not found                 | Run the two `Test-Path` checks in Step 7. If you moved `lab-machine-env`, rerun its setup script.                                                                |
| `ModuleNotFoundError` for `numpy`, `pal`, or `quanser` | Confirm the interpreter above. For Quanser imports, also check that installation Step 8 completed successfully and that you restarted afterward.                 |
| QArm is unavailable in QLabs                           | Ask a TA to check your course access.                                                                                                                            |
| Keyboard Navigator reports `expected 3, got 2`         | See the [temporary bug fix](additional/bug-fix.md) for that specific error.                                                                                      |

## 7. The Labs

### Pre-Lab

You're now in good shape to start the individual Pre-Lab.

- Return to your lab instructions after verifying your setup. If you completed only the basic Python setup, use a configured lab computer for exercises that require Quanser or QLabs.

- Complete the Pre-Lab. Refer to the section on [Git and the Command Line](#using-git-and-the-command-line) and the [submission instructions](#code-submission).

- Push your work when done. Confirm on GitHub that the latest commit appears.

### In-Class Lab

The **Pre-Lab is completed individually**, so each student begins with their own repository. For the In-Class Lab and the shared code portion of the Post-Lab, your team should instead work from **one shared repository**.

Choose one of the following options:

- **Option A: Create a new team repository**

  One teammate can create a new repository from the same lab template by following the process in [Section 1](#1-create-a-repository-on-github). Note that the Pre-Lab code will need to be copied over if required.

  Name the repository in the format `ELEC442-Lab<lab_num>-Team<2_digit_team_num>`. For example, `ELEC442-Lab1-Team03`.

  Keep the repository **private** and add all teammates and the required TA(s) as collaborators. Teammates must accept the invitation before they can push.

- **Option B: Reuse one teammate's Pre-Lab repository**

  After completing the individual Pre-Lab submission, one teammate can open their existing repository on GitHub, go to **Settings**, rename it using the same `ELEC442-Lab<lab_num>-Team<2_digit_team_num>` naming convention, and add the other teammates as collaborators.

  The person whose repository was renamed does **not** need to clone it again. GitHub normally redirects the old repository address to the new one, so their existing local copy should continue to work.

  Optionally, they can update the saved GitHub address directly:

  ```text
  git remote set-url origin https://github.com/your-user-name/ELEC442-Lab<lab_num>-Team<2_digit_team_num>
  ```

  The local folder itself does not need to be renamed.

Keep the reused repository **private** and check that the required TA(s) still have access.

Only one shared repository should be used by the team from this point onward. Everyone else should clone that same repository and open it in VS Code before beginning the In-Class Lab. Creating a team repository does not replace each student's individual Pre-Lab submission.

# Using Git and the Command Line

This section introduces the command-line and Git commands that are useful for the labs. Run Git commands from inside your cloned lab repository. Use `pwd` to check the current folder if Git reports that you are not in a repository.

A **terminal** is the window in which you type commands. On Windows, we will generally use **PowerShell** as the shell that interprets those commands. You can also use the terminal in **VS Code** which itself runs commands through PowerShell on Windows.

Git is the version-control system that keeps track of changes to your files. **GitHub** stores a remote (cloud) copy of the Git repository so that you and your teammates can share your work.

## Command-Line Basics

The terminal always has a **current working directory**: the folder in which commands are currently being run.

Some useful commands and path shortcuts are:

| Command / symbol    | Meaning                                 |
| ------------------- | --------------------------------------- |
| `pwd`               | Show the current folder                 |
| `ls`                | List the contents of the current folder |
| `cd folder-name`    | Enter a folder                          |
| `.`                 | The current folder                      |
| `..`                | The parent folder                       |
| `~`                 | Your home folder                        |
| `cd ..`             | Move to the parent folder               |
| `cd ~`              | Move to your home folder                |
| `mkdir folder-name` | Create a folder                         |
| `cp`                | Copy a file or folder                   |
| `mv`                | Move or rename a file or folder         |
| `rm`                | Remove a file or folder                 |
| `code .`            | Open current folder in VS Code          |
| `code file-name.py` | Create or open a file in VS Code        |

For example, during this setup we have been running:

```text
cd ~/Documents
```

which moves into the `Documents` folder inside your home directory, while:

```text
code .
```

opens the current folder (`.`) in VS Code.

You can press `Tab` while typing a file or folder name to autocomplete it.

## Git Basics

A Git repository contains both your files and a history of changes to those files. Your computer has a **local repository**, while the copy stored on GitHub is the **remote repository**.

One way to think about the workflow is:

```text
GitHub → fetch/pull → your computer → edit → stage → commit → push → GitHub
```

- **Fetch**: update Git's information about commits on GitHub without changing your working files.
- **Pull**: download and integrate commits from GitHub.
- **Stage**: select which changes should be included in the next commit.
- **Commit**: save those selected changes as an entry in the local Git history.
- **Push**: upload your local commits to GitHub.

If you and a teammate both make commits before either person pulls the other's work, the history can temporarily split into two paths. This is called **divergence**. A merge combines these histories while preserving both sets of commits. The steps below explain how to do this.

### Before starting work

Because your teammates (or yourself from another computer) may have changed the repository since you last worked on it, first update Git's information about the remote repository:

```text
git fetch
```

`git fetch` checks GitHub for new commits but does not change your working files.

Then run:

```text
git status
```

`git status` shows your local file changes, and whether your local repository is ahead of or behind the remote repository. Running `git fetch` first ensures that this comparison uses the latest information from GitHub.

If `git status` says that GitHub has newer commits and you have no uncommitted changes, update your local repository with:

```text
git pull --ff-only
```

`git pull --ff-only` updates your files when Git can simply move your local branch forward to the latest commit on GitHub. If it reports `Already up to date`, you are ready to work.

#### If the pull does not succeed

1. Run `git status` and read the message. If you have uncommitted changes, save your files, then review, stage, and **Commit** them in VS Code's Source Control panel. Leave **Sync Changes** until after the steps below. Retry `git pull --ff-only`.

2. If Git reports that the branches have **diverged** or that it is **not possible to fast-forward**, both your computer and GitHub have commits the other does not have. Your commits are still saved. With a clean working tree (`git status` shows no uncommitted changes), combine the histories using:

   ```text
   git pull --no-rebase --no-edit
   ```

   This requests a merge and uses Git's default merge message. Git normally combines changes automatically when they do not conflict.

3. If Git reports **merge conflicts**, run `git status` to see the affected files. Open each one in VS Code, review both versions, and edit it to contain the final code you want. Remove any conflict markers (`<<<<<<<`, `=======`, and `>>>>>>>`). Check with your teammate when their intended change is unclear, then save and stage each resolved file. Commit the completed merge in Source Control. See [GitHub's step-by-step guide to resolving merge conflicts](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/resolving-a-merge-conflict-using-the-command-line) for an example.

   To cancel an unfinished merge and return to the state before it started, run `git merge --abort`. This also discards edits made while resolving that merge, so copy any resolution you want to keep elsewhere first.

4. After the merge completes, review the combined code, run the relevant lab checks, and select **Sync Changes** to share the result. Run `git status` again to confirm that your working tree is clean and your branch is up to date with GitHub.

For other errors, such as authentication or network failures, address the reported problem and retry; merging will not fix those errors.

### While working

You can run:

```text
git status
```

at any time to see which files you have changed.

To inspect line-by-line changes that you have not yet staged, run

```text
git diff
```

Neither command modifies your files, so they are safe to run whenever you want to understand the state of the repository.

### Saving and sharing your work

VS Code's **Source Control** panel provides a graphical interface for the most common Git operations.

1. Open the **Source Control** panel on the left side of VS Code.
2. Review the changed files.
3. Stage the files you want to include in the commit using the `+` button.
4. Enter a short commit message describing the changes.
5. Select **Commit**.
6. Select **Sync Changes**.

A commit is initially saved only in your local repository. **Sync Changes** synchronizes your local repository with GitHub, including pulling any new remote commits and pushing your local commits.

After syncing, you can run:

```text
git fetch
git status
```

to confirm that you have no uncommitted changes and that your local repository is up to date with GitHub.

If Git asks who you are, set your own name and preferred GitHub-associated email as the defaults on your personal computer, then retry the commit:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

These commands set the default name and email that Git records in commits you create on this computer. They do not sign you into GitHub. They just tell Git what name and email to write into the metadata of commits you create.

## Useful Git Commands

| Command              | Meaning                                                                     |
| -------------------- | --------------------------------------------------------------------------- |
| `git clone <URL>`    | Create a local copy of a repository                                         |
| `git fetch`          | Update Git's information about GitHub without changing your working files   |
| `git status`         | Show local changes and whether your local copy is ahead of or behind GitHub |
| `git pull --ff-only` | Download new commits and update only if the histories have not diverged     |
| `git diff`           | Show line-by-line changes that have not yet been staged                     |

> ### A Note on This Git Guide
>
> There are many excellent Git tutorials and references available online. This section is intentionally minimal, and
> the descriptions here are drastically simplified. Many Git tutorials also perform more operations from the command line. In this guide, I deliberately use the VS Code Source Control graphical interface for staging, committing, and syncing changes because it provides a simpler visual workflow.
>
> If in doubt, use this routine:
>
> 1. **Immediately before starting work**, run `git fetch` and `git status`.
>    If GitHub has newer commits and you have no uncommitted changes, run `git pull --ff-only` before editing.
> 2. **When you finish a useful piece of work**, open VS Code's Source Control panel, **stage** the files you want to save, write a short **commit message**, click **commit**, and click **Sync Changes**.
>
> Fetching before you begin and syncing soon after you finish reduces the chance that you and a teammate will make conflicting changes before sharing your work.

# Code Submission

Follow the formats below unless the lab instructions or Canvas specify otherwise.

**Pushing to GitHub does not submit your work to Canvas.** Push your latest changes for sharing and backup, then prepare and upload the required ZIP separately.

### Pre-Lab

Submit a `.zip` file containing your modified code to Canvas. To avoid penalties create a zip file `l<lab_num>_<student_num>.zip`, where `<student_num>` is your student number and `<lab_num>` is the lab number.
For example

```text
l1_12345678.zip
```

1. Create a folder with the same name as above, but without the `.zip` extension:

   ```text
   l1_12345678
   ```

2. Inside this folder, include a folder named `code`.

3. Inside `code`, include **only the Python files that you modified as part of the lab**. Do not include lab instructions, worksheets, VS Code settings, unmodified starter files, or other files and directories.

4. Zip the outer folder with the correct name. The final submission should have the following structure:

   ```text
   l1_12345678.zip
   └── l1_12345678/
       └── code/
           ├── modified_file_1.py
           ├── modified_file_2.py
           └── ...
   ```

The names of the `.py` files will depend on the lab. Preserve their original filenames.

Submit written responses on Canvas separately.

### In-Class Lab and Post-Lab

One teammate should submit a `.zip` file containing the team's modified code to Canvas. To avoid penalties:

1. Name the zip file `l<lab_num>_team<team_num>.zip`, where `<team_num>` is your **two digit** team number and `<lab_num>` is the lab number.

   For example:

   ```text
   l1_team03.zip
   ```

2. Create a folder with the same name, but without the `.zip` extension:

   ```text
   l1_team03
   ```

3. Inside this folder, include a folder named `code`.

4. Inside `code`, include **only the Python files that you modified as part of the lab**. Do not include lab instructions, worksheets, VS Code settings, unmodified starter files, or other files and directories.

5. Zip the outer folder. The final submission should have the following structure:

   ```text
   l1_team03.zip
   └── l1_team03/
       └── code/
           ├── modified_file_1.py
           ├── modified_file_2.py
           └── ...
   ```

The names of the `.py` files will depend on the lab. Preserve their original filenames. Modified files from the pre-lab may remain in the lab submission.

Submit individual written responses on Canvas separately.
