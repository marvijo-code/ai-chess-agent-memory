# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0044-20261016-161517)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 99 | 4184905 | 3366656 | 80.4% | 80.7% |
| GLM 5.3 Flash | 159 | 6682736 | 4961280 | 74.2% | 74.5% |
| GPT-6.1 Sol | 220 | 9102349 | 8748160 | 96.1% | 96.7% |
| Haiku 5.5 | 133 | 4172324 | 3888040 | 93.2% | 93.8% |
| Sonnet 5.5 | 211 | 10717598 | 10074199 | 94.0% | 94.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10497 | 133827706 | 83554432 | 62.4% | 62.5% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1601 | 32217476 | 27440064 | 85.2% | 85.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9624 | 293790659 | 273666944 | 93.2% | 93.7% |
| Haiku 5.5 | 133 | 4172324 | 3888040 | 93.2% | 93.8% |
| Sonnet 5.5 | 9942 | 245414942 | 234709703 | 95.6% | 96.3% |
