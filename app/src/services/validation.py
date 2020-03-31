import torch
from facenet_pytorch import MTCNN, InceptionResnetV1

class ValidationService():
    def __init__(self):
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        self.mtcnn = MTCNN(image_size=160, margin=0, min_face_size=20, thresholds=[0.6, 0.7, 0.7], factor=0.709, post_process=True, device=self.device)
        self.resnet = InceptionResnetV1(pretrained="vggface2").eval().to(self.device)

    def get_embeddings(self, image):
        embeddings = None
        # Extract face from image
        face, prob = self.mtcnn(image, return_prob=True)

        if prob is not None and prob > 0.95:
            face = torch.stack([face]).to(self.device)
            embeddings = self.resnet(face).detach().cpu()

            return embeddings[-1,:]

        return embeddings

    '''
    Returns the Euclidean distance between the embeddings
    '''
    def get_distance(self, embeddings_1, embeddings_2):
        return torch.sqrt(torch.sum((embeddings_1 - embeddings_2)**2)).item()