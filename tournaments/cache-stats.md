# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0077-20261101-132048)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 199 | 12246836 | 11044992 | 90.2% | 90.5% |
| GLM 5.3 Flash | 180 | 9045041 | 8186692 | 90.5% | 90.8% |
| Muse Spark 1.3 | 145 | 4700358 | 4402410 | 93.7% | 94.5% |
| Sonnet 5.5 | 183 | 11034506 | 10305446 | 93.4% | 94.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 15958 | 423632823 | 341327746 | 80.6% | 80.9% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6359 | 220427224 | 181261800 | 82.2% | 82.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1931 | 51225858 | 47400970 | 92.5% | 93.1% |
| Sonnet 5.5 | 12234 | 369827803 | 350295462 | 94.7% | 95.3% |
