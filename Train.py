# AlexNet train
import torch
import torch.nn as nn
from torchvision import transforms, datasets, utils
import matplotlib.pyplot as plt
import numpy as np
import torch.optim as optim
import os
import json
import time

# 导入模型
from model.AlexNet import AlexNet

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model = AlexNet(num_classes=5, init_weights=True)
model.to(device)

loss_function = nn.CrossEntropyLoss()

# lr: learning_rate
optimizer = optim.Adam(model.parameters(), lr=0.0002)

best_acc = 0.0
epo = 10
for epoch in range(epo):
    # train
    # train() 启用 BatchNormalization 和 Dropout
    model.train()
    running_loss = 0.0
    t1 = time.perf_counter()
    #从train_loader,加载一个batch
    for step, data in enumerate(train_loader, start=0):
        images, labels = data
        # zero_grad(): Clears the gradients of all optimized torch.Tensor s.
        optimizer.zero_grad()
        outputs = model(images.to(device))
        loss = loss_function(outputs, labels.to(device))
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        # print train process
        rate = (step + 1) / len(train_loader)
        a = "*" * int(rate * 50)
        b = "." * int((1 - rate) * 50)
        print("\rtrain loss: {:^3.0f}%[{}->{}]{:.3f}".format(int(rate * 100), a, b, loss), end="")
    print()
    print(time.perf_counter()-t1)

    # validate
    # eval()
    # 不启用 BatchNormalization 和 Dropout，保证BN和dropout不发生变化，
    # pytorch框架会自动把BN和Dropout固定住，不会取平均，而是用训练好的值，
    # 不然的话，一旦test的batch_size过小，很容易就会被BN层影响结果。
    model.eval()
    acc = 0.0  # accumulate accurate number / epoch
    with torch.no_grad():
        #从validate_loader加载一个batch
        for val_data in validate_loader:
            val_images, val_labels = val_data
            outputs = model(val_images.to(device))
            predict_y = torch.max(outputs, dim=1)[1]
            #将预测正确的样本个数加起来，返回tensor类型值，item()返回int值
            acc += (predict_y == val_labels.to(device)).sum().item()
        val_accurate = acc / val_num
        if val_accurate > best_acc:
            best_acc = val_accurate
            torch.save(model.state_dict(), save_path)
        print('[epoch %d] train_loss: %.3f  test_accuracy: %.3f' %
              (epoch + 1, running_loss / step, val_accurate))

print('Finished Training')
