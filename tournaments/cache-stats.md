# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0071-20261027-002235)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 153 | 7774607 | 6825984 | 87.8% | 88.1% |
| GLM 5.3 Flash | 194 | 10295687 | 9483008 | 92.1% | 92.3% |
| Haiku 5.5 | 158 | 9465054 | 8834424 | 93.3% | 93.8% |
| Muse Spark 1.3 | 175 | 3652768 | 3381431 | 92.6% | 93.1% |
| Sonnet 5.5 | 203 | 11240523 | 10572206 | 94.1% | 94.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14337 | 334349845 | 260631042 | 78.0% | 78.2% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5110 | 160075998 | 128411708 | 80.2% | 80.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 730 | 13295021 | 12474989 | 93.8% | 94.4% |
| Sonnet 5.5 | 10741 | 285768228 | 272494910 | 95.4% | 96.0% |
