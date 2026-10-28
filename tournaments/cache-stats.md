# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0074-20261028-202920)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 49 | 2678215 | 2407424 | 89.9% | 90.1% |
| GLM 5.3 Flash | 40 | 1713814 | 1386112 | 80.9% | 81.2% |
| Muse Spark 1.3 | 36 | 1005806 | 915074 | 91.0% | 91.6% |
| Sonnet 5.5 | 51 | 2800582 | 2591333 | 92.5% | 93.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 14831 | 360157345 | 283646082 | 78.8% | 79.0% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 5475 | 177314716 | 142553988 | 80.4% | 81.0% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 1123 | 23172131 | 21601441 | 93.2% | 93.8% |
| Sonnet 5.5 | 11080 | 304252692 | 289644698 | 95.2% | 95.9% |
