# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0088-20261109-135130)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 60 | 2725923 | 2484608 | 91.1% | 91.7% |
| GLM 5.3 Flash | 45 | 1732191 | 1435072 | 82.8% | 83.6% |
| Muse Spark 1.3 | 61 | 3261840 | 3148555 | 96.5% | 96.8% |
| Sonnet 5.5 | 83 | 4501872 | 4184611 | 93.0% | 93.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 18505 | 557886113 | 463545858 | 83.1% | 83.4% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 8119 | 299841136 | 252825104 | 84.3% | 84.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 4041 | 131489769 | 122038407 | 92.8% | 93.4% |
| Sonnet 5.5 | 15133 | 532577832 | 500813647 | 94.0% | 94.6% |
