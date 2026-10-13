# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0041-20261013-124210)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 217 | 5034802 | 4775296 | 94.8% | 95.3% |
| GLM 5.3 Flash | 185 | 4297643 | 3915264 | 91.1% | 91.7% |
| GPT-6.1 Sol | 116 | 2986581 | 2641408 | 88.4% | 89.4% |
| Sonnet 5.5 | 159 | 4420990 | 4189394 | 94.8% | 95.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10201 | 126141637 | 77248256 | 61.2% | 61.3% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1303 | 22458832 | 19816640 | 88.2% | 88.9% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9049 | 273209192 | 254288256 | 93.1% | 93.6% |
| Sonnet 5.5 | 9426 | 226264846 | 216570452 | 95.7% | 96.4% |
