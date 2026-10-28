# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0073-20261028-121341)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 241 | 12318030 | 10876672 | 88.3% | 88.6% |
| GLM 5.3 Flash | 120 | 6226989 | 5391020 | 86.6% | 87.2% |
| Muse Spark 1.3 | 172 | 4207256 | 3833361 | 91.1% | 92.0% |
| Sonnet 5.5 | 288 | 15683882 | 14558455 | 92.8% | 93.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14778 | 357111139 | 280903554 | 78.7% | 78.9% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5435 | 175600902 | 141167876 | 80.4% | 81.0% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1084 | 22065463 | 20590028 | 93.3% | 93.9% |
| Sonnet 5.5 | 11029 | 301452110 | 287053365 | 95.2% | 95.9% |
