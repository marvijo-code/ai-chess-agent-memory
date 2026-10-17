# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).
- Lines: runs of 8+ consecutive moves in MEMORY.md (at most 6, none longer than 16 plies; a file over the limit must lose one line per reflection). Memory is for patterns, not long move sequences.

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Haiku 5.5: `agents/haiku/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0045-20261017-034241)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6 | 6 | 6 | 6 | 6 | 3 | 0 | 3 | 0 |
| GLM 5.3 Flash | 5 | 5 | 5 | 4 | 3 | 2 | 1 | 3 | 1 |
| GPT-6.1 Sol | 6 | 6 | 6 | 6 | 1 | 6 | 5 | 12 | 0 |
| Haiku 5.5 | 5 | 5 | 5 | 5 | 5 | 4 | 0 | 2 | 0 |
| Sonnet 5.5 | 6 | 6 | 6 | 6 | 5 | 2 | 1 | 4 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 168 | 168 | 168 | 162 | 160 | 204 | 4 | 84 | 5 |
| Fable 5.1 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 0 |
| GLM 5.3 Flash | 48 | 48 | 48 | 42 | 41 | 38 | 2 | 22 | 6 |
| GPT-6 Astra | 8 | 8 | 8 | 8 | 8 | 2 | 0 | 1 | 0 |
| GPT-6.1 Sol | 180 | 180 | 180 | 180 | 136 | 178 | 44 | 142 | 0 |
| Haiku 5.5 | 13 | 13 | 13 | 13 | 13 | 13 | 0 | 3 | 0 |
| Sonnet 5.5 | 178 | 178 | 177 | 178 | 177 | 129 | 1 | 60 | 0 |

## Memory shape now

| Player | Lines in MEMORY.md | Longest run (plies) | Over the ply cap |
| --- | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6 | 16 | 0 |
| GLM 5.3 Flash | 5 | 14 | 0 |
| GPT-6.1 Sol | 1 | 8 | 0 |
| Haiku 5.5 | 3 | 13 | 0 |
| Sonnet 5.5 | 3 | 13 | 0 |
