# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0076-20261029-173613)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 110 | 5583780 | 5025280 | 90.0% | 90.2% |
| GLM 5.3 Flash | 127 | 6878769 | 6170592 | 89.7% | 89.9% |
| Muse Spark 1.3 | 6 | 48542 | 38453 | 79.2% | 91.0% |
| Sonnet 5.5 | 47 | 2209561 | 2028202 | 91.8% | 93.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 15515 | 396500783 | 316759554 | 79.9% | 80.2% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6058 | 205473894 | 167850532 | 81.7% | 82.2% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1540 | 37193181 | 34462392 | 92.7% | 93.2% |
| Sonnet 5.5 | 11856 | 347497750 | 329731694 | 94.9% | 95.5% |
