import sys
import os
import json
import csv
import math
import matplotlib.pyplot as plt

def parse_status_json_files(status_folder):
    stat_dict = {}
    titles = set()

    for p in os.listdir(status_folder):
        if not p.endswith(".json"):
            continue
        with open(os.path.join(status_folder,p)) as f:
            j = json.load(f)
            name = p.replace(".json", "")
            stat_dict[name] = j
            titles.update(set(j.keys()))
    titles = list(sorted(titles))
    return titles, stat_dict

def prepare_csv(titles, stat_dict):
    rows = [["name"] + titles]
    for name in stat_dict.keys():
        stat = stat_dict[name]
        row = [name]
        for l in titles:
            cnt = str(stat[l]['cnt']) if l in stat else 0
            row.append(cnt)
        rows.append(row)
    row = ["TOTAL"]
    for i in range(1,len(rows[0])):
        row.append(sum([int(rows[j][i]) for j in range(1, len(rows))]))
    rows.append(row)
    return rows

def stat_size(titles, stat_dict):
    results = {}
    def sizeof(dtype: str):
        if dtype in ["torch.float32", "torch.int32"]:
            return 4
        if dtype == ["torch.float64", "torch.int64"]:
            return 8
        print(f"{dtype} not support")
        assert(0)
    for name in stat_dict.keys():
        stat = stat_dict[name]
        for l in titles:
            if l in stat:
                results.setdefault(l, [])
                metas = stat[l]['metas']
                for meta in metas:
                    size = math.prod(meta["shape"]) * sizeof(meta["dtype"])
                    if size != 0:
                        results[l].append(size)
    return results

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else "stat"
    raw = os.path.join(out,"raw")
    assert os.path.isdir(raw) and "cannot find stat/raw folder"
    titles, stat_dict = parse_status_json_files(raw)
    rows = prepare_csv(titles, stat_dict)
    with open(os.path.join(out,"node_count.csv"), "w") as f:
        csv.writer(f, quotechar = '"').writerows(rows)
    op_sizes = stat_size(titles, stat_dict)
    size_dir = os.path.join(out,"total_input_size_dist")
    os.makedirs(size_dir, exist_ok=True)
    for op_name in op_sizes.keys():
        f = os.path.join(size_dir, f"{op_name}.png")
        if len(op_sizes[op_name]) > 0:
            plt.title(f"{op_name}: TOTAL distribution of input size")
            plt.xlabel("input size: prod(shape) * dtype")
            plt.ylabel("count")
            plt.hist(op_sizes[op_name])
            plt.savefig(f)
            plt.cla()
