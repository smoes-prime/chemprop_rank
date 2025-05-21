import torch
import pytest
from chemprop.nn.metrics import NDCGLoss

def test_ndcg_perfect_match():
    # Perfect ranking yields loss 0
    preds = torch.tensor([[3.0, 2.0, 1.0]])
    targets = torch.tensor([[3.0, 2.0, 1.0]])
    loss = NDCGLoss(fraction=1.0)
    loss.update(preds, targets)
    result = loss.compute().item()
    assert pytest.approx(result, rel=1e-5) == 0.0


def test_ndcg_reverse():
    # Reverse ranking should yield high loss
    preds = torch.tensor([[1.0, 2.0, 3.0]])
    targets = torch.tensor([[3.0, 2.0, 1.0]])
    loss = NDCGLoss(fraction=1.0)
    loss.update(preds, targets)
    result = loss.compute().item()
    assert result > 0.5


def test_ndcg_top_fraction():
    # With fraction <1, ensure uses top fraction
    preds = torch.tensor([[5.0, 1.0, 2.0, 4.0, 3.0]])
    targets = torch.tensor([[1.0, 5.0, 2.0, 4.0, 3.0]])
    # top 40% means k=2
    loss = NDCGLoss(fraction=0.4)
    loss.update(preds, targets)
    result = loss.compute().item()
    # NDCG applies only to top 2: best possible would order top-2 equivalently
    assert 0.0 <= result <= 1.0


def test_ndcg_batch():
    # batch update works
    preds = torch.tensor([[3.0,1.0], [1.0,3.0]])
    targets = torch.tensor([[3.0,1.0], [1.0,3.0]])
    loss = NDCGLoss(fraction=0.5)
    loss.update(preds, targets)
    result = loss.compute()
    assert isinstance(result, torch.Tensor)
    assert 0.0 <= result.item() <= 1.0
