# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).
- Lines: runs of 8+ consecutive moves in MEMORY.md (at most 6, none longer than 16 plies; a file over the limit must lose one line per reflection). Memory is for patterns, not long move sequences.

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, DeepSeek V4.1 Flash 1017: `agents/deepseek1017/`, GLM 5.3 Flash: `agents/glm/`

## Current tournament (aichess-0056-20261021-191525)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| DeepSeek V4.1 Flash 1017 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 208 | 208 | 208 | 201 | 198 | 211 | 5 | 94 | 6 |
| DeepSeek V4.1 Flash 1017 | 42 | 42 | 42 | 41 | 41 | 30 | 1 | 19 | 1 |
| Fable 5.1 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 0 |
| GLM 5.3 Flash | 85 | 85 | 85 | 67 | 63 | 53 | 5 | 41 | 18 |
| GPT-6 Astra | 8 | 8 | 8 | 8 | 8 | 2 | 0 | 1 | 0 |
| GPT-6.1 Sol | 181 | 181 | 181 | 181 | 137 | 179 | 44 | 144 | 0 |
| Haiku 5.5 | 14 | 14 | 13 | 14 | 14 | 14 | 0 | 3 | 0 |
| Sonnet 5.5 | 181 | 181 | 180 | 181 | 178 | 129 | 3 | 65 | 0 |

## Memory shape now

| Player | Lines in MEMORY.md | Longest run (plies) | Over the ply cap |
| --- | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6 | 16 | 0 |
| DeepSeek V4.1 Flash 1017 | 5 | 16 | 0 |
| GLM 5.3 Flash | 6 | 15 | 0 |
