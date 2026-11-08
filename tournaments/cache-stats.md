# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0086-20261108-185025)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| GLM 5.3 Flash | 23 | 689305 | 627776 | 91.1% | 92.1% |
| Muse Spark 1.3 | 55 | 2446521 | 2221044 | 90.8% | 91.0% |
| Sonnet 5.5 | 58 | 2800376 | 2524457 | 90.1% | 90.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 17879 | 521821934 | 430149250 | 82.4% | 82.8% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7670 | 279231605 | 234120208 | 83.8% | 84.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 3642 | 113387105 | 104954955 | 92.6% | 93.1% |
| Sonnet 5.5 | 14723 | 508761672 | 478423429 | 94.0% | 94.6% |
