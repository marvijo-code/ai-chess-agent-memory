# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).
- Lines: runs of 8+ consecutive moves in MEMORY.md (at most 6, none longer than 16 plies; a file over the limit must lose one line per reflection). Memory is for patterns, not long move sequences.

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0040-20261013-090848)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2 | 2 | 2 | 2 | 2 | 2 | 0 | 0 | 0 |
| GLM 5.3 Flash | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| GPT-6.1 Sol | 2 | 2 | 2 | 2 | 0 | 2 | 2 | 4 | 0 |
| Sonnet 5.5 | 2 | 2 | 2 | 2 | 2 | 1 | 0 | 2 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 141 | 141 | 141 | 136 | 135 | 188 | 3 | 69 | 4 |
| Fable 5.1 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 0 |
| GLM 5.3 Flash | 26 | 26 | 26 | 26 | 26 | 25 | 1 | 9 | 0 |
| GPT-6 Astra | 8 | 8 | 8 | 8 | 8 | 2 | 0 | 1 | 0 |
| GPT-6.1 Sol | 150 | 150 | 150 | 150 | 121 | 149 | 29 | 95 | 0 |
| Sonnet 5.5 | 148 | 148 | 147 | 148 | 148 | 119 | 0 | 44 | 0 |

## Memory shape now

| Player | Lines in MEMORY.md | Longest run (plies) | Over the ply cap |
| --- | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6 | 16 | 0 |
| GLM 5.3 Flash | 3 | 8 | 0 |
| GPT-6.1 Sol | 2 | 8 | 0 |
| Sonnet 5.5 | 3 | 10 | 0 |
