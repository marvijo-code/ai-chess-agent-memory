# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0089-20261109-210352)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 147 | 6844070 | 5984640 | 87.4% | 88.7% |
| GLM 5.3 Flash | 230 | 13449656 | 11773952 | 87.5% | 87.9% |
| Sonnet 5.5 | 238 | 13021943 | 11934609 | 91.6% | 92.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 18790 | 571493350 | 475616386 | 83.2% | 83.6% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 8449 | 316746146 | 267735760 | 84.5% | 85.0% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 4146 | 135416281 | 125634505 | 92.8% | 93.3% |
| Sonnet 5.5 | 15505 | 551775752 | 518531178 | 94.0% | 94.6% |
