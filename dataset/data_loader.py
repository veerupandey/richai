# train validation and test
from torch.utils.data import DataLoader
from torch.utils.data.sampler import SubsetRandomSampler
from utils.helpers import get_config


def data_loader(dset):
    """Create pytorch data loader"""
    train_loader = DataLoader(
        dset,
        batch_size=get_config("data_loader.batch_size"),
        shuffle=False,
        sampler=SubsetRandomSampler(dset.train_indices),
        num_workers=get_config("data_loader.num_workers"),
        drop_last=get_config("data_loader.drop_last"),
    )

    val_loader = DataLoader(
        dset,
        batch_size=get_config("data_loader.batch_size"),
        shuffle=False,
        sampler=SubsetRandomSampler(dset.val_indices),
        num_workers=get_config("data_loader.num_workers"),
        drop_last=get_config("data_loader.drop_last"),
    )

    test_loader = None
    if hasattr(dset, "test_indices"):
        test_loader = DataLoader(
            dset,
            batch_size=get_config("data_loader.batch_size"),
            shuffle=False,
            sampler=SubsetRandomSampler(dset.test_indices),
            num_workers=get_config("data_loader.num_workers"),
            drop_last=get_config("data_loader.drop_last"),
        )

    return (train_loader, val_loader, test_loader)