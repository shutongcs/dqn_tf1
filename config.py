mahn = 10000

class MemoryConfig:
  mem_dir = "memory/"
  memory_size = 10 * mahn

class ModelConfig:
  model_name = "DQN"
  in_height = 84
  in_width = in_height

  batch_size = 32
  history_length = 4

  cnn_archi = [(32, 8, 4),
               (64, 4, 2),
               (64, 3, 1)]
  fc_archi = [512]

  log_dir = "tensorboard/"
  ckpt_dir = "ckpt/"

class EnvironmentConfig:
  env_name = "BreakoutDeterministic-v4"

  max_reward = 1.
  min_reward = -1.

class TrainConfig:
  max_step = 500 * mahn

  initial_exploration = 1.
  final_exploration = 0.1
  final_exploration_step = 100 * mahn
  
  replay_start_size = 5 * mahn
  fixed_net_update_frequency = mahn

  replay_frequency = 4
  action_repeat = 4

  no_op_max = 30
  
  df = 0.99

  lr = 0.00025
  lr_min = 0.00025
  lr_decay = 0.96
  lr_decay_step = 5 * mahn

  save_step = 10 * mahn
  summarize_step = 5 * mahn
  load_model = True
  
class Config(MemoryConfig, ModelConfig, EnvironmentConfig, TrainConfig):
  load_ckpt = True
  train = True
  render = 0