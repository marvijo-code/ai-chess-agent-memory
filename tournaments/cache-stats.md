# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0010-20261009-112258)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 167 | 1562970 | 606592 | 38.8% | 38.4% |
| GPT-6.1 Sol | 176 | 5301746 | 4917632 | 92.8% | 93.2% |
| Sonnet 5.5 | 110 | 1671113 | 1550845 | 92.8% | 94.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2614 | 28468172 | 12791040 | 44.9% | 44.8% |
| GPT-6.1 Sol | 2252 | 67373366 | 62738176 | 93.1% | 93.5% |
| Sonnet 5.5 | 2301 | 51055102 | 48778975 | 95.5% | 96.1% |
