import torch
from facenet_pytorch import MTCNN, InceptionResnetV1

class ValidationService():
    def __init__(self):
        device = torch.device("cuda:0" if torch.cuda_is_available() else "cpu")

        self.mtcnn = MTCNN(image_size=160, margin=0, min_face_size=20, thresholds=[0.6, 0.7, 0.7], factor=0.709, post_process=True, device=device)
        self.resnet = InceptionResnetV1(pretrained="vggface2").eval().to(device)

    def get_embeddings(self, image):
        # Extract face from image
        face, prob = self.mtcnn(image, return_prob=True)

        if prob > 0.95:
            face = torch.stack([face]).to(device)
            embeddings = self.resnet(face).detach().cpu()

            return embeddings[-1,:]

        # Get embeddings
        embeddings = self.resnet(face).detach().cpu()

        return embeddings