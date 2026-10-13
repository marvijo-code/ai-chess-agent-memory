# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0041-20261013-124210)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 108 | 2135293 | 2054016 | 96.2% | 96.8% |
| GLM 5.3 Flash | 74 | 1388272 | 1253056 | 90.3% | 91.2% |
| GPT-6.1 Sol | 62 | 1739233 | 1531136 | 88.0% | 88.7% |
| Sonnet 5.5 | 135 | 3940498 | 3743059 | 95.0% | 95.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10092 | 123242128 | 74526976 | 60.5% | 60.5% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1192 | 19549461 | 17154432 | 87.7% | 88.5% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8995 | 271961844 | 253177984 | 93.1% | 93.6% |
| Sonnet 5.5 | 9402 | 225784354 | 216124117 | 95.7% | 96.4% |
