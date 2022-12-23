"""Obsidian Backup, by Johan Mares
Backing up my precious second brain(s)."""

import os
import shutil
from config import SOURCE_PATH, TEMP_PATH, LOG_PATH, VAULTS, BACKUP_LOCATIONS
from datetime import datetime
import py7zr
from password_generator import get_password

def create_backup(vault):
    """
    Copy vault to a temp directory, compress and encrypt the vault
    """
    
    timestamp = datetime.now().strftime("%Y%m%d%H%M")

    try:

        # Copy vault to temp directory
        src = SOURCE_PATH + vault
        temp_vault_dir = vault + '-' + timestamp
        dst = TEMP_PATH + temp_vault_dir
        #shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)
        #print("Copying", src, "to", dst)
        shutil.copytree(src, dst)

        # Compress and encrypt temp vault directory
        backup_vault = temp_vault_dir + '.7z'
        #print("Compressing and encrypting", backup_vault)
        with py7zr.SevenZipFile(TEMP_PATH + backup_vault, 'w', password=get_password(temp_vault_dir)) as archive:
            archive.writeall(dst, vault)

        move_backup(backup_vault)

    except Exception as e:
        print(e)


def move_backup(backup_vault):
    """
    Copy the compressed and encrypted backup of a vault to one or more backup locations
    """
    src = TEMP_PATH + backup_vault
    
    try: 
            
        for lable, path in BACKUP_LOCATIONS.items():
            #print(lable, path)
            dst = path + backup_vault
            #print("Copying", src, "to", dst)
            shutil.copy2(src, dst)
    
    except Exception as e:
        print(e)


def main():
    """
    Backups one or more Obsidian vaults to one or more backup locations
    """
    
    for vault in VAULTS:
        #print("Backing up vault", vault)
        create_backup(vault)


# If this program was run (instead of imported), run:
if __name__ == '__main__':
    main()
