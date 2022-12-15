import os
import shutil
from config import SOURCE_DIR, DEST_DIR, LOG_DIR, VAULT
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d%H%M")
src = SOURCE_DIR + '/' + VAULT
dst = DEST_DIR + '/' + VAULT + '-' + timestamp

print(src, dst, timestamp)
shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=shutil.copy2, ignore_dangling_symlinks=False, dirs_exist_ok=False)

