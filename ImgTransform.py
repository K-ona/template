from torchvision import transforms

# 其中transforms.RandomResizedCrop                                  
# def __init__(self, size, scale=(0.08, 1.0), ratio=(3. / 4., 4. / 3.), interpolation=Image.BILINEAR):
# scale的范围是取出部分占原始图片面积的随机比例范围
# ratio的范围是宽高比的变化比例
# w = int(round(math.sqrt(target_area * aspect_ratio)))  宽
# h = int(round(math.sqrt(target_area / aspect_ratio)))  高

# 其中transforms.RandomHorizontalFlip(p)
# p：图片水平翻转的概率，default p = 0.5

data_transform = {
    "train": transforms.Compose([transforms.RandomResizedCrop(224), #
                                 transforms.RandomHorizontalFlip(),
                                 transforms.ToTensor(),
                                 transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    }

data_root = os.getcwd()  # get data root path
image_path = data_root + "\\data_set\\flower_data"  # flower data set path
train_dataset = datasets.ImageFolder(root=image_path + "\\train",
                                     transform=data_transform["train"])


