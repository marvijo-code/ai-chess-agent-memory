# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0082-20261103-122248)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 210 | 9819200 | 8890624 | 90.5% | 91.0% |
| GLM 5.3 Flash | 140 | 6660402 | 5962240 | 89.5% | 89.9% |
| Muse Spark 1.3 | 220 | 8632370 | 8057424 | 93.3% | 93.9% |
| Sonnet 5.5 | 364 | 21044677 | 19293487 | 91.7% | 92.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 17187 | 484918087 | 396648322 | 81.8% | 82.1% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7179 | 259262154 | 216045264 | 83.3% | 83.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2901 | 85557164 | 78959130 | 92.3% | 92.9% |
| Sonnet 5.5 | 13735 | 452118980 | 425697799 | 94.2% | 94.8% |
