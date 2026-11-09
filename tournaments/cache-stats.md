# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0089-20261109-210352)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 15 | 345863 | 282112 | 81.6% | 85.5% |
| GLM 5.3 Flash | 15 | 333771 | 262144 | 78.5% | 81.0% |
| Sonnet 5.5 | 51 | 2615594 | 2440664 | 93.3% | 93.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 18658 | 564995143 | 469913858 | 83.2% | 83.5% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 8234 | 303630261 | 256223952 | 84.4% | 84.9% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 4146 | 135416281 | 125634505 | 92.8% | 93.3% |
| Sonnet 5.5 | 15318 | 541369403 | 509037233 | 94.0% | 94.6% |
