import sys
import os
import json

def parse_status_json_files(status_folder):
    stat_list = []
    titles = set()

    for p in os.listdir(status_folder):
        if not p.endswith(".json"):
            continue
        with open(os.path.join(out,p)) as f:
            j = json.load(f)
            titles.update(set(j.keys()))
            stat_list.append(j)
            stat_list[-1]["name"] = p.replace(".json", "")
    titles = ["name"] + list(sorted(titles))
    return titles, stat_list

def prepare_csv(titles, stat_list):
    lines = [titles]

    for stat in stat_list:
        line = []
        for l in titles:
            if l in stat:
                val = str(stat[l])
            else:
                val = ""
            line.append(val)
        lines.append(line)
    return lines

def write_csv(lines, out = "report.csv"):
    with open(out, "w") as f:
        for line in lines:
            line = [f'"{l}"' for l in line]
            f.write(",".join(line))
            f.write("\n")

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else "stat"
    assert os.path.isdir(out) and "cannot find stat folder"
    titles, stat_list = parse_status_json_files(out)
    lines = prepare_csv(titles, stat_list)
    write_csv(lines)