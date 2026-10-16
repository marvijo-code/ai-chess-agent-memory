# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0043-20261016-140539)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 38 | 1305537 | 1109888 | 85.0% | 85.7% |
| GLM 5.3 Flash | 43 | 1681358 | 1491392 | 88.7% | 89.8% |
| GPT-6.1 Sol | 83 | 3043252 | 2910464 | 95.6% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10398 | 129642801 | 80187776 | 61.9% | 61.9% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1442 | 25534740 | 22478784 | 88.0% | 88.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9404 | 284688310 | 264918784 | 93.1% | 93.6% |
| Sonnet 5.5 | 9731 | 234697344 | 224635504 | 95.7% | 96.4% |
