import kagglehub
import os
import json
import csv
from PIL import Image
import shutil
import pandas as pd
import torch


def create_second_ground_truth(csv_file_1, csv_file_2):
    label_map = {}
    # csv_file_1  is second ground truth
    with open(csv_file_1, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            label_map[row['synset']] = row['label'].strip()


    # synset -> label
    true_labels = []
    image_names = []
    sysnet_names = []
    names_names = []
    
    with open(csv_file_2, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            synset = row["synset"]
            name = row["name"]
            image_name = row["image_name"]
            label_name = label_map[synset]
            
            image_names.append(image_name)
            true_labels.append(label_name)
            sysnet_names.append(synset)
            names_names.append(name)
            
    with open("processed_dataset/ground_truth_2.csv", mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["image_name", "synset", "label", "name"])  
        for image_name, synset, label, name in zip(image_names, sysnet_names, true_labels, names_names):
            writer.writerow([image_name, synset, label, name])


def validate_synset_label_mapping(val_csv_file, label_csv_file):
    label_map = {}
    with open(label_csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            label_map[row['synset']] = row['label'].strip()

    valid_entries = []
    invalid_entries = []
    with open(val_csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            synset = row['synset']
            val_label = row['label'].strip()

            if synset in label_map:
                if label_map[synset] == val_label:
                    valid_entries.append(row)
                else:
                    invalid_entries.append({
                        'image_name': row['image_name'],
                        'synset': synset,
                        'expected_label': label_map[synset],
                        'actual_label': val_label
                    })
            else:
                invalid_entries.append({
                    'image_name': row['image_name'],
                    'synset': synset,
                    'expected_label': 'Not Found',
                    'actual_label': val_label
                })

    return valid_entries, invalid_entries




def txt_to_csv(input_file, output_file):
    with open(input_file, 'r') as txt_file:
        lines = txt_file.readlines()

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['synset', 'label', 'name'])  # Write header

        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 3:
                synset = parts[0]
                label = parts[1]
                name = ' '.join(parts[2:])
                writer.writerow([synset, label, name])


def process_imagenet_dataset(root_dir, output_dir=None, csv_output_path=None):
    if output_dir is None:
        output_dir = os.path.join(os.getcwd(), "processed_dataset")
        os.makedirs(output_dir, exist_ok=True)
    if csv_output_path is None:
        csv_output_path = os.path.join(output_dir, "ground_truth.csv")
        
    image_output_dir = os.path.join(output_dir, "images")
    os.makedirs(image_output_dir, exist_ok=True)

    # ImageNet mappings
    name_to_label_file_path = kagglehub.dataset_download("tusonggao/imagenet-labels")
    synset_to_name_file_path = os.path.join(root_dir, "words.txt")
    with open(os.path.join(name_to_label_file_path, "imagenet_labels.json"), 'r') as file:
        json_data = json.load(file)
    name_to_label_mapping = {label: int(idx) for idx, label in json_data.items()}

    synset_to_name_mapping = {}
    with open(synset_to_name_file_path, 'r') as file:
        for line in file:
            synset, name = line.strip().split("\t")
            synset_to_name_mapping[synset] = name

    val_dir = os.path.join(root_dir, 'val', 'images')
    val_annotations = pd.read_csv(os.path.join(root_dir, 'val', 'val_annotations.txt'), 
                                            sep='\t', header=None, 
                                            names=['image_name', 'synset', 'x1', 'y1', 'x2', 'y2']) 


    with open(csv_output_path, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["image_name", "synset", "label", "name"])  
        
        
        for _, row in val_annotations.iterrows():
            img_name = row['image_name']
            synset = row['synset']
            src_img_path = os.path.join(val_dir, img_name)
            dst_img_path = os.path.join(image_output_dir, img_name)
                
            label_name = synset_to_name_mapping.get(synset, "Unknown")
            label_num = name_to_label_mapping.get(label_name, -1)
            writer.writerow([img_name, synset, label_num, label_name])
            
            shutil.copy2(src_img_path, dst_img_path)


class ImageClassificationDataset(torch.utils.data.Dataset):
    
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        
        self.data = []
        self.labels = []
        self.names = []

        images_dir = os.path.join(root_dir, "images")
        ground_truths_path = os.path.join(root_dir, "ground_truth.csv")
        ground_truths = pd.read_csv(ground_truths_path)
        
        for _, row in ground_truths.iterrows():
            image_name = row["image_name"]
            label = row["label"]
            self.data.append(os.path.join(images_dir, image_name))
            self.labels.append(label)
            
    def __len__(self):
        return len(self.data)
    
    def get_name(self, idx):
        return self.names[idx]

    def __getitem__(self, idx):
        img_path = self.data[idx]
        image = Image.open(img_path).convert('RGB')
        label = self.labels[idx]
        
        if self.transform:
            image = self.transform(image).to(torch.bfloat16)
        
        return image, label
    

    

