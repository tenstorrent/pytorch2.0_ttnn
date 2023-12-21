import sys
import os
import json
import csv

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
    rows = [titles]

    for stat in stat_list:
        row = []
        for l in titles:
            if l in stat:
                val = str(stat[l])
            else:
                val = ""
            row.append(val)
        rows.append(row)
    return rows

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else "stat"
    assert os.path.isdir(out) and "cannot find stat folder"
    titles, stat_list = parse_status_json_files(out)
    rows = prepare_csv(titles, stat_list)
    with open("report.csv", "w") as f: 
        csv.writer(f, quotechar = '"').writerows(rows)
