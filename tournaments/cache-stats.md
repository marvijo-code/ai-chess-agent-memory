# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0073-20261028-121341)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| GLM 5.3 Flash | 13 | 174159 | 136752 | 78.5% | 80.8% |
| Muse Spark 1.3 | 30 | 731000 | 631019 | 86.3% | 87.0% |
| Sonnet 5.5 | 13 | 291139 | 254150 | 87.3% | 91.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14537 | 344793109 | 270026882 | 78.3% | 78.6% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5328 | 169548072 | 135913608 | 80.2% | 80.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 942 | 18589207 | 17387686 | 93.5% | 94.1% |
| Sonnet 5.5 | 10754 | 286059367 | 272749060 | 95.3% | 96.0% |
