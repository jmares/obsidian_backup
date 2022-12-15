# Obsidian Backup

Script to backup my Obsidian vault(s) on a regularly basis

## Goal

I put a lot of information in my **Obsidian** vault on a daily basis, and I recently subscribed to the *Obsidian Sync* service. However, synchronization is not a backup. I want regularly backups.

## Plan

It has been a while since I did any python coding, or even any coding at all.

What do I need? A script that

- [x] Makes a copy of my vault, manually
- [x] Add a timestamp to the name
- [ ] Moves it to a location outside of my desktop pc (OneDrive, DropBox, SSD)
- [ ] Compresses the vault before moving it
- [ ] Encrypts the vault before moving it
- [ ] Automate the process (cron) 
- [ ] Add logging 
- [ ] Multiple vaults

## Log

## 2022-12-15

- Created repository
- Created script to test functionality
    - copy vault to another directory
    - add timestamp to the backup