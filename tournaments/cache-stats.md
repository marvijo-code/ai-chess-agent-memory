# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0044-20261016-161517)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 79 | 3457354 | 2873728 | 83.1% | 83.4% |
| GLM 5.3 Flash | 108 | 5139105 | 3768832 | 73.3% | 73.5% |
| GPT-6.1 Sol | 149 | 6540250 | 6342528 | 97.0% | 97.4% |
| Haiku 5.5 | 79 | 2121768 | 1974545 | 93.1% | 93.6% |
| Sonnet 5.5 | 155 | 8082284 | 7593900 | 94.0% | 94.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10477 | 133100155 | 83061504 | 62.4% | 62.5% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1550 | 30673845 | 26247616 | 85.6% | 86.2% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9553 | 291228560 | 271261312 | 93.1% | 93.7% |
| Haiku 5.5 | 79 | 2121768 | 1974545 | 93.1% | 93.6% |
| Sonnet 5.5 | 9886 | 242779628 | 232229404 | 95.7% | 96.4% |
