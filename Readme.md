# Py Cronicles

A 2D top-down RPG inspired by the classic *The Legend of Zelda*, built with Python and Pygame. Final project for the Object-Oriented Programming component of the Python Programming course (IEFP).

## Concept

The player wakes up in a dark, gloomy forest with no memory of the world around them. While exploring, they gradually discover three factions in conflict, each with its own goal:

- **Druids**: guardians of nature, initially peaceful, who escalate to hostility as ecological destruction grows.
- **Corrupted**: victims of a curse spreading from the mountains in the north, slowly falling from lucidity into full hostility.
- **Exiles**: a people banished from their own city, now sealed off, gathering resources to force their way back in.

The player can observe, intervene, or choose to side with one of the factions. The game ends when a faction achieves its goal, or when the player achieves their own, alone.

## Main Features

- **Explorable world** with a scrolling camera, built from tiles (Tiled Map Editor)
- **Faction system** with independent progression phases that influence one another
- **Branching dialogue**, with options unlocked by the knowledge the player has accumulated
- **Survival mechanics**: hunger and energy, with consequences for the player
- **Resource gathering** (e.g. mushrooms, with edible and poisonous variants) and an inventory
- **Basic combat**, with NPCs reacting according to the state of their faction
- **Autonomous NPCs** with movement behavior and obstacle detection

## Tech Stack

- **Python 3.13**
- **Pygame**: rendering engine and game loop
- **Tiled Map Editor**: map building, plus collision, pickup and point-of-interest layers
- **PyTMX**: loading the maps exported from Tiled

## Architecture (OOP Highlights)

- Character hierarchy (`Character` → `Player`, `NPC`) with shared base attributes and behavior, specialized per subclass
- A `Faction` class per faction, each with its own phase-advancement logic (polymorphism)
- Item hierarchy (`Item` → `Food`, ...) with a polymorphic `use()` method, where each subtype defines its own effect
- Separation between world data (Tiled) and game logic (Python)

## How to Run

```bash
pip install -r requirements.txt
python main.py
```

## Author

Rui · [GitHub](https://github.com/rmas96/py-chronicles) · built as part of the IEFP training in Python Programming.