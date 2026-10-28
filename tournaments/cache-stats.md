# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0073-20261028-121341)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 57 | 2748682 | 2446336 | 89.0% | 89.5% |
| GLM 5.3 Flash | 61 | 2059871 | 1521964 | 73.9% | 74.7% |
| Muse Spark 1.3 | 45 | 934182 | 812185 | 86.9% | 88.1% |
| Sonnet 5.5 | 94 | 4390411 | 4055772 | 92.4% | 93.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14594 | 347541791 | 272473218 | 78.4% | 78.7% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5376 | 171433784 | 137298820 | 80.1% | 80.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 957 | 18792389 | 17568852 | 93.5% | 94.1% |
| Sonnet 5.5 | 10835 | 290158639 | 276550682 | 95.3% | 96.0% |
