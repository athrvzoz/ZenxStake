"""Main file for generating results for sample lines-pay game."""

from gamestate import GameState
from game_config import GameConfig
from src.state.run_sims import create_books
from src.write_data.write_configs import generate_configs

if __name__ == "__main__":

    num_threads = 2
    batching_size = 50000
    compression = True
    profiling = False

    num_sim_args = {
        "red": int(1e4),
        "blue": int(1e4),
    }

    run_conditions = {"run_sims": True}
    target_modes = ["red", "blue"]

    config = GameConfig()
    gamestate = GameState(config)
    print(gamestate.get_betmode("red").get_distributions())

    if run_conditions["run_sims"]:
        create_books(
            gamestate,
            config,
            num_sim_args,
            batching_size,
            num_threads,
            compression,
            profiling,
        )
    generate_configs(gamestate)

