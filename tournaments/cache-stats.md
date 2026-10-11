# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0028-20261011-102906)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 153 | 2179336 | 1516544 | 69.6% | 69.7% |
| GPT-6.1 Sol | 135 | 5621771 | 5390464 | 95.9% | 96.0% |
| Sonnet 5.5 | 74 | 1561513 | 1485598 | 95.1% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7415 | 83225796 | 42562048 | 51.1% | 51.1% |
| GPT-6.1 Sol | 5966 | 174848497 | 163004672 | 93.2% | 93.7% |
| Sonnet 5.5 | 6108 | 134578261 | 128490318 | 95.5% | 96.1% |
