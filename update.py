import os
import re
import shutil
import ssl
from urllib.request import urlopen

base_url = "http://vrp.atd-lab.inf.puc-rio.br"
index_path = "/index.php/en/"
pattern = re.compile('"(/media/com_vrp/instances/(.*)/(.*\.(vrp|sol)))"')
context = ssl._create_unverified_context()

with urlopen(base_url + index_path, context=context) as response:
    body = response.read().decode()

for path, dir_path, file_name, _ in pattern.findall(body):
    print(path)
    file_path = os.path.join(dir_path, file_name)
    os.makedirs(dir_path, exist_ok=True)
    with urlopen(base_url + path, timeout=10, context=context) as response:
        with open(file_path, "wb") as file:
            shutil.copyfileobj(response, file)

