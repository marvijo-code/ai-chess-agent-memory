# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0009-20261009-081556)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 172 | 1575932 | 696960 | 44.2% | 44.2% |
| GPT-6.1 Sol | 236 | 8203945 | 7628928 | 93.0% | 93.5% |
| Sonnet 5.5 | 194 | 4309174 | 4113217 | 95.5% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2432 | 26675282 | 12093312 | 45.3% | 45.2% |
| GPT-6.1 Sol | 2068 | 61836403 | 57642368 | 93.2% | 93.7% |
| Sonnet 5.5 | 2161 | 48903332 | 46779736 | 95.7% | 96.2% |
