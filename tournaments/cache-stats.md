# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0071-20261027-002235)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 75 | 3686931 | 3226624 | 87.5% | 87.8% |
| GLM 5.3 Flash | 84 | 4323688 | 3974464 | 91.9% | 92.2% |
| Haiku 5.5 | 118 | 7208958 | 6812131 | 94.5% | 94.9% |
| Muse Spark 1.3 | 84 | 1515695 | 1411664 | 93.1% | 94.1% |
| Sonnet 5.5 | 108 | 5290638 | 4964377 | 93.8% | 94.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14259 | 330262169 | 257031682 | 77.8% | 78.1% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5000 | 154103999 | 122903164 | 79.8% | 80.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 721 | 38507122 | 36674352 | 95.2% | 95.6% |
| Muse Spark 1.3 | 639 | 11157948 | 10505222 | 94.2% | 94.7% |
| Sonnet 5.5 | 10646 | 279818343 | 266887081 | 95.4% | 96.1% |
