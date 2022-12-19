import os
import shutil
from config import SOURCE_DIR, DEST_DIR, LOG_DIR, VAULT, BACKUP_LOCATIONS
from datetime import datetime
import py7zr

timestamp = datetime.now().strftime("%Y%m%d%H%M")
src = SOURCE_DIR + VAULT
backup_vault_dir = VAULT + '-' + timestamp
dst = DEST_DIR + backup_vault_dir
backup_vault_file = backup_vault_dir + '.7z'

print(src, dst, timestamp)
shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)

with py7zr.SevenZipFile(DEST_DIR + backup_vault_file, 'w', password='secret') as archive:
    archive.writeall(dst, VAULT)

src = DEST_DIR + backup_vault_file
for lable, path in BACKUP_LOCATIONS.items():
    print(lable, path)
    dst = path + backup_vault_file
    shutil.copy2(src, dst)

