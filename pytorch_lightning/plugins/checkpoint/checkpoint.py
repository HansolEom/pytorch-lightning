from abc import ABC
from pathlib import Path
from typing import Any, Dict, Mapping, Union


class CheckpointPlugin(ABC):

    def save_checkpoint(self, checkpoint: Dict[str, Any], filepath: str) -> None:
        """Save model/training states as a checkpoint file through state-dump and file-write.

        Args:
            checkpoint: dict containing model and trainer state
            filepath: write-target file's path
        """

    def load_checkpoint_file(self, checkpoint_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Load checkpoint from a path when resuming or loading ckpt for test/validate/predict stages.
        Args:
            checkpoint_path: Path to checkpoint

        Returns: The loaded checkpoint.
        """
        pass

    def load_model_state_dict(self, checkpoint: Mapping[str, Any]) -> None:
        """
        Given the loaded checkpoint file, loads the state dict into the model.
        Args:
            checkpoint: The loaded checkpoint file.
        """

    def load_optimizer_state_dict(self, checkpoint: Mapping[str, Any]) -> None:
        """
        Given the loaded checkpoint file, loads the optimizer state dicts into optimizers.
        Args:
            checkpoint: The loaded checkpoint file.
        """
