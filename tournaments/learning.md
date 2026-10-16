# Learning check

Each AI player writes only to its own folder (`agents/<folder>/`) and reads every other folder.

- Read in prompt: games where every move request carried the player's MEMORY.md (fingerprint sent by the engine).
- Read latest: games that started with the exact MEMORY.md the player wrote after its previous game.
- Memory / note updates: reflections that changed MEMORY.md / a notes file. Rejected: edits over a cap or outside the player's folder (the player gets one retry to shorten them).
- Lines: runs of 8+ consecutive moves in MEMORY.md (at most 6, none longer than 16 plies; a file over the limit must lose one line per reflection). Memory is for patterns, not long move sequences.

Folders: DeepSeek V4.1 Flash: `agents/deepseek/`, GLM 5.3 Flash: `agents/glm/`, GPT-6.1 Sol: `agents/gpt/`, Sonnet 5.5: `agents/claude/`

## Current tournament (aichess-0041-20261013-124210)

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6 | 6 | 6 | 5 | 5 | 2 | 0 | 2 | 1 |
| GLM 5.3 Flash | 4 | 4 | 4 | 4 | 4 | 4 | 0 | 2 | 0 |
| GPT-6.1 Sol | 7 | 7 | 7 | 7 | 3 | 7 | 4 | 10 | 0 |
| Sonnet 5.5 | 7 | 7 | 7 | 7 | 7 | 1 | 0 | 4 | 0 |

## All tournaments since this check started

| Player | Games | Read in prompt | Read latest | Reflections | MEMORY.md updates | Note updates | Rejected | Retries | Errors |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 151 | 151 | 151 | 145 | 144 | 193 | 3 | 73 | 5 |
| Fable 5.1 | 5 | 5 | 5 | 5 | 5 | 5 | 0 | 0 | 0 |
| GLM 5.3 Flash | 33 | 33 | 33 | 33 | 33 | 33 | 1 | 13 | 0 |
| GPT-6 Astra | 8 | 8 | 8 | 8 | 8 | 2 | 0 | 1 | 0 |
| GPT-6.1 Sol | 161 | 161 | 161 | 161 | 128 | 160 | 33 | 109 | 0 |
| Sonnet 5.5 | 160 | 160 | 159 | 160 | 160 | 125 | 0 | 51 | 0 |

## Memory shape now

| Player | Lines in MEMORY.md | Longest run (plies) | Over the ply cap |
| --- | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6 | 16 | 0 |
| GLM 5.3 Flash | 5 | 15 | 0 |
| GPT-6.1 Sol | 1 | 8 | 0 |
| Sonnet 5.5 | 2 | 12 | 0 |
