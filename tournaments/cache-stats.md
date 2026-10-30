# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0076-20261029-173613)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 232 | 12844610 | 11620480 | 90.5% | 90.7% |
| GLM 5.3 Flash | 199 | 10336251 | 9316000 | 90.1% | 90.4% |
| Muse Spark 1.3 | 147 | 5924614 | 5451867 | 92.0% | 92.5% |
| Sonnet 5.5 | 111 | 6008397 | 5430699 | 90.4% | 91.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 15637 | 403761613 | 323354754 | 80.1% | 80.4% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6130 | 208931376 | 170995940 | 81.8% | 82.4% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1681 | 43069253 | 39875806 | 92.6% | 93.1% |
| Sonnet 5.5 | 11920 | 351296586 | 333134191 | 94.8% | 95.5% |
