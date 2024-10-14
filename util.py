import datetime
import bank_threads
import json
from random import randint
res = []
filse = ["file.json", "file1.json", "file2.json", "file3.json", "file4.json", "file5.json"]

# for file in filse:
#     for _ in range(100_000):
#         res.append(randint(0, 1000000))
#     with open(file, "w") as f:
#         json.dump(res, f)
#     res = []
res_count = []
start = datetime.datetime.now()
for fil in filse:
    with open(fil, "r") as f:
        data = json.load(f)
        res_count.extend(data)

print(sum(res_count))
end = datetime.datetime.now()
print(end - start)
