import torch
import pytest
from chemprop.nn.metrics import SoftRankLoss, ListNetLoss, ListMLELoss, LambdaRankLoss

@torch.no_grad()
def run_loss(loss_class, preds, targets, **kwargs):
    loss = loss_class(**kwargs)
    loss.update(preds, targets)
    result = loss.compute()
    return result.item() if isinstance(result, torch.Tensor) else result


def test_soft_rank_single_item_zero():
    preds = torch.tensor([[1.0]])
    targets = torch.tensor([[1.0]])
    val = run_loss(SoftRankLoss, preds, targets)
    assert pytest.approx(val, rel=1e-5) == 0.0


def test_listnet_single_item_zero():
    preds = torch.tensor([[2.0]])
    targets = torch.tensor([[2.0]])
    val = run_loss(ListNetLoss, preds, targets)
    assert pytest.approx(val, rel=1e-5) == 0.0


def test_listmle_single_item_zero():
    preds = torch.tensor([[0.5]])
    targets = torch.tensor([[0.5]])
    val = run_loss(ListMLELoss, preds, targets)
    assert pytest.approx(val, rel=1e-5) == 0.0


def test_lambdarank_single_item_zero():
    preds = torch.tensor([[0.0]])
    targets = torch.tensor([[0.0]])
    val = run_loss(LambdaRankLoss, preds, targets)
    assert pytest.approx(val, rel=1e-5) == 0.0


def test_loss_returns_scalar_tensor():
    # Verify each returns a torch.Tensor scalar when batched
    preds = torch.tensor([[1.0, 2.0, 3.0]])
    targets = torch.tensor([[3.0, 2.0, 1.0]])
    for cls in (SoftRankLoss, ListNetLoss, ListMLELoss, LambdaRankLoss):
        loss = cls()
        loss.update(preds, targets)
        result = loss.compute()
        assert isinstance(result, torch.Tensor)
        assert result.dim() == 0
