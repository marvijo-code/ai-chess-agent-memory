# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0071-20261027-002235)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 97 | 4457390 | 3875072 | 86.9% | 87.3% |
| GLM 5.3 Flash | 106 | 4945855 | 4518464 | 91.4% | 91.8% |
| Haiku 5.5 | 118 | 7208958 | 6812131 | 94.5% | 94.9% |
| Muse Spark 1.3 | 112 | 2433240 | 2261691 | 92.9% | 93.5% |
| Sonnet 5.5 | 136 | 7419042 | 6954118 | 93.7% | 94.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14281 | 331032628 | 257680130 | 77.8% | 78.1% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5022 | 154726166 | 123447164 | 79.8% | 80.4% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 721 | 38507122 | 36674352 | 95.2% | 95.6% |
| Muse Spark 1.3 | 667 | 12075493 | 11355249 | 94.0% | 94.6% |
| Sonnet 5.5 | 10674 | 281946747 | 268876822 | 95.4% | 96.0% |
