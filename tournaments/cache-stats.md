# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0077-20261101-132048)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 24 | 1359154 | 1157760 | 85.2% | 85.6% |
| GLM 5.3 Flash | 55 | 2447889 | 2125952 | 86.8% | 87.3% |
| Muse Spark 1.3 | 46 | 1251096 | 1166700 | 93.3% | 94.5% |
| Sonnet 5.5 | 10 | 264881 | 212938 | 80.4% | 84.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 15783 | 412745141 | 331440514 | 80.3% | 80.6% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6234 | 213830072 | 175201060 | 81.9% | 82.5% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1832 | 47776596 | 44165260 | 92.4% | 93.0% |
| Sonnet 5.5 | 12061 | 359058178 | 340202954 | 94.7% | 95.4% |
