# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0078-20261101-211509)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 140 | 7169282 | 6471424 | 90.3% | 90.6% |
| GLM 5.3 Flash | 172 | 10321639 | 9447208 | 91.5% | 91.7% |
| Muse Spark 1.3 | 115 | 5294203 | 4833565 | 91.3% | 91.7% |
| Sonnet 5.5 | 131 | 7794373 | 7225929 | 92.7% | 93.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 16161 | 433473077 | 350196610 | 80.8% | 81.1% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6531 | 230748863 | 190709008 | 82.6% | 83.2% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2137 | 59795702 | 55359728 | 92.6% | 93.1% |
| Sonnet 5.5 | 12405 | 379798365 | 359525883 | 94.7% | 95.3% |
