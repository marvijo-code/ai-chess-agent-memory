# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0038-20261013-003046)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 139 | 2268390 | 2110976 | 93.1% | 93.8% |
| GLM 5.3 Flash | 136 | 2267016 | 1903360 | 84.0% | 84.9% |
| GPT-6.1 Sol | 159 | 5108343 | 4676352 | 91.5% | 92.3% |
| Sonnet 5.5 | 141 | 3757379 | 3601333 | 95.8% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9471 | 111905210 | 64100352 | 57.3% | 57.3% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 808 | 13054923 | 11544256 | 88.4% | 89.1% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8344 | 251064903 | 233860224 | 93.1% | 93.6% |
| Sonnet 5.5 | 8454 | 196695064 | 188093626 | 95.6% | 96.3% |
