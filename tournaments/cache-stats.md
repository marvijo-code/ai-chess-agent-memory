# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0086-20261108-185025)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 34 | 1566309 | 1439744 | 91.9% | 93.4% |
| GLM 5.3 Flash | 23 | 689305 | 627776 | 91.1% | 92.1% |
| Muse Spark 1.3 | 80 | 3040195 | 2772364 | 91.2% | 91.5% |
| Sonnet 5.5 | 90 | 4235266 | 3868426 | 91.3% | 91.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 17913 | 523388243 | 431588994 | 82.5% | 82.8% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 7670 | 279231605 | 234120208 | 83.8% | 84.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 3667 | 113980779 | 105506275 | 92.6% | 93.2% |
| Sonnet 5.5 | 14755 | 510196562 | 479767398 | 94.0% | 94.6% |
