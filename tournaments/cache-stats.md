# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0078-20261101-211509)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 93 | 4641661 | 4216320 | 90.8% | 91.2% |
| GLM 5.3 Flash | 111 | 6734794 | 6191912 | 91.9% | 92.1% |
| Muse Spark 1.3 | 69 | 3206209 | 2870193 | 89.5% | 89.9% |
| Sonnet 5.5 | 73 | 4553877 | 4290627 | 94.2% | 94.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 16114 | 430945456 | 347941506 | 80.7% | 81.0% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6470 | 227162018 | 187453712 | 82.5% | 83.0% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2091 | 57707708 | 53396356 | 92.5% | 93.1% |
| Sonnet 5.5 | 12347 | 376557869 | 356590581 | 94.7% | 95.3% |
