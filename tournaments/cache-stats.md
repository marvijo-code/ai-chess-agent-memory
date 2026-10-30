# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0076-20261029-173613)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 268 | 14503672 | 13073024 | 90.1% | 90.3% |
| GLM 5.3 Flash | 248 | 12787058 | 11395168 | 89.1% | 89.3% |
| Muse Spark 1.3 | 208 | 7694194 | 7004563 | 91.0% | 91.5% |
| Sonnet 5.5 | 188 | 10579377 | 9674603 | 91.4% | 92.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 15673 | 405420675 | 324807298 | 80.1% | 80.4% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6179 | 211382183 | 173075108 | 81.9% | 82.4% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1742 | 44838833 | 41428502 | 92.4% | 92.9% |
| Sonnet 5.5 | 11997 | 355867566 | 337378095 | 94.8% | 95.4% |
