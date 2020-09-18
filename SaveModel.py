# save model parameters

import torch 

# eg. net = AlexNet(num_classes=5, init_weights=True)

net = model()

save_path = 'Alex.pth'

torch.save(net.state_dict(), save_path)

# load model parameters

model_weight_path = 'Alex.pth'
model.load_state_dict(torch.load(model_weight_path))
