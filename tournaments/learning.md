# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).
- Lines: runs of 8+ consecutive moves in MEMORY.md (at most 6, none longer than 16 plies; a file over the limit must lose one line per reflection). Memory is for patterns, not long move sequences.

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, Muse Spark 1.3: `agents/muse/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0079-20261102-080217)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6 | 6 | 6 | 6 | 6 | 4 | 1 | 7 | 0 |
| GLM 5.3 Flash | 4 | 4 | 4 | 2 | 2 | 0 | 0 | 3 | 2 |
| Muse Spark 1.3 | 6 | 6 | 6 | 6 | 6 | 3 | 0 | 1 | 0 |
| Sonnet 5.5 | 7 | 7 | 7 | 7 | 6 | 1 | 1 | 3 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 310 | 310 | 310 | 301 | 298 | 272 | 6 | 140 | 8 |
| DeepSeek V4.1 Flash 1017 | 79 | 79 | 79 | 78 | 78 | 41 | 1 | 26 | 1 |
| Fable 5.1 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 0 |
| GLM 5.3 Flash | 181 | 181 | 181 | 145 | 140 | 137 | 15 | 104 | 36 |
| GPT-6 Astra | 8 | 8 | 8 | 8 | 8 | 2 | 0 | 1 | 0 |
| GPT-6.1 Sol | 181 | 181 | 181 | 181 | 137 | 179 | 44 | 144 | 0 |
| Haiku 5.5 | 17 | 17 | 16 | 17 | 17 | 18 | 0 | 4 | 0 |
| Muse Spark 1.3 | 63 | 63 | 63 | 63 | 63 | 41 | 0 | 17 | 0 |
| Sonnet 5.5 | 230 | 230 | 229 | 230 | 224 | 146 | 6 | 95 | 0 |

## Memory shape now

| Player | Lines in MEMORY.md | Longest run (plies) | Over the ply cap |
| --- | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 5 | 16 | 0 |
| GLM 5.3 Flash | 1 | 9 | 0 |
| Muse Spark 1.3 | 2 | 10 | 0 |
| Sonnet 5.5 | 6 | 16 | 0 |
