# ELEC 442 QArm Lab Setup for Personal Computers

**Last updated:** September 24, 2026  

> This guide is for a Windows **personal computer**. Lab computers have already been configured.

> This guide assumes you have followed through the steps of `personal-software-installation.md`.

> This guide assumes you are familiar with Python code, but does not assume that you are familiar with installing Python, the VS Code IDE, or using Git.

# Contents

### I. Repository and VS Code setup

#### Short version
Those that are more familiar with VS Code, Python interpreters, Git, and GitHub may follow the [condensed steps](#short-version-for-familiar-users).

#### Long version
Those that are less familiar with VS Code, Python interpreters, Git, and GitHub should follow the [detailed steps](#1-create-a-repository-on-github).

### II. Git and the Command Line
Those that are less familiar with Git and the Command Line should read the section on [Git and the Command Line](#using-git-and-the-command-line). Those that are more familiar may skip this section.

### III. Code Submission
Read the section on [submission](#code-submission).

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
   git clone <repository-URL>
   cd ELEC442-Lab<lab_num>-ID<student_num>
   code .
   ```

3. Trust the workspace if prompted.

4. Install the VS Code `Python` extension. The `vscode-pdf` extension is optional.

5. Select the Python installation configured in `personal-software-installation.md` (typically Python 3.13). Do not create a new virtual environment as the Quanser packages were installed into this global Python installation.

6. Complete the **Pre-Lab individually** in this repository. Commit and push your work when finished, and follow the individual Pre-Lab [submission](#code-submission) instructions below.

7. For the **In-Class Lab and shared Post-Lab code**, switch to one repository for the whole team. Either:

   - create a new repository named `ELEC442-Lab<lab_num>-Team<2_digit_team_num>` (e.g. `ELEC442-Lab1-Team03`) from the lab template and copy over any required Pre-Lab code; or
   - rename one teammate's existing Pre-Lab repository to `ELEC442-Lab<lab_num>-Team<2_digit_team_num>` and add the other teammates as collaborators.

   If an existing repository is renamed, its owner does not need to clone it again. Updating the saved remote URL is optional:

   ```text
   git remote set-url origin https://github.com/your-user-name/ELEC442-LabX-TeamYY
   ```

8. From this point onward, all teammates should work from the same team repository and keep it synced with GitHub.

9. Read the section on [submission](#code-submission).

The detailed version follows.

## 1. Create a repository on GitHub

Each lab is a repository (repo) template located in the organization [UBC-ELEC-442-Labs-2026](https://github.com/UBC-ELEC-442-Labs-2026). Included is [lab 1](https://github.com/UBC-ELEC-442-Labs-2026/Lab-1) and [lab 2](https://github.com/UBC-ELEC-442-Labs-2026/Lab-2).

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

The repo's URL can always be typed and should resemble the format:

```text
https://github.com/your-user-name/ELEC442-Lab<lab_num>-ID<student_num>
   ```
   
**Alternatively**, using the GUI from your GitHub repository page:

1. Click the green **Code** button.

2. Select **HTTPS**.

3. Copy the URL.

## 3. Clone the repository

1. Open a terminal such as **PowerShell**, or a **VS Code terminal** from VS Code with   `` CTRL + ` ``

2. Go to your Documents folder:

   ```text
   cd ~/Documents
   ```

   `cd` (change directory) changes the folder the terminal is working in. `~` is your home directory.

   Hit `Tab` while typing to autocomplete.


3. Clone the repository using the URL copied from GitHub:

   ```text
   git clone https://github.com/your-user-name/ELEC442-Lab<lab_num>-ID<student_num>
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

   `code .` opens the current folder in VS Code; the dot means “this folder.” Opening the top-level repository folder ensures that VS Code applies the repository's `.vscode` workspace settings.

## 4. Trust the cloned lab folder

The first time VS Code opens a newly cloned repository, it may enter Restricted Mode.

1. Click **Manage** on the Workspace Trust banner.

2. Confirm that the folder shown is your cloned lab repository.

3. Click **Trust**.

## 5. Add VS Code extensions

Python itself is the interpreter that runs your `.py` files. The VS Code Python extension adds Python-specific IDE features such as interpreter selection, code completion, linting, debugging, and the `Run Python File` button found at the top right.

1. Select the `Extensions` menu from the leftmost panel of VS Code.

2. Search for `Python` and install.

3. You may also want to search for and install the third-party extension `vscode-pdf` to view PDFs from within VS Code.

4. You can go back by selecting `Explorer`.

## 6. Select the Python Interpreter

VS Code may automatically select the Python installation configured in the previous guide. To ensure the correct interpreter is being used:

1. Press `Ctrl + Shift + P`

2. Search for **Python: Select Interpreter**.

3. Select the Python installation configured in `personal-software-installation.md` (typically Python 3.13).

Note: Do not create a new virtual environment for these labs. The Quanser setup script has already installed the required packages into this (global) Python installation.

## 7. The Labs

### Pre-Lab

You're now in good shape to start the individual Pre-Lab.

- By having followed these two guides (`personal-software-installation.md` and `personal-computer-setup.md`), you have already completed section `3.1.1` of the Lab 1 Instructions.

- Complete the Pre-Lab. Refer to the section on [Git and the Command Line](#git-and-the-command-line) and the [submission instructions](#code-submission).

- Push your work when done. Confirm on GitHub that the latest commit appears.

### In-Class Lab

The **Pre-Lab is completed individually**, so each student begins with their own repository. For the In-Class Lab and the shared code portion of the Post-Lab, your team should instead work from **one shared repository**.

Choose one of the following options:

- **Option A: Create a new team repository**

  One teammate can create a new repository from the same lab template by following the process in [Section 1](#1-create-a-repository-on-github). Note that the Pre-Lab code will need to be copied over if required.

  Name the repository in the format `ELEC442-Lab<lab_num>-Team<2_digit_team_num>`. For example, `ELEC442-Lab1-Team03`.

  Add all teammates as collaborators. Teammates must accept the invitation before they can push.

- **Option B: Reuse one teammate's Pre-Lab repository**

   One teammate can open their existing repository on GitHub, go to **Settings**, rename it using the same `ELEC442-Lab<lab_num>-Team<2_digit_team_num>` naming convention, and add the other teammates as collaborators.

   The person whose repository was renamed does **not** need to clone it again. GitHub normally redirects the old repository address to the new one, so their existing local copy should continue to work.

   Optionally, they can update the saved GitHub address directly:

   ```text
   git remote set-url origin https://github.com/your-user-name/ELEC442-LabX-TeamYY
   ```

   The local folder itself does not need to be renamed.

Only one shared repository should be used by the team from this point onward. Everyone else should clone that same repository before beginning the In-Class Lab.

# Using Git and the Command Line

This section introduces the command-line and Git commands that are useful for the labs.

A **terminal** is the window in which you type commands. On Windows, we will generally use **PowerShell** as the shell that interprets those commands. You can also use the terminal in **VS Code** which itself runs commands through PowerShell on Windows.

Git is the version-control system that keeps track of changes to your files. **GitHub** stores a remote (cloud) copy of the Git repository so that you and your teammates can share your work.

## Command-Line Basics

The terminal always has a **current working directory**: the folder in which commands are currently being run.

Some useful commands and path shortcuts are:

| Command / symbol | Meaning |
|---|---|
| `pwd` | Show the current folder |
| `ls` | List the contents of the current folder |
| `cd folder-name` | Enter a folder |
| `.` | The current folder |
| `..` | The parent folder |
| `~` | Your home folder |
| `cd ..` | Move to the parent folder |
| `cd ~` | Move to your home folder |
| `mkdir folder-name` | Create a folder |
| `cp` | Copy a file or folder |
| `mv` | Move or rename a file or folder |
| `rm` | Remove a file or folder |
| `code .` | Open current folder in VS Code |
| `code file-name.py` | Create or open a file in VS Code |


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

However, this mental model becomes more complicated when you add teammates who are also pushing commits! If you and a teammate both make commits before either person pulls the other's work, the history can temporarily split into two paths. This is called divergence. Git will usually merge them automatically if the changes do not conflict.

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
git pull
```

`git pull` downloads the new commits and applies them to your local repository. Adding `--ff-only` is more conservative and tells Git to update only when this can be done without creating a merge commit.

If Git stops the pull because it cannot combine the changes automatically, coordinate with your teammate before continuing.

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

If Git asks who you are, set your own name and preferred GitHub-associated email for this repository, then retry the commit:

```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

These commands set the default name and email that Git records in commits you create on this computer. They do not sign you into GitHub. They just tell Git what name and email to write into the metadata of commits you create.

## Useful Git Commands

| Command | Meaning |
|---|---|
| `git clone <URL>` | Create a local copy of a repository |
| `git fetch` | Update Git's information about GitHub without changing your working files |
| `git status` | Show local changes and whether your local copy is ahead of or behind GitHub |
| `git pull` | Download and combine new commits from GitHub |
| `git diff` | Show the line-by-line changes you have made |

> ### A Note on This Git Guide
>
> There are many excellent Git tutorials and references available online. This section is intentionally minimal, and
> the descriptions here are drastically simplified. Many Git tutorials also perform more operations from the command line. In this guide, I deliberately use the VS Code Source Control graphical interface for staging, committing, and syncing changes because it provides a simpler visual workflow.
>
> If in doubt, use this routine:
>
> 1. **Immediately before starting work**, run `git fetch` and `git status`.
>    If GitHub has newer commits, run `git pull` before editing.
>
> 2. **When you finish a useful piece of work**, open VS Code's Source Control panel, **stage** the files you want to save, write a short **commit message**, click **commit**, and click **Sync Changes**.
>
> Fetching before you begin and syncing soon after you finish reduces the chance that you and a teammate will make conflicting changes before sharing your work.

# Code Submission

Note: If the lab instructions or Canvas give different submission requirements, follow those instructions instead.

### Pre-Lab

Submit a `.zip` file containing your modified code to Canvas. To avoid penalties:

1. Name the zip file `l<lab_num>_<student_num>.zip`, where `<student_num>` is your student number and `<lab_num>` is the lab number.

   For example:

   ```text
   l1_12345678.zip
   ```

2. Create a folder with the same name, but without the `.zip` extension:

   ```text
   l1_12345678
   ```

3. Inside this folder, include a folder named `code`.

4. Inside `code`, include **only the Python files that you modified as part of the lab**. Do not include lab instructions, worksheets, VS Code settings, unmodified starter files, or other files and directories.

5. Zip the outer folder. The final submission should have the following structure:

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