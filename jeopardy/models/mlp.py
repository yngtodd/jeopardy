import torch
import torch.nn as nn
import torch.nn.functional as F


class MultiLayerRegressor(nn.Module):
    """Simple multi-layer regressor."""
    def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, 1)

    def forward(x):
        x = F.relu(self.fc1(x))
        out = self.fc2(x)
        return
