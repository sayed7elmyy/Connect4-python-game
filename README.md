Here’s a professional and GitHub-ready **`README.md` file** for your **Connect 4 Python Game** project:

---

````markdown
# 🧩 Connect 4 Game – AI-Powered (Python + Pygame)

A visually engaging, AI-powered version of the classic **Connect 4 game**, built using **Python** and **Pygame**. The game supports multiple difficulty levels powered by distinct AI strategies, customizable themes, and intuitive game interaction.

---

## 🎮 Features

- **Human vs AI gameplay**
- **3 Difficulty Levels**:
  - *Easy*: Random column selection
  - *Medium*: Heuristic-based blocking and winning strategy
  - *Hard*: Advanced Minimax algorithm with Alpha-Beta pruning
- **Custom Themes**: Classic, Space, and Neon
- **Win/Draw Detection**: Visually highlights winning tiles and detects draws
- **Restart Option**: Easily restart the game from the result screen

---

## 🧠 AI Strategies

### 🟢 Easy
```python
def ai_move_easy(board):
    valid_columns = [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]
    return random.choice(valid_columns)
````

* Picks a random valid column.
* No strategic depth.

### 🟡 Medium

* Blocks the player’s winning moves.
* Tries to create immediate wins.
* Uses basic heuristics for decision-making.

### 🔴 Hard (Minimax + Alpha-Beta Pruning)

* Recursive game-tree search up to a certain depth.
* Optimizes AI moves while countering the player's best options.
* **Alpha-Beta pruning** reduces computational overhead.

---

## 🎨 Themes and UI

* Switch between **Classic**, **Space**, and **Neon** color themes.
* Winning tiles are highlighted visually.
* Game board is drawn dynamically using Pygame’s rendering capabilities.

---

## 📄 Code Structure Highlights

### Board Initialization

```python
def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT), int)
```

Creates an empty 6x7 game board using NumPy.

### Win Detection

```python
def winning_move(board, piece):
    # Horizontal, vertical, and diagonal win detection logic
```

### Drawing the Board

```python
def draw_board(board, PLAYER_COLOR, AI_COLOR, WINNING_COLOR, winning_tiles=None):
    # Uses Pygame to render board and pieces, highlighting winning tiles
```

### Restart Mechanism

```python
def display_winner(winner):
    # Displays winner and renders a restart button
```

---

## 💻 Requirements

* **Python 3.x**
* **Libraries**:

  * `numpy`
  * `pygame`

Install dependencies via pip:

```bash
pip install numpy pygame
```

---

## ▶️ How to Run

1. Clone or download the repository.
2. Run the script:

   ```bash
   python connect4.py
   ```
3. Choose a theme and difficulty level.
4. Play against the AI and restart as needed.

---

## 👨‍💻 Developed By

* **Sayed Helmy**
* **Eyad Ahmed Mazhar**
* **Mahmoud Waleed**
* **Omar Hesham Mohamed**

---

Enjoy the game and feel free to contribute or raise issues!

```
