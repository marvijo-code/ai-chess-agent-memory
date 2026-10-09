# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0009-20261009-081556)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 47 | 342103 | 142208 | 41.6% | 40.7% |
| GPT-6.1 Sol | 117 | 4496204 | 4180864 | 93.0% | 93.4% |
| Sonnet 5.5 | 63 | 1223363 | 1155105 | 94.4% | 95.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2307 | 25441453 | 11538560 | 45.4% | 45.2% |
| GPT-6.1 Sol | 1949 | 58128662 | 54194304 | 93.2% | 93.7% |
| Sonnet 5.5 | 2030 | 45817521 | 43821624 | 95.6% | 96.2% |
