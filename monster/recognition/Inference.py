# -*- coding: utf-8 -*-
"""
dependencies:
torch
torchvision
"""

import torch
import torchvision
from PIL import Image
class Inference:
    def __init__(self,transform,model_path):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = torch.load(model_path,self.device).eval()
        self.transforms = transform
    def prediction(self,img_path):
        self.image = Image.open(img_path)
        image = self.transforms(self.image)
        image = image.reshape(1,image.shape[0],image.shape[1],image.shape[2])
        image = image.to(self.device)
        #model = self.model.eval()
        preds = self.model(image)
        if len(preds[0]['labels'])>1: # more than 1 items detected
            return preds[0]['labels'][0].item(), preds[0]['scores'][0].item()
        elif len(preds[0]['labels']) == 1: #exactly 1 item
            return preds[0]['labels'].item(), preds[0]['scores'][0].item()
        else: #image unrecognized
            print('Image Unrecognized')
            return None, None
    

#Demo code
model_path = 'D:/model.pt'  #model path
transform = torchvision.transforms.ToTensor()
img_path = 'D:/weaha/bottle_front/bottle_front_349.jpg'
inference = Inference(transform,model_path) #Initiate inference class
labels,score = inference.prediction(img_path)
print(labels,score)

#若 labels 和 score 為空值，代表模型辨認失敗