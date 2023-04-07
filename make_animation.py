from PIL import Image
import torch

model_facev2 = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", pretrained="face_paint_512_v2")
face2paint = torch.hub.load("bryandlee/animegan2-pytorch:main", "face2paint", size = 1200)

for INPUT_IMG in ['pngegg.png']:
    img = Image.open(INPUT_IMG).convert("RGB")
    out_facev2 = face2paint(model_facev2, img)
    img.show()
    out_facev2.show()


