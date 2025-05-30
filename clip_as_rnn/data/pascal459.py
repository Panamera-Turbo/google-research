# coding=utf-8
# Copyright 2025 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Pascal-459 Dataset."""

import os
import numpy as np
from PIL import Image
# pylint: disable=g-importing-member
from torch.utils.data import Dataset


PASCAL_459_CLASSES = [
    'accordion',
    'aeroplane',
    'air conditioner',
    'antenna',
    'artillery',
    'ashtray',
    'atrium',
    'baby carriage',
    'bag',
    'ball',
    'balloon',
    'bamboo weaving',
    'barrel',
    'baseball bat',
    'basket',
    'basketball backboard',
    'bathtub',
    'bed',
    'bedclothes',
    'beer',
    'bell',
    'bench',
    'bicycle',
    'binoculars',
    'bird',
    'bird cage',
    'bird feeder',
    'bird nest',
    'blackboard',
    'board',
    'boat',
    'bone',
    'book',
    'bottle',
    'bottle opener',
    'bowl',
    'box',
    'bracelet',
    'brick',
    'bridge',
    'broom',
    'brush',
    'bucket',
    'building',
    'bus',
    'cabinet',
    'cabinet door',
    'cage',
    'cake',
    'calculator',
    'calendar',
    'camel',
    'camera',
    'camera lens',
    'can',
    'candle',
    'candle holder',
    'cap',
    'car',
    'card',
    'cart',
    'case',
    'casette recorder',
    'cash register',
    'cat',
    'cd',
    'cd player',
    'ceiling',
    'cell phone',
    'cello',
    'chain',
    'chair',
    'chessboard',
    'chicken',
    'chopstick',
    'clip',
    'clippers',
    'clock',
    'closet',
    'cloth',
    'clothes tree',
    'coffee',
    'coffee machine',
    'comb',
    'computer',
    'concrete',
    'cone',
    'container',
    'control booth',
    'controller',
    'cooker',
    'copying machine',
    'coral',
    'cork',
    'corkscrew',
    'counter',
    'court',
    'cow',
    'crabstick',
    'crane',
    'crate',
    'cross',
    'crutch',
    'cup',
    'curtain',
    'cushion',
    'cutting board',
    'dais',
    'disc',
    'disc case',
    'dishwasher',
    'dock',
    'dog',
    'dolphin',
    'door',
    'drainer',
    'dray',
    'drink dispenser',
    'drinking machine',
    'drop',
    'drug',
    'drum',
    'drum kit',
    'duck',
    'dumbbell',
    'earphone',
    'earrings',
    'egg',
    'electric fan',
    'electric iron',
    'electric pot',
    'electric saw',
    'electronic keyboard',
    'engine',
    'envelope',
    'equipment',
    'escalator',
    'exhibition booth',
    'extinguisher',
    'eyeglass',
    'fan',
    'faucet',
    'fax machine',
    'fence',
    'ferris wheel',
    'fire extinguisher',
    'fire hydrant',
    'fire place',
    'fish',
    'fish tank',
    'fishbowl',
    'fishing net',
    'fishing pole',
    'flag',
    'flagstaff',
    'flame',
    'flashlight',
    'floor',
    'flower',
    'fly',
    'foam',
    'food',
    'footbridge',
    'forceps',
    'fork',
    'forklift',
    'fountain',
    'fox',
    'frame',
    'fridge',
    'frog',
    'fruit',
    'funnel',
    'furnace',
    'game controller',
    'game machine',
    'gas cylinder',
    'gas hood',
    'gas stove',
    'gift box',
    'glass',
    'glass marble',
    'globe',
    'glove',
    'goal',
    'grandstand',
    'grass',
    'gravestone',
    'ground',
    'guardrail',
    'guitar',
    'gun',
    'hammer',
    'hand cart',
    'handle',
    'handrail',
    'hanger',
    'hard disk drive',
    'hat',
    'hay',
    'headphone',
    'heater',
    'helicopter',
    'helmet',
    'holder',
    'hook',
    'horse',
    'horse-drawn carriage',
    'hot-air balloon',
    'hydrovalve',
    'ice',
    'inflator pump',
    'ipod',
    'iron',
    'ironing board',
    'jar',
    'kart',
    'kettle',
    'key',
    'keyboard',
    'kitchen range',
    'kite',
    'knife',
    'knife block',
    'ladder',
    'ladder truck',
    'ladle',
    'laptop',
    'leaves',
    'lid',
    'life buoy',
    'light',
    'light bulb',
    'lighter',
    'line',
    'lion',
    'lobster',
    'lock',
    'machine',
    'mailbox',
    'mannequin',
    'map',
    'mask',
    'mat',
    'match book',
    'mattress',
    'menu',
    'metal',
    'meter box',
    'microphone',
    'microwave',
    'mirror',
    'missile',
    'model',
    'money',
    'monkey',
    'mop',
    'motorbike',
    'mountain',
    'mouse',
    'mouse pad',
    'musical instrument',
    'napkin',
    'net',
    'newspaper',
    'oar',
    'ornament',
    'outlet',
    'oven',
    'oxygen bottle',
    'pack',
    'pan',
    'paper',
    'paper box',
    'paper cutter',
    'parachute',
    'parasol',
    'parterre',
    'patio',
    'pelage',
    'pen',
    'pen container',
    'pencil',
    'person',
    'photo',
    'piano',
    'picture',
    'pig',
    'pillar',
    'pillow',
    'pipe',
    'pitcher',
    'plant',
    'plastic',
    'plate',
    'platform',
    'player',
    'playground',
    'pliers',
    'plume',
    'poker',
    'poker chip',
    'pole',
    'pool table',
    'postcard',
    'poster',
    'pot',
    'pottedplant',
    'printer',
    'projector',
    'pumpkin',
    'rabbit',
    'racket',
    'radiator',
    'radio',
    'rail',
    'rake',
    'ramp',
    'range hood',
    'receiver',
    'recorder',
    'recreational machines',
    'remote control',
    'road',
    'robot',
    'rock',
    'rocket',
    'rocking horse',
    'rope',
    'rug',
    'ruler',
    'runway',
    'saddle',
    'sand',
    'saw',
    'scale',
    'scanner',
    'scissors',
    'scoop',
    'screen',
    'screwdriver',
    'sculpture',
    'scythe',
    'sewer',
    'sewing machine',
    'shed',
    'sheep',
    'shell',
    'shelves',
    'shoe',
    'shopping cart',
    'shovel',
    'sidecar',
    'sidewalk',
    'sign',
    'signal light',
    'sink',
    'skateboard',
    'ski',
    'sky',
    'sled',
    'slippers',
    'smoke',
    'snail',
    'snake',
    'snow',
    'snowmobiles',
    'sofa',
    'spanner',
    'spatula',
    'speaker',
    'speed bump',
    'spice container',
    'spoon',
    'sprayer',
    'squirrel',
    'stage',
    'stair',
    'stapler',
    'stick',
    'sticky note',
    'stone',
    'stool',
    'stove',
    'straw',
    'stretcher',
    'sun',
    'sunglass',
    'sunshade',
    'surveillance camera',
    'swan',
    'sweeper',
    'swim ring',
    'swimming pool',
    'swing',
    'switch',
    'table',
    'tableware',
    'tank',
    'tap',
    'tape',
    'tarp',
    'telephone',
    'telephone booth',
    'tent',
    'tire',
    'toaster',
    'toilet',
    'tong',
    'tool',
    'toothbrush',
    'towel',
    'toy',
    'toy car',
    'track',
    'train',
    'trampoline',
    'trash bin',
    'tray',
    'tree',
    'tricycle',
    'tripod',
    'trophy',
    'truck',
    'tube',
    'turtle',
    'tvmonitor',
    'tweezers',
    'typewriter',
    'umbrella',
    'unknown',
    'vacuum cleaner',
    'vending machine',
    'video camera',
    'video game console',
    'video player',
    'video tape',
    'violin',
    'wakeboard',
    'wall',
    'wallet',
    'wardrobe',
    'washing machine',
    'watch',
    'water',
    'water dispenser',
    'water pipe',
    'water skate board',
    'watermelon',
    'whale',
    'wharf',
    'wheel',
    'wheelchair',
    'window',
    'window blinds',
    'wineglass',
    'wire',
    'wood',
    'wool',
]

PASCAL_459_CLASSE_ID = list(range(459))


PASCAL_459_STUFF_CLASS = [
    'atrium',
    'ceiling',
    'concrete',
    'coral',
    'court',
    'dock',
    'floor',
    'foam',
    'grass',
    'ground',
    'ice',
    'leaves',
    'mountain',
    'parterre',
    'patio',
    'road',
    'rock',
    'rug',
    'sand',
    'sky',
    'snow',
    'stone',
    'sun',
    'wall',
    'water',
    'wood',
]

PASCAL_459_THING_CLASS = [
    'accordion',
    'aeroplane',
    'air conditioner',
    'antenna',
    'artillery',
    'ashtray',
    'baby carriage',
    'bag',
    'ball',
    'balloon',
    'bamboo weaving',
    'barrel',
    'baseball bat',
    'basket',
    'basketball backboard',
    'bathtub',
    'bed',
    'bedclothes',
    'beer',
    'bell',
    'bench',
    'bicycle',
    'binoculars',
    'bird',
    'bird cage',
    'bird feeder',
    'bird nest',
    'blackboard',
    'board',
    'boat',
    'bone',
    'book',
    'bottle',
    'bottle opener',
    'bowl',
    'box',
    'bracelet',
    'brick',
    'bridge',
    'broom',
    'brush',
    'bucket',
    'building',
    'bus',
    'cabinet',
    'cabinet door',
    'cage',
    'cake',
    'calculator',
    'calendar',
    'camel',
    'camera',
    'camera lens',
    'can',
    'candle',
    'candle holder',
    'cap',
    'car',
    'card',
    'cart',
    'case',
    'casette recorder',
    'cash register',
    'cat',
    'cd',
    'cd player',
    'cell phone',
    'cello',
    'chain',
    'chair',
    'chessboard',
    'chicken',
    'chopstick',
    'clip',
    'clippers',
    'clock',
    'closet',
    'cloth',
    'clothes tree',
    'coffee',
    'coffee machine',
    'comb',
    'computer',
    'cone',
    'container',
    'control booth',
    'controller',
    'cooker',
    'copying machine',
    'cork',
    'corkscrew',
    'counter',
    'cow',
    'crabstick',
    'crane',
    'crate',
    'cross',
    'crutch',
    'cup',
    'curtain',
    'cushion',
    'cutting board',
    'dais',
    'disc',
    'disc case',
    'dishwasher',
    'dog',
    'dolphin',
    'door',
    'drainer',
    'dray',
    'drink dispenser',
    'drinking machine',
    'drop',
    'drug',
    'drum',
    'drum kit',
    'duck',
    'dumbbell',
    'earphone',
    'earrings',
    'egg',
    'electric fan',
    'electric iron',
    'electric pot',
    'electric saw',
    'electronic keyboard',
    'engine',
    'envelope',
    'equipment',
    'escalator',
    'exhibition booth',
    'extinguisher',
    'eyeglass',
    'fan',
    'faucet',
    'fax machine',
    'fence',
    'ferris wheel',
    'fire extinguisher',
    'fire hydrant',
    'fire place',
    'fish',
    'fish tank',
    'fishbowl',
    'fishing net',
    'fishing pole',
    'flag',
    'flagstaff',
    'flame',
    'flashlight',
    'flower',
    'fly',
    'food',
    'footbridge',
    'forceps',
    'fork',
    'forklift',
    'fountain',
    'fox',
    'frame',
    'fridge',
    'frog',
    'fruit',
    'funnel',
    'furnace',
    'game controller',
    'game machine',
    'gas cylinder',
    'gas hood',
    'gas stove',
    'gift box',
    'glass',
    'glass marble',
    'globe',
    'glove',
    'goal',
    'grandstand',
    'gravestone',
    'guardrail',
    'guitar',
    'gun',
    'hammer',
    'hand cart',
    'handle',
    'handrail',
    'hanger',
    'hard disk drive',
    'hat',
    'hay',
    'headphone',
    'heater',
    'helicopter',
    'helmet',
    'holder',
    'hook',
    'horse',
    'horse-drawn carriage',
    'hot-air balloon',
    'hydrovalve',
    'inflator pump',
    'ipod',
    'iron',
    'ironing board',
    'jar',
    'kart',
    'kettle',
    'key',
    'keyboard',
    'kitchen range',
    'kite',
    'knife',
    'knife block',
    'ladder',
    'ladder truck',
    'ladle',
    'laptop',
    'lid',
    'life buoy',
    'light',
    'light bulb',
    'lighter',
    'line',
    'lion',
    'lobster',
    'lock',
    'machine',
    'mailbox',
    'mannequin',
    'map',
    'mask',
    'mat',
    'match book',
    'mattress',
    'menu',
    'metal',
    'meter box',
    'microphone',
    'microwave',
    'mirror',
    'missile',
    'model',
    'money',
    'monkey',
    'mop',
    'motorbike',
    'mouse',
    'mouse pad',
    'musical instrument',
    'napkin',
    'net',
    'newspaper',
    'oar',
    'ornament',
    'outlet',
    'oven',
    'oxygen bottle',
    'pack',
    'pan',
    'paper',
    'paper box',
    'paper cutter',
    'parachute',
    'parasol',
    'pelage',
    'pen',
    'pen container',
    'pencil',
    'person',
    'photo',
    'piano',
    'picture',
    'pig',
    'pillar',
    'pillow',
    'pipe',
    'pitcher',
    'plant',
    'plastic',
    'plate',
    'platform',
    'player',
    'playground',
    'pliers',
    'plume',
    'poker',
    'poker chip',
    'pole',
    'pool table',
    'postcard',
    'poster',
    'pot',
    'pottedplant',
    'printer',
    'projector',
    'pumpkin',
    'rabbit',
    'racket',
    'radiator',
    'radio',
    'rail',
    'rake',
    'ramp',
    'range hood',
    'receiver',
    'recorder',
    'recreational machines',
    'remote control',
    'robot',
    'rocket',
    'rocking horse',
    'rope',
    'ruler',
    'runway',
    'saddle',
    'saw',
    'scale',
    'scanner',
    'scissors',
    'scoop',
    'screen',
    'screwdriver',
    'sculpture',
    'scythe',
    'sewer',
    'sewing machine',
    'shed',
    'sheep',
    'shell',
    'shelves',
    'shoe',
    'shopping cart',
    'shovel',
    'sidecar',
    'sidewalk',
    'sign',
    'signal light',
    'sink',
    'skateboard',
    'ski',
    'sled',
    'slippers',
    'smoke',
    'snail',
    'snake',
    'snowmobiles',
    'sofa',
    'spanner',
    'spatula',
    'speaker',
    'speed bump',
    'spice container',
    'spoon',
    'sprayer',
    'squirrel',
    'stage',
    'stair',
    'stapler',
    'stick',
    'sticky note',
    'stool',
    'stove',
    'straw',
    'stretcher',
    'sunglass',
    'sunshade',
    'surveillance camera',
    'swan',
    'sweeper',
    'swim ring',
    'swimming pool',
    'swing',
    'switch',
    'table',
    'tableware',
    'tank',
    'tap',
    'tape',
    'tarp',
    'telephone',
    'telephone booth',
    'tent',
    'tire',
    'toaster',
    'toilet',
    'tong',
    'tool',
    'toothbrush',
    'towel',
    'toy',
    'toy car',
    'track',
    'train',
    'trampoline',
    'trash bin',
    'tray',
    'tree',
    'tricycle',
    'tripod',
    'trophy',
    'truck',
    'tube',
    'turtle',
    'tvmonitor',
    'tweezers',
    'typewriter',
    'umbrella',
    'unknown',
    'vacuum cleaner',
    'vending machine',
    'video camera',
    'video game console',
    'video player',
    'video tape',
    'violin',
    'wakeboard',
    'wallet',
    'wardrobe',
    'washing machine',
    'watch',
    'water dispenser',
    'water pipe',
    'water skate board',
    'watermelon',
    'whale',
    'wharf',
    'wheel',
    'wheelchair',
    'window',
    'window blinds',
    'wineglass',
    'wire',
    'wool',
]

PASCAL_459_STUFF_CLASS_ID = [
    6, 67, 85, 92, 96, 111, 157, 160, 186, 188, 210, 228, 258, 277, 278, 323,
    325, 329, 333, 359, 365, 381, 386, 439, 444, 457,
]

PASCAL_459_THING_CLASS_ID = [
    i for i in range(459) if i not in PASCAL_459_STUFF_CLASS_ID
]


class Pascal459Dataset(Dataset):
  """PASCAL 459 dataset."""

  def __init__(self, root, split='validation', transform=None):
    super(Pascal459Dataset, self).__init__()
    self.root = root
    self.split = split
    self.transforms = transform
    self.image_dir = os.path.join(root, 'images', split)
    self.mask_dir = os.path.join(root, 'annotations_ctx459', split)
    self.images = os.listdir(self.image_dir)

  def __getitem__(self, index):
    image_path = os.path.join(self.image_dir, self.images[index])
    image = Image.open(image_path).convert('RGB')
    target = (
        np.asarray(
            Image.open(
                os.path.join(
                    self.mask_dir, self.images[index].replace('jpg', 'tif')
                )
            ),
            dtype=np.int32,
        )
        + 1
    )

    if self.transforms:
      image = self.transforms(image)

    return image, image_path, target, index

  def __len__(self):
    return len(self.images)
