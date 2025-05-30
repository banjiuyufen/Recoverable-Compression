import os
from .clip_encoder import CLIPVisionTower, CLIPTextEncoder


def build_vision_tower(vision_tower_cfg, **kwargs):
    vision_tower = getattr(vision_tower_cfg, 'mm_vision_tower', getattr(vision_tower_cfg, 'vision_tower', None))
    is_absolute_path_exists = os.path.exists(vision_tower)
    if is_absolute_path_exists or vision_tower.startswith("openai") or vision_tower.startswith("laion"):
        return CLIPVisionTower(vision_tower, args=vision_tower_cfg, **kwargs)

    raise ValueError(f'Unknown vision tower: {vision_tower}')


def build_text_encoder(text_encoder_cfg, **kwargs):
    text_encoder = getattr(text_encoder_cfg, 'mm_vision_tower', getattr(text_encoder_cfg, 'text_encoder', None))
    is_absolute_path_exists = os.path.exists(text_encoder)
    if is_absolute_path_exists or text_encoder.startswith("openai") or text_encoder.startswith("laion"):
        return CLIPTextEncoder(text_encoder, args=text_encoder_cfg, **kwargs)

    raise ValueError(f'Unknown text tower: {text_encoder}')
