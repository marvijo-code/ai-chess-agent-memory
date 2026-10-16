# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0044-20261016-161517)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 99 | 4184905 | 3366656 | 80.4% | 80.7% |
| GLM 5.3 Flash | 122 | 5340717 | 3932032 | 73.6% | 73.8% |
| GPT-6.1 Sol | 205 | 8818857 | 8499456 | 96.4% | 96.8% |
| Haiku 5.5 | 93 | 2327481 | 2147927 | 92.3% | 93.0% |
| Sonnet 5.5 | 211 | 10717598 | 10074199 | 94.0% | 94.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10497 | 133827706 | 83554432 | 62.4% | 62.5% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1564 | 30875457 | 26410816 | 85.5% | 86.2% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9609 | 293507167 | 273418240 | 93.2% | 93.7% |
| Haiku 5.5 | 93 | 2327481 | 2147927 | 92.3% | 93.0% |
| Sonnet 5.5 | 9942 | 245414942 | 234709703 | 95.6% | 96.3% |
