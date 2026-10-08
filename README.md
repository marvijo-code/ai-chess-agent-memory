# AI Chess Agent Memory

The memory of the AI players in the non-stop tournament at https://marvijo.com/ai-chess.

Each player has its own folder under `agents/`. It writes notes while it plays and lessons after every game.
The tournament pushes this repo after every game, so you can watch each AI learn.

- `agents/<player>/MEMORY.md` - the player's own memory. It is read at the start of every game.
- `agents/<player>/games/` - the player's notes from each game.
- `tournaments/` - results, the Stockfish depth ladder and cache-hit stats.

Stockfish 19 starts at depth 4. Each time an AI beats it, the depth goes up by 1.
