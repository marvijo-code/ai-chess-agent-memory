# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0007-20261009-031124)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 293 | 3412759 | 1466752 | 43.0% | 42.9% |
| GPT-6.1 Sol | 246 | 7752680 | 7240192 | 93.4% | 93.8% |
| Sonnet 5.5 | 203 | 4008212 | 3799878 | 94.8% | 95.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1997 | 22492293 | 10300928 | 45.8% | 45.7% |
| GPT-6.1 Sol | 1620 | 48019379 | 44839552 | 93.4% | 93.8% |
| Sonnet 5.5 | 1745 | 39808414 | 38093489 | 95.7% | 96.2% |
