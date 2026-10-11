# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0030-20261011-145519)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 109 | 952656 | 434688 | 45.6% | 45.2% |
| GPT-6.1 Sol | 139 | 4680702 | 4369024 | 93.3% | 93.7% |
| Sonnet 5.5 | 103 | 2255804 | 2149516 | 95.3% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7933 | 88339023 | 45224960 | 51.2% | 51.1% |
| GPT-6.1 Sol | 6365 | 185305301 | 172571392 | 93.1% | 93.6% |
| Sonnet 5.5 | 6478 | 141617884 | 135144966 | 95.4% | 96.1% |
