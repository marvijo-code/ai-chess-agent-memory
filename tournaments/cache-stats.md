# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0089-20261109-210352)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 122 | 5254605 | 4561024 | 86.8% | 88.4% |
| GLM 5.3 Flash | 204 | 11370770 | 9969664 | 87.7% | 88.1% |
| Sonnet 5.5 | 238 | 13021943 | 11934609 | 91.6% | 92.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 18765 | 569903885 | 474192770 | 83.2% | 83.6% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 8423 | 314667260 | 265931472 | 84.5% | 85.0% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 4146 | 135416281 | 125634505 | 92.8% | 93.3% |
| Sonnet 5.5 | 15505 | 551775752 | 518531178 | 94.0% | 94.6% |
