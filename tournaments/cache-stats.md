# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0007-20261009-031124)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 32 | 253689 | 106240 | 41.9% | 41.5% |
| GPT-6.1 Sol | 26 | 497175 | 433664 | 87.2% | 89.9% |
| Sonnet 5.5 | 25 | 334680 | 307472 | 91.9% | 93.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1736 | 19333223 | 8940416 | 46.2% | 46.2% |
| GPT-6.1 Sol | 1400 | 40763874 | 38033024 | 93.3% | 93.8% |
| Sonnet 5.5 | 1567 | 36134882 | 34601083 | 95.8% | 96.3% |
