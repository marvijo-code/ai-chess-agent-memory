# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0046-20261017-142632)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 38 | 1760133 | 1528576 | 86.8% | 87.1% |
| GLM 5.3 Flash | 41 | 2206485 | 1621440 | 73.5% | 74.0% |
| Haiku 5.5 | 37 | 1803133 | 1713802 | 95.0% | 95.6% |
| Sonnet 5.5 | 37 | 1993248 | 1870921 | 93.9% | 94.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10821 | 151002479 | 97760640 | 64.7% | 64.9% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1840 | 43101277 | 36268416 | 84.1% | 84.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 570 | 29772206 | 28438392 | 95.5% | 95.9% |
| Sonnet 5.5 | 10486 | 272503275 | 260068870 | 95.4% | 96.1% |
