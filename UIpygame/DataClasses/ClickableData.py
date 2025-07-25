from dataclasses import dataclass
from UIpygame.Utils.Utils import Utils
from UIpygame.Constants import RunCommandAt
from UIpygame.Constants import MouseButton
from UIpygame.Constants import ClickType
import pygame

@dataclass
class ClickableData:
    """
    Dataclass containing data used by all children of GuiItem.
    """
    clickable: bool = True
    clickable_rect: pygame.Rect | tuple[float|str, float|str, float|str, float|str] = None
    command: callable = Utils.emptyFunction
    run_command_at: RunCommandAt = RunCommandAt.START_OF_CLICK
    mouse_button: MouseButton = MouseButton.LEFT_CLICK
    click_type: ClickType = ClickType.LEFT_CLICK
    dragable: bool = False

