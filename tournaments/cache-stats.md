# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0040-20261013-090848)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 91 | 1598256 | 1409920 | 88.2% | 89.5% |
| GLM 5.3 Flash | 114 | 1751685 | 1418240 | 81.0% | 81.8% |
| GPT-6.1 Sol | 154 | 4532599 | 4164096 | 91.9% | 92.7% |
| Sonnet 5.5 | 148 | 4441416 | 4275487 | 96.3% | 97.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9894 | 119786815 | 71344896 | 59.6% | 59.6% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1090 | 17794216 | 15653056 | 88.0% | 88.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8879 | 268952201 | 250528128 | 93.1% | 93.7% |
| Sonnet 5.5 | 9072 | 215776901 | 206526855 | 95.7% | 96.4% |
