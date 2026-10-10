# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0017-20261010-051708)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 306 | 3625855 | 2144768 | 59.2% | 59.3% |
| GPT-6.1 Sol | 160 | 3828449 | 3463296 | 90.5% | 90.9% |
| Sonnet 5.5 | 196 | 4047374 | 3853617 | 95.2% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4453 | 48785178 | 23323136 | 47.8% | 47.7% |
| GPT-6.1 Sol | 3669 | 105365217 | 97774336 | 92.8% | 93.3% |
| Sonnet 5.5 | 3871 | 85115480 | 81269980 | 95.5% | 96.1% |
