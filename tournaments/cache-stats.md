# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0010-20261009-112258)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 211 | 1987511 | 748416 | 37.7% | 37.2% |
| GPT-6.1 Sol | 256 | 7549930 | 7016192 | 92.9% | 93.3% |
| Sonnet 5.5 | 171 | 3305611 | 3128826 | 94.7% | 95.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2658 | 28892713 | 12932864 | 44.8% | 44.6% |
| GPT-6.1 Sol | 2332 | 69621550 | 64836736 | 93.1% | 93.6% |
| Sonnet 5.5 | 2362 | 52689600 | 50356956 | 95.6% | 96.1% |
