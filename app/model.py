import os
import numpy as np
import pandas as pd
import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image

def collate_fn(x):
    return x[0]

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Runnig on {device}")

mtcnn = MTCNN(image_size=160, margin=0, min_face_size=20, thresholds=[0.6,0.7,0.7], factor=0.709, post_process=True, device=device)

resnet = InceptionResnetV1(pretrained="vggface2").eval().to(device)

img1 = Image.open("./images/img1.jpg")
img1b = Image.open("./images/img1_b.jpg")
img1c = Image.open("./images/img1_c.jpg")
img2 = Image.open("./images/img2.jpg")

x_aligned1, prob1 = mtcnn(img1, return_prob=True)
x_aligned1b, prob1b = mtcnn(img1b, return_prob=True)
x_aligned1c, prob1c = mtcnn(img1c, return_prob=True)
x_aligned2, prob2 = mtcnn(img2, return_prob=True)

aligned = torch.stack([x_aligned1, x_aligned1b, x_aligned1c, x_aligned2]).to(device)

embeddings = resnet(aligned).detach().cpu()

dists = [[(e1 - e2).norm().item() for e2 in embeddings] for e1 in embeddings]

print(pd.DataFrame(dists, columns=["img1", "img1b", "img1c", "img2"], index=["img1", "img1b", "img1c", "img2"]))