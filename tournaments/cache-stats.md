# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0017-20261010-051708)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 209 | 2601936 | 1554432 | 59.7% | 59.9% |
| GPT-6.1 Sol | 132 | 3073397 | 2754688 | 89.6% | 89.9% |
| Sonnet 5.5 | 168 | 3482221 | 3315591 | 95.2% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4356 | 47761259 | 22732800 | 47.6% | 47.5% |
| GPT-6.1 Sol | 3641 | 104610165 | 97065728 | 92.8% | 93.3% |
| Sonnet 5.5 | 3843 | 84550327 | 80731954 | 95.5% | 96.1% |
