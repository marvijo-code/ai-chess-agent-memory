# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0039-20261013-051801)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 158 | 3401536 | 3193856 | 93.9% | 94.3% |
| GLM 5.3 Flash | 138 | 2577130 | 2368000 | 91.9% | 92.6% |
| GPT-6.1 Sol | 107 | 3005447 | 2727936 | 90.8% | 91.5% |
| Sonnet 5.5 | 146 | 3766832 | 3597873 | 95.5% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9682 | 115997824 | 67914368 | 58.5% | 58.6% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 946 | 15632053 | 13912256 | 89.0% | 89.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8563 | 258747405 | 241007488 | 93.1% | 93.6% |
| Sonnet 5.5 | 8781 | 206440173 | 197502813 | 95.7% | 96.4% |
