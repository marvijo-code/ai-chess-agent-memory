# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0038-20261013-003046)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 133 | 2148177 | 1993856 | 92.8% | 93.6% |
| GLM 5.3 Flash | 106 | 1877412 | 1579520 | 84.1% | 85.3% |
| GPT-6.1 Sol | 87 | 2124286 | 1921536 | 90.5% | 92.1% |
| Sonnet 5.5 | 76 | 1579027 | 1478557 | 93.6% | 95.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9465 | 111784997 | 63983232 | 57.2% | 57.2% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 778 | 12665319 | 11220416 | 88.6% | 89.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8272 | 248080846 | 231105408 | 93.2% | 93.7% |
| Sonnet 5.5 | 8389 | 194516712 | 185970850 | 95.6% | 96.3% |
