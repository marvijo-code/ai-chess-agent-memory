# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).
- Lines: runs of 8+ consecutive moves in MEMORY.md (at most 6, none longer than 16 plies; a file over the limit must lose one line per reflection). Memory is for patterns, not long move sequences.

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0039-20261013-051801)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6 | 6 | 6 | 5 | 5 | 3 | 0 | 2 | 0 |
| GLM 5.3 Flash | 4 | 4 | 4 | 4 | 4 | 3 | 1 | 3 | 0 |
| GPT-6.1 Sol | 6 | 6 | 6 | 5 | 0 | 5 | 5 | 10 | 0 |
| Sonnet 5.5 | 6 | 6 | 6 | 6 | 6 | 4 | 0 | 3 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 139 | 139 | 139 | 133 | 132 | 185 | 3 | 68 | 4 |
| Fable 5.1 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 0 |
| GLM 5.3 Flash | 25 | 25 | 25 | 25 | 25 | 24 | 1 | 9 | 0 |
| GPT-6 Astra | 8 | 8 | 8 | 8 | 8 | 2 | 0 | 1 | 0 |
| GPT-6.1 Sol | 148 | 148 | 148 | 147 | 121 | 146 | 26 | 89 | 0 |
| Sonnet 5.5 | 146 | 146 | 145 | 146 | 146 | 118 | 0 | 42 | 0 |

## Memory shape now

| Player | Lines in MEMORY.md | Longest run (plies) | Over the ply cap |
| --- | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6 | 16 | 0 |
| GLM 5.3 Flash | 3 | 8 | 0 |
| GPT-6.1 Sol | 2 | 8 | 0 |
| Sonnet 5.5 | 2 | 9 | 0 |
