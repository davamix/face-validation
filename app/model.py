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

images = ["./images/img1.jpg", 
        "./images/img1_b.jpg",
        "./images/img1_c.jpg",
        "./images/img1_c.jpg",
        "./images/img1_c.jpg",
        "./images/img1_c.jpg",
        "./images/img2.jpg"]

aligned = []
for i in images:
    img = Image.open(i)
    x_aligned, prob = mtcnn(img, return_prob=True)
    aligned.append(x_aligned)

aligned = torch.stack(aligned).to(device)
embeddings = resnet(aligned).detach().cpu()

dists = [[(e1 - e2).norm().item() for e2 in embeddings] for e1 in embeddings]

print(pd.DataFrame(dists, columns=["img1", "img1b", "img1c", "img1d", "img1e", "img1f", "img2"], index=["img1", "img1b", "img1c", "img1d", "img1e", "img1f", "img2"]))

#            img1     img1b     img1c     img1d     img1e     img1f      img2
# img1   0.000000  0.830902  0.504560  0.504560  0.504560  0.504560  1.384472
# img1b  0.830902  0.000000  0.618703  0.618703  0.618703  0.618703  1.392450
# img1c  0.504560  0.618703  0.000000  0.000000  0.000000  0.000000  1.403071
# img1d  0.504560  0.618703  0.000000  0.000000  0.000000  0.000000  1.403071
# img1e  0.504560  0.618703  0.000000  0.000000  0.000000  0.000000  1.403071
# img1f  0.504560  0.618703  0.000000  0.000000  0.000000  0.000000  1.403071
# img2   1.384472  1.392450  1.403071  1.403071  1.403071  1.403071  0.000000