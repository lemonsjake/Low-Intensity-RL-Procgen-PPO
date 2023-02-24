# Procgen Project
A project using OpenAIs' Procgen to learn and exlpore reinforcement learning ...


## Setting up a Linux Virtual Environment:
![venv guidelines (Linux)](https://user-images.githubusercontent.com/89406861/220013729-12755153-877e-49e2-925d-b2c3dd9faa95.png)
@____JoeVincent____


## Setting up a Windows Virtual Environment:
1) Install virtualenv:
    pip install virtualenv
2) Create your Project Folder:
    mkdir project_folder_name
3) Enter your Project Folder:
    cd project_folder_name
4) Create the Virtual Environment:
    virtualenv venv_name
5) Enter your Virtual Environment:
    venv_name\Scripts\activate


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


## States
### What are the possible states?
Not sure if this is right, but I think it's:
  Able to move, Not able to move
  Alive         Level Fail, Level Success


## Observation Space
### What are the possible observations?
If using "gym" and the regular environment, the Observation Space is a Numpy array of shape (64, 64, 3) where values represent RGB pixels the agent sees.
If using "gym3" and the vectorized environment, the Observation Space is a dictionary space where the pixels are under the key "rgb".
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
The rewards depends on which environment is being used. There are 16 different environments where each is a different game w/ unique game rules.
The 16 environments/games are:
- Bigfish
- Bossfight
- Caveflyer
- Chaser
- Climber
- Coinrun
- Dodgeball
- Fruitbot
- Heist
- Jumper
- Leaper
- Maze
- Miner
- Ninja
- Plunder
- Starpilot

For detailed info on each environment including reward info, go to https://github.com/openai/procgen#environments.


## Most of the content provided was obtained via others
@article{cobbe2019procgen,
  title={Leveraging Procedural Generation to Benchmark Reinforcement Learning},
  author={Cobbe, Karl and Hesse, Christopher and Hilton, Jacob and Schulman, John},
  journal={arXiv preprint arXiv:1912.01588},
  year={2019}
}
