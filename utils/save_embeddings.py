import torch
import sqlite3
import numpy as np
from facenet_pytorch import MTCNN, InceptionResnetV1
from PIL import Image
from pathlib import Path

def get_embeddings(image_path):
    print("Getting embeddings...")
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # print(device)

    mtcnn = MTCNN(image_size=160, margin=0, min_face_size=20, thresholds=[0.6,0.7,0.7], factor=0.709, post_process=True, device=device)
    resnet = InceptionResnetV1(pretrained="vggface2").eval().to(device)

    image = Image.open(image_path)

    face, prob = mtcnn(image, return_prob=True)

    if prob > 0.95:
        face = torch.stack([face]).to(device)
        embeddings = resnet(face).detach().cpu()
        
        print(embeddings)
        print(f"Embeddings size: {embeddings.size()}")


        return embeddings
    
def create_db(username):
    print("Creating DB...")
    conn = sqlite3.connect("users.db")

    create_user_table_query = "CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL UNIQUE)"
    create_embeddings_table_query = "CREATE TABLE IF NOT EXISTS embeddings(username TEXT, value REAL)"
    insert_user_query = "INSERT INTO user(username) VALUES (?)"

    with conn:
        cursor = conn.cursor()

        cursor.execute(create_user_table_query)
        cursor.execute(create_embeddings_table_query)
        cursor.execute(insert_user_query, (username, ))

def save_embeddings(username, embeddings):
    print("Saving values into db...")
    conn = sqlite3.connect("users.db")

    insert_embeddings_query = "INSERT INTO embeddings(username, value) VALUES (?, ?)"
    values = [(username, value.item()) for value in embeddings]
    with conn:
        cursor = conn.cursor()

        cursor.executemany(insert_embeddings_query, values)


# # Set the username
# username = "Me"

# Set the image path
image_path = Path(Path.cwd(), "app", "images", "img1.jpg")

# # Create db and tables with data
# create_db(username)

# # Get the embeddings for the image
embeddings = get_embeddings(image_path)
print(embeddings.norm())

# # Save the embeddings 
# if embeddings is not None:
#     save_embeddings(username, embeddings[-1,:])

# print("Done!")


