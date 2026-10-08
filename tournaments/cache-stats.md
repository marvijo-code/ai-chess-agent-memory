# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0002-20261008-140326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 107 | 1139381 | 509824 | 44.7% | 44.6% |
| GPT-6.1 Sol | 59 | 1301004 | 1216128 | 93.5% | 94.3% |
| Sonnet 5.5 | 88 | 2244782 | 2160513 | 96.2% | 96.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 344 | 3475479 | 1786496 | 51.4% | 51.5% |
| GPT-6.1 Sol | 361 | 10855018 | 10120192 | 93.2% | 93.5% |
| Sonnet 5.5 | 357 | 7850462 | 7522318 | 95.8% | 96.3% |
