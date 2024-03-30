from PIL import Image
from torchvision.transforms import v2 
import torch
import warnings

warnings.filterwarnings("ignore")

def model_load(path='model\model_7314.pth'):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = torch.load(path, map_location=device)
    model.eval()
    return model, device

def ask_image_path():
    print('image path:')
    path = input()
    return path

def preprocess_image(image_path, device):
    image = Image.open(image_path)
    transforms = v2.Compose([
                            v2.Resize((380, 380)),
                            v2.ToTensor(),
                            v2.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                            ])
    image = transforms(image).unsqueeze(0)
    return image.to(device)


@torch.no_grad()
def predict_image(image):
    output = model(image)
    predicted_class_index = torch.argmax(output[0]).item()
    return predicted_class_index

class_names = [
            'Close Up',
            'Extreme Close Up',
            'Extreme Wide',
            'Medium',
            'Medium Close Up',
            'Medium Wide',
            'Wide'
            ]
model, device = model_load()
image = preprocess_image(ask_image_path(), device)
prediction = predict_image(image)
print(class_names[prediction])


