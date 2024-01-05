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
        try:
            with open(os.path.join(status_folder,p)) as f:
                j = json.load(f)
                model_name = p.replace(".json", "")
                stat_dict[model_name] = j
                titles.update(set(j.keys()))
        except:
            pass
    titles = list(sorted(titles))
    return titles, stat_dict

def generate_node_count(titles, stat_dict, node_count_csv):
    rows = [["model_name"] + titles]
    for model_name in stat_dict.keys():
        stat = stat_dict[model_name]
        row = [model_name]
        for op_name in titles:
            cnt = str(stat[op_name]["cnt"]) if op_name in stat else 0
            row.append(cnt)
        rows.append(row)
    row = ["TOTAL"]
    for i in range(1,len(rows[0])):
        row.append(sum([int(rows[j][i]) for j in range(1, len(rows))]))
    rows.append(row)

    with open(node_count_csv, "w") as f:
        csv.writer(f, quotechar = '"').writerows(rows)
    print(f"{node_count_csv} generated")

def generate_total_input_size(titles, stat_dict, size_dir):
    op_sizes = {}
    def sizeof(dtype: str):
        if dtype in ["torch.float32", "torch.int32"]:
            return 4
        if dtype in ["torch.float64", "torch.int64"]:
            return 8
        print(f"{dtype} not support")
        assert(0)
    for model_name in stat_dict.keys():
        stat = stat_dict[model_name]
        for op_name in titles:
            if op_name in stat:
                op_sizes.setdefault(op_name, [])
                metas = stat[op_name]["metas"]
                for meta in metas:
                    size = math.prod(meta["shape"]) * sizeof(meta["dtype"])
                    op_sizes[op_name].append(size)

    os.makedirs(size_dir, exist_ok=True)
    for op_name in op_sizes.keys():
        f = os.path.join(size_dir, f"{op_name}.png")
        if len(op_sizes[op_name]) > 0:
            plt.title(f"{op_name}: TOTAL distribution of input size")
            plt.xlabel("input size: prod(input_shape) * dtype")
            plt.ylabel("count")
            plt.hist(op_sizes[op_name])
            plt.savefig(f)
            plt.cla()
    print(f"{size_dir} prepared")

def generate_total_arguments(titles, stat_dict, args_dir):
    op_args = {}
    for model_name in stat_dict.keys():
        stat = stat_dict[model_name]
        for op_name in titles:
            if op_name in stat:
                op_args.setdefault(op_name, {})
                args_list = stat[op_name]["args"]
                for args in args_list:
                    for i in range(len(args)):
                        idx = f"arg{i}"
                        op_args[op_name].setdefault(idx, {})
                        if type(args[i]) == str and "not_jsonable:" in args[i]:
                            val_name = "not_jsonable"
                        else:
                            val_name = str(args[i])
                        op_args[op_name][idx].setdefault(val_name, 0)
                        op_args[op_name][idx][val_name] += 1
    os.makedirs(args_dir, exist_ok=True)
    for op_name in op_args.keys():
        args_csv = os.path.join(args_dir, f"{op_name}.csv")
        rows = []
        for idx in op_args[op_name]:
            value_names = list(sorted(op_args[op_name][idx].keys()))
            row1 = [f"{idx}'s appeared value"] + value_names
            row2 = [f"{idx}'s appeared value's count"]
            for v in value_names:
                row2.append(op_args[op_name][idx][v])
            rows.append(row1)
            rows.append(row2)
        with open(args_csv, "w") as f:
            csv.writer(f, quotechar = '"').writerows(rows)
    print(f"{args_dir} prepared")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.getcwd(),"stat")
    raw = os.path.join(out,"raw")
    assert os.path.isdir(raw) and "cannot find stat/raw folder"

    titles, stat_dict = parse_status_json_files(raw)

    generate_node_count(titles, stat_dict, os.path.join(out,"node_count.csv"))
    generate_total_input_size(titles, stat_dict, os.path.join(out,"total_input_size_dist/"))
    generate_total_arguments(titles, stat_dict, os.path.join(out,"total_arguments/"))
