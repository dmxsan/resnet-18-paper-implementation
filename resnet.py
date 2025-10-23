import torch
import torch.nn as nn
import torch.nn.functional as F

class BasicBlock(nn.Module):
    expansion = 1

    def __init__(self, in_planes, planes, stride=1):
        super(BasicBlock, self).__init__()
        # TODO: Implement conv layers and shortcut connection
        pass

    def forward(self, x):
        # TODO: Implement forward pass logic with residual connection
        pass