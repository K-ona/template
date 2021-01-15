# image samples arranged in this way: 
# 
# root/class_x/xxx.ext
# root/class_x/xxy.ext
# root/class_x/xxz.ext

# root/class_y/123.ext
# root/class_y/nsdf3.ext
# root/class_y/asd932_.ext

# IMG_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm', '.tif', '.tiff', '.webp')

from torchvision import datasets, transforms
import torch

# class ImageFolder 
# self.classes = classes                  str, 对应于训练集类别名，class_x, class_y
# self.class_to_idx = class_to_idx        dict，classname对应的target整数标识，从0开始
# self.samples = samples                  list of tuple, 对应于该文件夹下所有的文件的路径及其对应的target标识,(path, class_index)
# self.imgs = self.samples                同上
# self.targets = [s[1] for s in samples]  每个训练集的target

# transform (callable, optional): A function/transform that  takes in an PIL image
#             and returns a transformed version. E.g, ``transforms.RandomCrop``
# target_transform (callable, optional): A function/transform that takes in the
# target and transforms it.
# loader (callable, optional): A function to load an image given its path.
# is_valid_file (callable, optional): A function that takes path of an Image file
# and check if the file is a valid file (used to check of corrupt files)        
          
train_dataset = datasets.ImageFolder(root = image_data_path,
                                     transform = data_transform["val"],  
                                     target_transform=None,
                                     loader=default_loader, 
                                     is_valid_file = None)

validate_dataset = datasets.ImageFolder(root = image_path + "\\val",
                                        transform = data_transform["val"])
# dataset (Dataset): dataset from which to load the data.
#         batch_size (int, optional): how many samples per batch to load
#             (default: ``1``).
#         shuffle (bool, optional): set to ``True`` to have the data reshuffled
#             at every epoch (default: ``False``).
#         sampler (Sampler or Iterable, optional): defines the strategy to draw
#             samples from the dataset. Can be any ``Iterable`` with ``__len__``
#             implemented. If specified, :attr:`shuffle` must not be specified.
#         batch_sampler (Sampler or Iterable, optional): like :attr:`sampler`, but
#             returns a batch of indices at a time. Mutually exclusive with
#             :attr:`batch_size`, :attr:`shuffle`, :attr:`sampler`,
#             and :attr:`drop_last`.
#         num_workers (int, optional): how many subprocesses to use for data
#             loading. ``0`` means that the data will be loaded in the main process.
#             (default: ``0``)
#         collate_fn (callable, optional): merges a list of samples to form a
#             mini-batch of Tensor(s).  Used when using batched loading from a
#             map-style dataset.
#         pin_memory (bool, optional): If ``True``, the data loader will copy Tensors
#             into CUDA pinned memory before returning them.  If your data elements
#             are a custom type, or your :attr:`collate_fn` returns a batch that is a custom type,
#             see the example below.
#         drop_last (bool, optional): set to ``True`` to drop the last incomplete batch,
#             if the dataset size is not divisible by the batch size. If ``False`` and
#             the size of dataset is not divisible by the batch size, then the last batch
#             will be smaller. (default: ``False``)
#         timeout (numeric, optional): if positive, the timeout value for collecting a batch
#             from workers. Should always be non-negative. (default: ``0``)
#         worker_init_fn (callable, optional): If not ``None``, this will be called on each
#             worker subprocess with the worker id (an int in ``[0, num_workers - 1]``) as
#             input, after seeding and before data loading. (default: ``None``)

batch_size = 32
train_loader = torch.utils.data.DataLoader( dataset = train_dataset, batch_size = batch_size, shuffle=False, sampler=None,
                                            batch_sampler=None, num_workers=0, collate_fn=None,
                                            pin_memory=False, drop_last=False, timeout=0,
                                            worker_init_fn=None, multiprocessing_context=None,
                                            generator=None)

validate_loader = torch.utils.data.DataLoader(dataset = validate_dataset,
                                              batch_size = 4, shuffle=True,
                                              num_workers=0)
                   


