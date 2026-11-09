# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0088-20261109-135130)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 174 | 8587707 | 7761792 | 90.4% | 90.8% |
| GLM 5.3 Flash | 120 | 4484843 | 3942912 | 87.9% | 88.7% |
| Muse Spark 1.3 | 166 | 7188352 | 6744653 | 93.8% | 94.2% |
| Sonnet 5.5 | 159 | 7775928 | 7219957 | 92.9% | 93.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 18619 | 563747897 | 468823042 | 83.2% | 83.5% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 8194 | 302593788 | 255332944 | 84.4% | 84.9% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 4146 | 135416281 | 125634505 | 92.8% | 93.3% |
| Sonnet 5.5 | 15209 | 535851888 | 503848993 | 94.0% | 94.6% |
