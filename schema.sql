DROP DATABASE IF EXISTS baking_sim;
CREATE DATABASE baking_sim;

\c baking_sim;

CREATE TABLE IF NOT EXISTS baking_sim_user (
    baking_sim_user_id SMALLINT GENERATED ALWAYS AS IDENTITY,
    user_name TEXT NOT NULL UNIQUE,
    PRIMARY KEY (baking_sim_user_id)
);

CREATE TABLE IF NOT EXISTS user_stats (
    user_stats_id SMALLINT GENERATED ALWAYS AS IDENTITY, 
    user_id SMALLINT UNIQUE NOT NULL,
    user_level SMALLINT NOT NULL DEFAULT 1,
    user_xp INT NOT NULL DEFAULT 0,
    user_max_xp INT,
    user_good_luck SMALLINT NOT NULL DEFAULT 10,
    user_bad_luck SMALLINT NOT NULL DEFAULT 0,
    user_max_luck SMALLINT NOT NULL DEFAULT 100,
    PRIMARY KEY (user_stats_id),
    FOREIGN KEY (user_id) REFERENCES baking_sim_user(baking_sim_user_id),
    CONSTRAINT user_level_constraint CHECK (user_level > 0 AND user_level < 5),
    CONSTRAINT user_good_luck_constraint CHECK (user_good_luck >= 0 AND user_good_luck < user_max_luck),
    CONSTRAINT user_bad_luck_constraint CHECK (user_bad_luck >= 0 AND user_bad_luck < user_max_luck)
);

CREATE TABLE IF NOT EXISTS user_stock (
    user_inventory_id SMALLINT GENERATED ALWAYS AS IDENTITY,
    user_id SMALLINT UNIQUE NOT NULL,

    PRIMARY KEY (user_inventory_id),
    FOREIGN KEY (user_id) REFERENCES user_stats (user_id)
);
