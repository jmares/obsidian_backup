# Obsidian Backup

Script to backup my Obsidian vault(s) on a regularly basis

## Goal

I put a lot of information in my **Obsidian** vault on a daily basis, and I recently subscribed to the *Obsidian Sync* service. However, synchronization is not a backup. I want regularly backups.

## Plan

It has been a while since I did any python coding, or even any coding at all.

What do I need? A script that

- [x] Makes a copy of my vault, manually
- [x] Add a timestamp to the name
- [x] Moves it to a location outside of my desktop pc (OneDrive, DropBox, SSD, ...)
- [x] Compresses the vault before moving it
- [x] Encrypts the vault before moving it
- [x] Automate the process (cron) 
- [ ] Exception handling
- [ ] Add logging 
- [x] Multiple vaults
- [ ] SCP to remote server
- [ ] Clean up temporary files


## Problem Solving

### How to add a cronjob on a Mac

Compared to cronjob on a Ubuntu server I encountered several problems.

I want backups every hour that my computer is on, at 10 minutes past the hour.

First problem: The `Terminal.app` and `cron` need **full disk access**.

- Go to *System Preferences*
- Go to *Security and Privacy*
- Go to the tab *Privacy*
- Unlock to make changes
- Click on the `+` underneath the list of apps
- The app you are looking for `cron` is in the `/usr/sbin` directory
- Select it and click `Open`
- Check `cron` and `Terminal.app` in the list
- Lock it

Second problem: You need to specify the **full path** for the python version you are using and for the location of your python script.

Where is your python version located on the hard disk? In the terminal type the following command:

```bash
which python
```

The result I got, was:

```
/Users/myname/.pyenv/shims/python
```

If you want to know the full path of the python script ypu want to use, go to the directory using the terminal and type the following command:

```bash
pwd
```

The result I got, was:

```
/Users/myname/cronjobs/obsidian_backups
```

Open the crontab editor with the following command (my default editor is `vi`):

```bash
crontab -e
```

I am not going to explain how to use `vi` here.

Enter the following line and save the file.

```
10 * * * *	/Users/myname/.pyenv/shims/python /Users/myname/cronjobs/obsidian_backups/obs_backup.py
```

This got it working for me.

## Log

### 2022-12-22

- Renaming some variables
- Moving code into functions
- Basic exception handling
- Dealing with multiple vaults
- Cronjob on Mac mini

### 2022-12-19

- copy compressed and encrypted backupt to two locations outside of internal HD, in my case:
    - external SSD
    - OneDrive
- quick and dirty

### 2022-12-18

- installing `py7zr`

```bash
pip install py7zr
```

- compressing and encrypting locally

### 2022-12-15

- Created repository
- Created script to test functionality
    - copy vault to another directory
    - add timestamp to the backup