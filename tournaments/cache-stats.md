# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0075-20261029-072421)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 202 | 11016141 | 10073216 | 91.4% | 91.7% |
| GLM 5.3 Flash | 136 | 5944741 | 5182144 | 87.2% | 87.6% |
| Muse Spark 1.3 | 168 | 5451129 | 4941133 | 90.6% | 91.1% |
| Sonnet 5.5 | 218 | 12452557 | 11617554 | 93.3% | 93.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 15316 | 386540088 | 307801346 | 79.6% | 79.9% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5931 | 198595125 | 161679940 | 81.4% | 82.0% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1444 | 34270271 | 31810671 | 92.8% | 93.4% |
| Sonnet 5.5 | 11718 | 340700006 | 323460799 | 94.9% | 95.6% |
