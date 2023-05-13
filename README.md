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


## States
### What are the possible states?
Alive / Able to move, Not able to move, Level Fail, Level Success


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
- Example: [5] which would be ??
### How are the actions of left/right/etc mapped to numbers?
- Example: [5] which would be ("UP")
```
def keys_to_act(self, keys_list: Sequence[Sequence[str]]) -> List[Optional[np.ndarray]]:
        """
        Convert list of keys being pressed to actions, used in interactive mode
        """
        result = []
        for keys in keys_list:
            action = None
            max_len = -1
            for i, combo in enumerate(self.get_combos()):
                pressed = True
                for key in combo:
                    if key not in keys:
                        pressed = False

                if pressed and (max_len < len(combo)):
                    action = i
                    max_len = len(combo)

            if action is not None:
                action = np.array([action])
            result.append(action)
        return result
```
@openai >> procgen >> env.py


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
