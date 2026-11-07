# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0083-20261107-164306)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 145 | 7459686 | 6634880 | 88.9% | 89.7% |
| GLM 5.3 Flash | 88 | 3293176 | 2986560 | 90.7% | 91.4% |
| Muse Spark 1.3 | 61 | 1270225 | 1102776 | 86.8% | 88.2% |
| Sonnet 5.5 | 177 | 11019427 | 10149267 | 92.1% | 92.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 17378 | 495079321 | 405798914 | 82.0% | 82.3% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7267 | 262555330 | 219031824 | 83.4% | 83.9% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 3007 | 88964523 | 82038364 | 92.2% | 92.8% |
| Sonnet 5.5 | 13912 | 463138407 | 435847066 | 94.1% | 94.7% |
