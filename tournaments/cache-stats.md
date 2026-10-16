# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0042-20261016-110957)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10 | 88968 | 81024 | 91.1% | 93.5% |
| GLM 5.3 Flash | 10 | 85990 | 70720 | 82.2% | 88.9% |
| Sonnet 5.5 | 39 | 972027 | 924854 | 95.1% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10253 | 126806251 | 77790336 | 61.3% | 61.4% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1313 | 22544822 | 19887360 | 88.2% | 88.9% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9166 | 276783155 | 257553024 | 93.1% | 93.6% |
| Sonnet 5.5 | 9572 | 230058529 | 220184134 | 95.7% | 96.4% |
