# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0077-20261101-132048)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 262 | 14917808 | 13442432 | 90.1% | 90.4% |
| GLM 5.3 Flash | 180 | 9045041 | 8186692 | 90.5% | 90.8% |
| Muse Spark 1.3 | 236 | 7975999 | 7527603 | 94.4% | 95.1% |
| Sonnet 5.5 | 223 | 13210695 | 12309938 | 93.2% | 93.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 16021 | 426303795 | 343725186 | 80.6% | 80.9% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6359 | 220427224 | 181261800 | 82.2% | 82.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2022 | 54501499 | 50526163 | 92.7% | 93.3% |
| Sonnet 5.5 | 12274 | 372003992 | 352299954 | 94.7% | 95.3% |
