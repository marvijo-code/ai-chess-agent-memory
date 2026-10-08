# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0002-20261008-140326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 107 | 1139381 | 509824 | 44.7% | 44.6% |
| GPT-6.1 Sol | 65 | 1458377 | 1345920 | 92.3% | 93.0% |
| Sonnet 5.5 | 94 | 2363911 | 2273727 | 96.2% | 96.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 344 | 3475479 | 1786496 | 51.4% | 51.5% |
| GPT-6.1 Sol | 367 | 11012391 | 10249984 | 93.1% | 93.4% |
| Sonnet 5.5 | 363 | 7969591 | 7635532 | 95.8% | 96.3% |
