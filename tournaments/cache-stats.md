# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0039-20261013-051801)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 158 | 3401536 | 3193856 | 93.9% | 94.3% |
| GLM 5.3 Flash | 138 | 2577130 | 2368000 | 91.9% | 92.6% |
| GPT-6.1 Sol | 120 | 3552686 | 3255552 | 91.6% | 92.3% |
| Sonnet 5.5 | 159 | 4253215 | 4071560 | 95.7% | 96.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9682 | 115997824 | 67914368 | 58.5% | 58.6% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 946 | 15632053 | 13912256 | 89.0% | 89.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8576 | 259294644 | 241535104 | 93.2% | 93.7% |
| Sonnet 5.5 | 8794 | 206926556 | 197976500 | 95.7% | 96.4% |
