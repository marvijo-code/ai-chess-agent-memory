# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0029-20261011-130205)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 227 | 2204739 | 1198592 | 54.4% | 54.4% |
| GPT-6.1 Sol | 135 | 2702455 | 2408064 | 89.1% | 90.5% |
| Sonnet 5.5 | 149 | 2447534 | 2286380 | 93.4% | 94.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7798 | 87005946 | 44541440 | 51.2% | 51.1% |
| GPT-6.1 Sol | 6211 | 180192423 | 167819264 | 93.1% | 93.6% |
| Sonnet 5.5 | 6375 | 139362080 | 132995450 | 95.4% | 96.1% |
