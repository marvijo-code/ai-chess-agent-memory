# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0010-20261009-112258)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 54 | 600404 | 271744 | 45.3% | 45.1% |
| GPT-6.1 Sol | 32 | 663141 | 602240 | 90.8% | 91.9% |
| Sonnet 5.5 | 22 | 272897 | 248961 | 91.2% | 93.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2501 | 27505606 | 12456192 | 45.3% | 45.2% |
| GPT-6.1 Sol | 2108 | 62734761 | 58422784 | 93.1% | 93.6% |
| Sonnet 5.5 | 2213 | 49656886 | 47477091 | 95.6% | 96.2% |
