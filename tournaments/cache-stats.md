# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0029-20261011-130205)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 253 | 2585160 | 1447424 | 56.0% | 56.0% |
| GPT-6.1 Sol | 150 | 3134631 | 2791168 | 89.0% | 90.2% |
| Sonnet 5.5 | 149 | 2447534 | 2286380 | 93.4% | 94.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7824 | 87386367 | 44790272 | 51.3% | 51.2% |
| GPT-6.1 Sol | 6226 | 180624599 | 168202368 | 93.1% | 93.6% |
| Sonnet 5.5 | 6375 | 139362080 | 132995450 | 95.4% | 96.1% |
