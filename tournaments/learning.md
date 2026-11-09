# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).
- Lines: runs of 8+ consecutive moves in MEMORY.md (at most 6, none longer than 16 plies; a file over the limit must lose one line per reflection). Memory is for patterns, not long move sequences.

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, Muse Spark 1.3: `agents/muse/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0088-20261109-135130)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4 | 4 | 4 | 4 | 4 | 3 | 0 | 3 | 0 |
| GLM 5.3 Flash | 2 | 2 | 2 | 2 | 2 | 1 | 0 | 0 | 0 |
| Muse Spark 1.3 | 2 | 2 | 2 | 2 | 2 | 1 | 0 | 0 | 0 |
| Sonnet 5.5 | 3 | 3 | 3 | 3 | 2 | 3 | 1 | 5 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 361 | 361 | 361 | 352 | 349 | 305 | 7 | 173 | 8 |
| DeepSeek V4.1 Flash 1017 | 79 | 79 | 79 | 78 | 78 | 41 | 1 | 26 | 1 |
| Fable 5.1 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 0 |
| GLM 5.3 Flash | 220 | 220 | 220 | 181 | 176 | 171 | 23 | 140 | 39 |
| GPT-6 Astra | 8 | 8 | 8 | 8 | 8 | 2 | 0 | 1 | 0 |
| GPT-6.1 Sol | 181 | 181 | 181 | 181 | 137 | 179 | 44 | 144 | 0 |
| Haiku 5.5 | 17 | 17 | 16 | 17 | 17 | 18 | 0 | 4 | 0 |
| Muse Spark 1.3 | 112 | 112 | 112 | 112 | 112 | 55 | 0 | 31 | 0 |
| Sonnet 5.5 | 276 | 276 | 275 | 276 | 263 | 163 | 13 | 142 | 0 |

## Memory shape now

| Player | Lines in MEMORY.md | Longest run (plies) | Over the ply cap |
| --- | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6 | 16 | 0 |
| GLM 5.3 Flash | 6 | 16 | 0 |
| Muse Spark 1.3 | 2 | 15 | 0 |
| Sonnet 5.5 | 6 | 16 | 0 |
