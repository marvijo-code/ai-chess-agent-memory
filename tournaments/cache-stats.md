# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0010-20261009-112258)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 85 | 838204 | 360320 | 43.0% | 42.8% |
| GPT-6.1 Sol | 57 | 1132473 | 1027072 | 90.7% | 91.5% |
| Sonnet 5.5 | 47 | 597748 | 547102 | 91.5% | 93.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2532 | 27743406 | 12544768 | 45.2% | 45.1% |
| GPT-6.1 Sol | 2133 | 63204093 | 58847616 | 93.1% | 93.5% |
| Sonnet 5.5 | 2238 | 49981737 | 47775232 | 95.6% | 96.1% |
