# Procgen Project
A project using OpenAIs' Procgen to learn and exlpore reinforcement learning ...


## Setting up a Linux Virtual Environment:
![venv guidelines (Linux)](https://user-images.githubusercontent.com/89406861/220013729-12755153-877e-49e2-925d-b2c3dd9faa95.png)
@____JoeVincent____


## Requirements:
cffi==1.15.1
cloudpickle==2.2.1
filelock==3.9.0
glcontext==2.3.7
glfw==1.12.0
gym==0.26.2
gym-notices==0.0.8
gym3==0.3.3
imageio==2.25.1
imageio-ffmpeg==0.3.0
importlib-metadata==6.0.0
moderngl==5.7.4
numpy==1.24.2
Pillow==9.4.0
procgen==0.10.7
pycparser==2.21
zipp==3.13.0

@____OpenAi____


The observation space is a box space with the RGB pixels the agent sees in a numpy array of shape (64, 64, 3). The expected step rate for a human player is 15 Hz.
The action space is Discrete(15) for which button combo to press. The button combos are defined in env.py.
If you are using the vectorized environment, the observation space is a dictionary space where the pixels are under the key "rgb".


## States
### What are the possible states?
...

## Observation Space
### What are the possible observations?
The Observation Space is a Numpy array of shape (64, 64, 3) where values represent RGB pixels the agent sees.
- 3 vals per list: [r, g, b]
- 64 lists of rgb vals: [[r, g, b], ..., [r, g, b]]
- 64 lists of those lists of rgb vals: [[[[r, g, b], ..., [r, g, b]], ..., [[r, g, b]]]]
- Example:
  ```
  Observation PER STEP
  [[[[187, 203, 204],
  [197, 209, 210],
  [197, 209, 210],
  ...,
  [196, 237, 240],
  [196, 237, 240],
  [196, 237, 240]],
 
  [[172, 192, 193],
  [172, 192, 193],
  [172, 192, 193],
  ...,
  [172, 192, 193],
  [172, 192, 193],
  [172, 192, 193]]]], dtype=uint8)}
  ```

## Action Space
### What are the possible actions?
The Action Space is Discrete(15) and an action is a tuple of shape 2 where values represent key combos (listed below).
- Key Combos (15 total):
  - ("LEFT", "DOWN")
  - ("LEFT",)
  - ("LEFT", "UP")
  - ("DOWN",)
  - ()
  - ("UP",)
  - ("RIGHT", "DOWN")
  - ("RIGHT",)
  - ("RIGHT", "UP")
  - ("D",)
  - ("A",)
  - ("W",)
  - ("S",)
  - ("Q",)
  - ("E",)
- Example: [13 9] which would be ??
### How are the actions of left/right/etc mapped to numbers?
- Example: [13 9] which would be ??

## Rewards
### What are the possible rewards?
...
