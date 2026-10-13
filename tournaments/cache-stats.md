# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0038-20261013-003046)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 139 | 2268390 | 2110976 | 93.1% | 93.8% |
| GLM 5.3 Flash | 106 | 1877412 | 1579520 | 84.1% | 85.3% |
| GPT-6.1 Sol | 94 | 2384192 | 2133504 | 89.5% | 90.9% |
| Sonnet 5.5 | 76 | 1579027 | 1478557 | 93.6% | 95.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9471 | 111905210 | 64100352 | 57.3% | 57.3% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 778 | 12665319 | 11220416 | 88.6% | 89.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8279 | 248340752 | 231317376 | 93.1% | 93.6% |
| Sonnet 5.5 | 8389 | 194516712 | 185970850 | 95.6% | 96.3% |
