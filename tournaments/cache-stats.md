# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0044-20261016-161517)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 13 | 237793 | 187264 | 78.8% | 80.2% |
| GLM 5.3 Flash | 14 | 171202 | 142528 | 83.3% | 86.0% |
| GPT-6.1 Sol | 33 | 840029 | 799232 | 95.1% | 96.5% |
| Haiku 5.5 | 33 | 890204 | 832307 | 93.5% | 93.8% |
| Sonnet 5.5 | 87 | 4897093 | 4618963 | 94.3% | 94.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10411 | 129880594 | 80375040 | 61.9% | 62.0% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1456 | 25705942 | 22621312 | 88.0% | 88.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9437 | 285528339 | 265718016 | 93.1% | 93.6% |
| Haiku 5.5 | 33 | 890204 | 832307 | 93.5% | 93.8% |
| Sonnet 5.5 | 9818 | 239594437 | 229254467 | 95.7% | 96.4% |
