# Section 1

## Question 1

Use the default hyperparameters in the notebook.

Or use the following command.

```bash
python run_hw1.py --expert_policy_file /content/hw_16831/16831-S26-HW/hw1/rob831/policies/experts/Ant.pkl --expert_data /content/hw_16831/16831-S26-HW/hw1/rob831/expert_data/expert_data_Ant-v2.pkl --env_name Ant
```

## Question 2

Change the `num_agent_train_step_per_iter` to 5000 and keep other hyperparameters unchanged in the notebook.

Or use the following command.

```bash
python run_hw1.py --expert_policy_file /content/hw_16831/16831-S26-HW/hw1/rob831/policies/experts/Ant.pkl --expert_data /content/hw_16831/16831-S26-HW/hw1/rob831/expert_data/expert_data_Ant-v2.pkl --env_name Ant --num_agent_train_step_per_iter 5000
```

## Question 3

Change the `num_agent_train_step_per_iter` and keep other hyperparameters unchanged in the notebook.

# Section 2

Change the `num_agent_train_step_per_iter` to 5000, the `n_iter` to 10, and check the `do_dagger` box in the notebook.

Or use the following command.

```bash
python run_hw1.py --expert_policy_file /content/hw_16831/16831-S26-HW/hw1/rob831/policies/experts/Ant.pkl --expert_data /content/hw_16831/16831-S26-HW/hw1/rob831/expert_data/expert_data_Ant-v2.pkl --env_name Ant --num_agent_train_step_per_iter 5000 --n_iter 10 --do_dagger
```