# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0008-20261009-055507)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 263 | 2607057 | 1095424 | 42.0% | 41.7% |
| GPT-6.1 Sol | 212 | 5613079 | 5173888 | 92.2% | 92.6% |
| Sonnet 5.5 | 222 | 4785744 | 4573030 | 95.6% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2260 | 25099350 | 11396352 | 45.4% | 45.3% |
| GPT-6.1 Sol | 1832 | 53632458 | 50013440 | 93.3% | 93.7% |
| Sonnet 5.5 | 1967 | 44594158 | 42666519 | 95.7% | 96.2% |
