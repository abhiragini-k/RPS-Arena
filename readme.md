# 🪨📄✂️ RPS-Arena

**RPS-Arena** is a Python-based terminal game where players battle it out in the classic **Rock–Paper–Scissors** showdown. It supports multiple modes, series-based matches, difficulty levels, and an optional persistent leaderboard to track player progress.

---

## ✨ Features im currently working on

* 🎮 **Game Modes**:

  * Player vs CPU (Easy / Medium / Hard)
  * Player vs Player (local multiplayer)
* 🏆 **Arena Battles**: Play in best-of-3, 5, or 7 series.
* 🤖 **AI Opponents**:

  * **Easy** → Random moves
  * **Medium** → Counters your most frequent moves
  * **Hard** → Predicts your next move based on history
* 📊 **Leaderboard** (optional):

  * Tracks wins, losses, draws
  * Elo rating system for ranking
  * Saved in JSON for persistence
* ⚡ **Polished CLI**:

  * Clear instructions
  * Scoreboard display
  * Replay options

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/rps-arena.git
cd rps-arena
```

Run the game with:

```bash
python app.py
```

*(Requires Python 3.7+)*

---

## 🎯 How to Play(this is just a backend for now)

1. Choose a mode from the main menu:

   * **1** → Quick Match vs CPU
   * **2** → Local PvP
   * **3** → Show Leaderboard
   * **4** → Reset Leaderboard
   * **5** → Quit
2. Select series length (Best of 3 / 5 / 7).
3. Enter your move each round:

   * `r` → Rock 🪨
   * `p` → Paper 📄
   * `s` → Scissors ✂️
4. The game updates scores until someone wins the series.
5. Check your **Elo rating** on the leaderboard!

---

## 📖 Example Gameplay

```
===== RPS-Arena =====
1) Quick Match vs CPU
2) Local PvP
3) Show Leaderboard
4) Reset Leaderboard
5) Quit
Choose an option [1-5]: 1

Enter your player name: Abhi
Choose CPU difficulty:
1) Easy
2) Medium
3) Hard
Enter choice [1-3]: 2

Choose series length:
1) Best of 3
2) Best of 5
3) Best of 7
4) Best of n
Enter choice [1-3]: 1

--- Round 1 ---
Abhi, your move (r/p/s): r
CPU played: Scissors
You win this round!
Score: Abhi 1 - 0 CPU | Draws: 0
```


