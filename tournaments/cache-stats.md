# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0072-20261028-024146)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 113 | 5815075 | 5229440 | 89.9% | 90.3% |
| GLM 5.3 Flash | 133 | 6364017 | 5041920 | 79.2% | 79.4% |
| Muse Spark 1.3 | 81 | 1374130 | 1263357 | 91.9% | 93.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14450 | 340164920 | 265860482 | 78.2% | 78.4% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5243 | 166440015 | 133453628 | 80.2% | 80.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 811 | 14669151 | 13738346 | 93.7% | 94.2% |
| Sonnet 5.5 | 10741 | 285768228 | 272494910 | 95.4% | 96.0% |
