import random

# Define the rarity probabilities for each reward
rewards_probabilities = {
    "rare": {
        "coins": {50: 0.4190},
        "power points": {25: 0.3260},
        "credits": {10: 0.0230},
        "bling": {20: 0.0230},
        "xp doubler": {1: 0.2090}
    },
    "super rare": {
        "coins": {100: 0.4238},
        "power points": {50: 0.3311},
        "credits": {30: 0.0331},
        "bling": {50: 0.0331},
        "common pin": {1: 0.0331},
        "random spray": {1: 0.0132},
        "xp doubler": {1: 0.1325}
    },
    "epic": {
        "coins": {200: 0.2105},
        "power points": {100: 0.2105},
        "rare brawler": {1: 0.0526},
        "rare skin": {1: 0.0526},
        "common pin": {1: 0.1579},
        "rare pin": {1: 0.0526},
        "random spray": {1: 0.1579},
        "xp doubler": {1: 0.1053}
    },
    "mythic": {
        "coins": {500: 0.0949},
        "gadget": {1: 0.1582},
        "power points": {200: 0.1899},
        "super rare brawler": {1: 0.0949},
        "epic brawler": {1: 0.0633},
        "mythic brawler": {1: 0.0190},
        "rare skin": {1: 0.1582},
        "rare pin": {1: 0.0633},
        "epic pin": {1: 0.0316},
        "random spray": {1: 0.0633},
        "profile icon": {1: 0.0633}
    },
    "legendary": {
        "star power": {1: 0.2717},
        "hypercharge": {1: 0.1630},
        "epic brawler": {1: 0.1087},
        "mythic brawler": {1: 0.0543},
        "legendary brawler": {1: 0.0217},
        "super rare skin": {1: 0.3587},
        "epic skin": {1: 0.0217}
    }
}

# Function to simulate opening a single drop
def open_starr_drop(rarity):
    reward_category = random.choices(list(rewards_probabilities[rarity].keys()), weights=[sum(d.values()) for d in rewards_probabilities[rarity].values()])[0]
    reward_value = random.choices(list(rewards_probabilities[rarity][reward_category].keys()), weights=list(rewards_probabilities[rarity][reward_category].values()))[0]
    return reward_category, reward_value

# Main simulation function
def simulate_starr_drops(num_drops):
    drop_counts = {rarity: 0 for rarity in rewards_probabilities}
    total_rewards = {
        "coins": 0,
        "power points": 0,
        "credits": 0,
        "bling": 0,
        "xp doubler": 0,
        "common pin": 0,
        "rare pin": 0,
        "epic pin": 0,
        "random spray": 0,
        "profile icon": 0,
        "rare brawler": 0,
        "super rare brawler": 0,
        "epic brawler": 0,
        "mythic brawler": 0,
        "legendary brawler": 0,
        "gadget": 0,
        "star power": 0,
        "hypercharge": 0,
        "rare skin": 0,
        "super rare skin": 0,
        "epic skin": 0,
    }

    for _ in range(num_drops):
        rarity = random.choices(list(rewards_probabilities.keys()), weights=[0.5, 0.28, 0.15, 0.05, 0.02])[0]
        drop_counts[rarity] += 1
        reward_category, reward_value = open_starr_drop(rarity)
        total_rewards[reward_category] += reward_value

    return drop_counts, total_rewards

# User input and simulation
num_drops = int(input("Enter the number of Starr Drops to open: "))
drop_counts, total_rewards = simulate_starr_drops(num_drops)

# Print out the drop counts
print("\nStarr Drop Counts:")
for rarity, count in drop_counts.items():
    if count > 0:
        print(f"{rarity.capitalize()} Drops: {count}")

# Print out the total rewards obtained, only showing categories where the reward was greater than 0
print("\nTotal rewards obtained:")
for reward, amount in total_rewards.items():
    if amount > 0:
        print(f"{reward.capitalize().replace('_', ' ')}: {amount}")