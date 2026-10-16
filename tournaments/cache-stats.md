# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0044-20261016-161517)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 96 | 4137086 | 3331200 | 80.5% | 80.8% |
| GLM 5.3 Flash | 108 | 5139105 | 3768832 | 73.3% | 73.5% |
| GPT-6.1 Sol | 205 | 8818857 | 8499456 | 96.4% | 96.8% |
| Haiku 5.5 | 79 | 2121768 | 1974545 | 93.1% | 93.6% |
| Sonnet 5.5 | 211 | 10717598 | 10074199 | 94.0% | 94.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10494 | 133779887 | 83518976 | 62.4% | 62.5% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1550 | 30673845 | 26247616 | 85.6% | 86.2% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9609 | 293507167 | 273418240 | 93.2% | 93.7% |
| Haiku 5.5 | 79 | 2121768 | 1974545 | 93.1% | 93.6% |
| Sonnet 5.5 | 9942 | 245414942 | 234709703 | 95.6% | 96.3% |
