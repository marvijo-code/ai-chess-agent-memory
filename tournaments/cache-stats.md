# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0045-20261017-034241)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 86 | 5231867 | 4172416 | 79.8% | 79.9% |
| GLM 5.3 Flash | 61 | 2682315 | 2441472 | 91.0% | 91.4% |
| GPT-6.1 Sol | 111 | 5029810 | 4754560 | 94.5% | 95.0% |
| Haiku 5.5 | 62 | 2222248 | 2072277 | 93.3% | 93.9% |
| Sonnet 5.5 | 89 | 4268598 | 3867160 | 90.6% | 91.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10610 | 140113249 | 88540672 | 63.2% | 63.3% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1706 | 37753367 | 32336064 | 85.7% | 86.2% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9858 | 304091279 | 283437952 | 93.2% | 93.7% |
| Haiku 5.5 | 386 | 18648040 | 17822549 | 95.6% | 95.9% |
| Sonnet 5.5 | 10255 | 261276566 | 249498471 | 95.5% | 96.2% |
