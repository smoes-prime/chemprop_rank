import torch
import pytest
from chemprop.nn.metrics import RBOLoss

def test_rbo_perfect_match():
    # Perfect ranking should yield loss 0
    preds = torch.tensor([[3.0, 2.0, 1.0]])
    targets = torch.tensor([[3.0, 2.0, 1.0]])
    loss = RBOLoss(p=0.9)
    loss.update(preds, targets)
    result = loss.compute().item()
    assert pytest.approx(result, rel=1e-5) == 0.0


def test_rbo_reverse():
    # Reverse ranking should yield maximal loss (1 - minimal overlap)
    preds = torch.tensor([[1.0, 2.0, 3.0]])
    targets = torch.tensor([[3.0, 2.0, 1.0]])
    loss = RBOLoss(p=0.9)
    loss.update(preds, targets)
    result = loss.compute().item()
    # RBO for reverse 3-items at p=0.9 is small but not zero; check it's near 1
    assert result > 0.5


def test_rbo_multiple_samples():
    # Test batching across samples
    preds = torch.tensor([[3.0, 1.0, 2.0], [1.0, 3.0, 2.0]])
    targets = torch.tensor([[3.0, 2.0, 1.0], [3.0, 2.0, 1.0]])
    loss = RBOLoss(p=0.8)
    loss.update(preds, targets)
    # compute shouldn't error
    result = loss.compute()
    assert isinstance(result, torch.Tensor)
    assert 0.0 <= result.item() <= 1.0
