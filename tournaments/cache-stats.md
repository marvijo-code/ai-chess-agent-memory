# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0076-20261029-173613)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 185 | 10466637 | 9546880 | 91.2% | 91.4% |
| GLM 5.3 Flash | 159 | 7870874 | 7051328 | 89.6% | 89.8% |
| Muse Spark 1.3 | 33 | 715671 | 659119 | 92.1% | 94.0% |
| Sonnet 5.5 | 62 | 3557018 | 3255958 | 91.5% | 92.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 15590 | 401383640 | 321281154 | 80.0% | 80.3% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6090 | 206465999 | 168731268 | 81.7% | 82.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1567 | 37860310 | 35083058 | 92.7% | 93.2% |
| Sonnet 5.5 | 11871 | 348845207 | 330959450 | 94.9% | 95.5% |
