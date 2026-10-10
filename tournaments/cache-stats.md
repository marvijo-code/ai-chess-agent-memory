# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0014-20261009-214817)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 293 | 3095904 | 1555712 | 50.3% | 50.4% |
| GPT-6.1 Sol | 230 | 6844108 | 6454528 | 94.3% | 94.6% |
| Sonnet 5.5 | 207 | 4232830 | 4025638 | 95.1% | 95.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3607 | 39135839 | 18119424 | 46.3% | 46.2% |
| GPT-6.1 Sol | 3130 | 91617791 | 85127168 | 92.9% | 93.4% |
| Sonnet 5.5 | 3294 | 73622958 | 70353782 | 95.6% | 96.1% |
