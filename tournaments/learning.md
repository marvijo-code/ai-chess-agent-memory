# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).
- Lines: runs of 8+ consecutive moves in MEMORY.md (at most 6, none longer than 16 plies; a file over the limit must lose one line per reflection). Memory is for patterns, not long move sequences.

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, Muse Spark 1.3: `agents/muse/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0089-20261109-210352)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4 | 4 | 4 | 4 | 4 | 2 | 0 | 4 | 0 |
| GLM 5.3 Flash | 3 | 3 | 3 | 3 | 3 | 3 | 1 | 5 | 0 |
| Sonnet 5.5 | 3 | 3 | 3 | 3 | 3 | 1 | 0 | 2 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 367 | 367 | 367 | 358 | 355 | 307 | 8 | 180 | 8 |
| DeepSeek V4.1 Flash 1017 | 79 | 79 | 79 | 78 | 78 | 41 | 1 | 26 | 1 |
| Fable 5.1 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 0 |
| GLM 5.3 Flash | 227 | 227 | 227 | 188 | 183 | 177 | 24 | 148 | 39 |
| GPT-6 Astra | 8 | 8 | 8 | 8 | 8 | 2 | 0 | 1 | 0 |
| GPT-6.1 Sol | 181 | 181 | 181 | 181 | 137 | 179 | 44 | 144 | 0 |
| Haiku 5.5 | 17 | 17 | 16 | 17 | 17 | 18 | 0 | 4 | 0 |
| Muse Spark 1.3 | 114 | 114 | 114 | 114 | 114 | 57 | 0 | 32 | 0 |
| Sonnet 5.5 | 282 | 282 | 281 | 282 | 269 | 165 | 13 | 147 | 0 |

## Memory shape now

| Player | Lines in MEMORY.md | Longest run (plies) | Over the ply cap |
| --- | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5 | 16 | 0 |
| GLM 5.3 Flash | 6 | 15 | 0 |
| Muse Spark 1.3 | 4 | 15 | 0 |
| Sonnet 5.5 | 6 | 16 | 0 |
