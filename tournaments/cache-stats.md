# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0080-20261102-201218)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 86 | 4341713 | 3874944 | 89.2% | 89.6% |
| GLM 5.3 Flash | 86 | 3362874 | 2995264 | 89.1% | 89.6% |
| Muse Spark 1.3 | 29 | 463319 | 391290 | 84.5% | 86.8% |
| Sonnet 5.5 | 122 | 6138842 | 5470322 | 89.1% | 89.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 16583 | 454941996 | 369467010 | 81.2% | 81.5% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6854 | 244118634 | 202570384 | 83.0% | 83.5% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2365 | 66866965 | 61902807 | 92.6% | 93.2% |
| Sonnet 5.5 | 13007 | 412481683 | 389466684 | 94.4% | 95.0% |
