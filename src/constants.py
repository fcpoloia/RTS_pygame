# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 25
FPS = 30
BUILDING_COOLDOWN_TIME = 1000
MESSAGE_DURATION = 3000
WAVE_INTERVAL = 25000
ENEMY_SPAWN_RATE = 1
UNIT_ATTACK_RANGE = 50
UNIT_ATTACK_COOLDOWN = 1000  # 1 second cooldown

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



# --- Data ---
# Building data
BUILDING_DATA = {
    "Castle": {"hp": 2750, "image": "../buildings/castle.png", "cost": 75, "resources": {"gold": 75, "wood": 50, "stone": 100}, "size_multiplier": 2},
    "House": {"hp": 2000, "image": "../buildings/house.png", "cost": 20, "resources": {"gold": 20, "wood": 15}},
    "Market": {"hp": 2300, "image": "../buildings/market.png", "cost": 30, "resources": {"gold": 30, "wood": 20, "stone": 25}},
    "Barracks": {"hp": 2400, "image": "../buildings/barracks.png", "cost": 40, "resources": {"gold": 40, "wood": 20, "stone": 15}, "unit": "Swordsman"},
    "Stable": {"hp": 2250, "image": "../buildings/stable.png", "cost": 25, "resources": {"gold": 35, "wood": 20, "stone": 15}, "unit": "Archer"},
    "Farm": {"hp": 2500, "image": "../buildings/farm.png", "cost": 25, "resources": {"gold": 25, "wood": 10}},
    "LumberMill": {"hp": 2000, "image": "../buildings/lumber.png", "cost": 40, "resources": {"gold": 40, "wood": 30, "stone": 10}},
    "Quarry": {"hp": 2500, "image": "../buildings/quarry.png", "cost": 50, "resources": {"gold": 20, "wood": 30, "stone": 10}},
}

# Unit data
UNIT_DATA = {
    "Swordsman": {"image": "../characters/swordsman.png", "cost": {"gold": 50, "food": 30, "people": 1}, "hp": 10, "atk": 1},
    "Archer": {"image": "../characters/bowman.png", "cost": {"gold": 60, "food": 40, "people": 1}, "hp": 8, "atk": 2},
}

# Enemy data
ENEMY_DATA = {
    "Goblin": {"image": "../characters/goblin.png", "speed": 20, "hp": 8, "atk": 1},
    "Orc": {"image": "../characters/orc.png", "speed": 10, "hp": 12, "atk": 2},
}