# 🕹️ SayCaster - A Raycasting Engine Inspired by DOOM and Wolfenstein 3D


SayCaster is a basic 2D raycasting engine written in Python using Pygame. It renders a pseudo-3D environment based on a tile map made up of 2D Array — similar to the early FPS games like DOOM and Wolfenstein 3D.

## 📸 Preview

> ![SayCaster Demo](\preview.gif) 

---

## 🧠 Concepts Learned

- Raycasting fundamentals
- Converting 2D grid data into a 3D projection
- Angle normalization and vector math
- Collision detection using grid indexing
- Python classes, modular design (`map.py`, `ray.py`, `engine.py`)
- 2D to 3D projection via fisheye correction
- Creating a minimap overlay and directional indicators
- Pygame rendering loop and framerate control

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.8+
- Pygame

### 📦 Setup

1. Clone the repo:
```bash
git clone https://github.com/yourusername/saycaster.git
cd saycaster
````

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the game:

```bash
python engine.py
```

---

## 🎮 Controls

| Key     | Action        |
| ------- | ------------- |
| `W / ↑` | Move forward  |
| `S / ↓` | Move backward |
| `A / ←` | Turn left     |
| `D / →` | Turn right    |
| `Esc`   | Quit game     |

---

## 📁 Project Structures

```
saycaster/
├── engine.py         # Main game loop and rendering
├── map.py            # 2D tile-based map and minimap drawing
├── ray.py            # Raycasting logic
├── requirements.txt  # Python dependencies
├── .gitignore
└── README.md
```

---

## 🌈 TODOs & Future Ideas

* Implement DDA Algorithm
* Add textured walls using ray hit logic
* Implement enemies / NPCs
* Add sound effects and gunfire
* WebGL/Three.js port (for web hosting)
* Add mouse support for turning

---

## 🧠 Inspiration

* [DOOM](https://doom.fandom.com/wiki/DOOM)
* [Wolfenstein 3D](https://wolfenstein.fandom.com/wiki/Wolfenstein_3D)
* [Weird Devers RayCasting Explanation](https://youtu.be/g8p7nAbDz6Y?feature=shared)
---

## 🛡️ License

MIT — free to use, remix, and learn from.

---

> Made by Yours Truly [Sandeep Nautiyal](https://github.com/Sandeep-Naughtyal)

```

---

```
