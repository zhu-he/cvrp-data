import os
import re
import shutil
from urllib.request import urlopen

base_path = "data"
base_url = "http://vrp.atd-lab.inf.puc-rio.br"
index_path = "/index.php/en/"
pattern = re.compile('"(/media/com_vrp/instances/(.*)/(.*\.(vrp|sol)))"')

with urlopen(base_url + index_path) as response:
    body = response.read().decode()

for path, set_name, file_name, _ in pattern.findall(body):
    print(path)
    dir_path = os.path.join(base_path, set_name)
    file_path = os.path.join(dir_path, file_name)
    os.makedirs(dir_path, exist_ok=True)
    with urlopen(base_url + path, timeout=10) as response:
        with open(file_path, "wb") as file:
            shutil.copyfileobj(response, file)
