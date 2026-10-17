# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0045-20261017-034241)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 86 | 5231867 | 4172416 | 79.8% | 79.9% |
| GLM 5.3 Flash | 83 | 2998962 | 2715648 | 90.6% | 91.1% |
| GPT-6.1 Sol | 154 | 6369205 | 6038528 | 94.8% | 95.3% |
| Haiku 5.5 | 62 | 2222248 | 2072277 | 93.3% | 93.9% |
| Sonnet 5.5 | 112 | 4921396 | 4461582 | 90.7% | 91.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10610 | 140113249 | 88540672 | 63.2% | 63.3% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1728 | 38070014 | 32610240 | 85.7% | 86.2% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9901 | 305430674 | 284721920 | 93.2% | 93.8% |
| Haiku 5.5 | 386 | 18648040 | 17822549 | 95.6% | 95.9% |
| Sonnet 5.5 | 10278 | 261929364 | 250092893 | 95.5% | 96.2% |
