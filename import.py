import os
import shutil
from git import Repo
import datetime as dt
tgl = dt.datetime.now().strftime("%y%m%d_%H%M%S")
os.chdir('/content/initmask')

full_local_path = "/content/initmask"

initt = "/content/init.png"
maskk = "/content/mask.png"
initoutputss = "/content/initmask/outputs/" + str(tgl) + "I.png"
maskoutputss = "/content/initmask/outputs/" + str(tgl) + "M.png"
shutil.copy(initt, initoutputss)
shutil.copy(maskk, maskoutputss)

repo = Repo(full_local_path)
repo.git.add("-A")
repo.index.commit(tgl)

origin = repo.remote(name="origin")
origin.push()


os.chdir('/content')
