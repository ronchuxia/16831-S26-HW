import os
import glob
import numpy as np
import matplotlib.pyplot as plt

dqn_path = 'q1_dpn'
ddqn_path = 'q1_ddqn'

script_dir = os.path.dirname(os.path.abspath(__file__))

def load(folder):
    files = sorted(glob.glob(os.path.join(script_dir, folder, '*.csv')))
    runs = [np.genfromtxt(f, delimiter=',', skip_header=1) for f in files]
    steps = runs[0][:, 1]
    rewards = np.array([r[:, 2] for r in runs])
    return steps, rewards.mean(axis=0), rewards.std(axis=0)

fig, ax = plt.subplots(figsize=(10, 6))

for label, path in [('DQN', dqn_path), ('Double DQN', ddqn_path)]:
    steps, mean, std = load(path)
    ax.plot(steps, mean, label=label)
    ax.fill_between(steps, mean - std, mean + std, alpha=0.3)

ax.set_xlabel('Steps')
ax.set_ylabel('Mean Reward')
ax.set_title('DQN vs Double DQN on LunarLander-v3')
ax.legend()
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 'q1.png'), dpi=150)
plt.show()
