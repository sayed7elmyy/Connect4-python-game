
# 🧩 Connect 4 Game – AI-Powered (Python + Pygame)

An interactive, customizable version of the classic Connect 4 game built in Python using Pygame. This game includes AI opponents with three difficulty levels, unique themes, and dynamic visual feedback for wins and draws.

---

## 📌 Overview

This project implements:
- A graphical interface using Pygame
- AI with 3 difficulty levels:
  - Easy: Random moves
  - Medium: Heuristic strategy (blocks/wins)
  - Hard: Minimax algorithm with Alpha-Beta pruning
- Theme customization (Classic, Space, Neon)
- Visual win/draw indicators
- Restart game option after result

---

## 🎮 Features

- **Player vs AI gameplay**
- **Difficulty Levels**:
  - **Easy** – Random column selection
  - **Medium** – Rule-based AI (blocks & wins)
  - **Hard** – Minimax with Alpha-Beta pruning
- **Custom Themes** – Classic, Space, Neon
- **Interactive UI** – Rendered via Pygame
- **Win/Draw Detection** – Highlights results
- **Restart Functionality**

---

## 🧠 AI Strategy

### Easy (Random)
- Picks a random column from valid moves
- No logic involved

### Medium (Heuristic)
- Detects and blocks potential player wins
- Attempts to win when possible
- Uses scoring logic for basic strategy

### Hard (Minimax + Alpha-Beta)
- Evaluates game tree to a certain depth
- Considers both AI and player best options
- Alpha-Beta pruning optimizes performance

---

## 🧩 Key Functions

- `create_board()` – Initializes 6x7 game board
- `winning_move(board, piece)` – Checks for wins
- `draw_board()` – Renders UI and highlights
- `ai_move_easy()`, `ai_move_medium()` – AI logic
- `minimax()` – Advanced move decision making
- `display_winner()` – Result and restart handler

---

## 📦 Requirements

- **Python 3.x**
- **Libraries**:
  - `pygame`
  - `numpy`

Install dependencies with:
```bash
pip install pygame numpy
```

---

## ▶️ Running the Game

1. Run the game with:
```bash
python connect4.py
```
2. Choose theme and difficulty.
3. Play against the AI.
4. Restart after each game if desired.

---

## 👨‍💻 Authors

- Sayed Helmy
- Eyad Ahmed Mazhar
- Mahmoud Waleed
- Omar Hesham Mohamed

---
