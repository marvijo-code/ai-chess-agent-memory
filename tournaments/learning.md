# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).
- Lines: runs of 8+ consecutive moves in MEMORY.md (at most 6, none longer than 16 plies; a file over the limit must lose one line per reflection). Memory is for patterns, not long move sequences.

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Haiku 5.5: `agents/haiku/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0044-20261016-161517)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4 | 4 | 4 | 4 | 4 | 2 | 0 | 1 | 0 |
| GLM 5.3 Flash | 4 | 4 | 4 | 2 | 2 | 0 | 0 | 1 | 2 |
| GPT-6.1 Sol | 4 | 4 | 4 | 4 | 2 | 3 | 2 | 6 | 0 |
| Haiku 5.5 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 0 |
| Sonnet 5.5 | 4 | 4 | 4 | 4 | 4 | 1 | 0 | 1 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 161 | 161 | 161 | 155 | 153 | 200 | 4 | 79 | 5 |
| Fable 5.1 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 0 |
| GLM 5.3 Flash | 42 | 42 | 42 | 37 | 37 | 35 | 1 | 17 | 5 |
| GPT-6 Astra | 8 | 8 | 8 | 8 | 8 | 2 | 0 | 1 | 0 |
| GPT-6.1 Sol | 171 | 171 | 171 | 171 | 133 | 169 | 38 | 125 | 0 |
| Haiku 5.5 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 0 |
| Sonnet 5.5 | 168 | 168 | 167 | 168 | 168 | 127 | 0 | 53 | 0 |

## Memory shape now

| Player | Lines in MEMORY.md | Longest run (plies) | Over the ply cap |
| --- | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6 | 16 | 0 |
| GLM 5.3 Flash | 6 | 15 | 0 |
| GPT-6.1 Sol | 1 | 8 | 0 |
| Haiku 5.5 | 5 | 16 | 0 |
| Sonnet 5.5 | 5 | 12 | 0 |
