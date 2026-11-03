# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0080-20261102-201218)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 180 | 9556078 | 8658432 | 90.6% | 90.9% |
| GLM 5.3 Flash | 107 | 4112830 | 3578432 | 87.0% | 87.6% |
| Muse Spark 1.3 | 89 | 2361755 | 2099777 | 88.9% | 90.0% |
| Sonnet 5.5 | 159 | 8003563 | 7157256 | 89.4% | 90.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 16677 | 460156361 | 374250498 | 81.3% | 81.6% |
| DeepSeek V4.1 Flash 1017 | 2852 | 141981847 | 125681528 | 88.5% | 88.8% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 6875 | 244868590 | 203153552 | 83.0% | 83.5% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 10063 | 311254406 | 290190080 | 93.2% | 93.8% |
| Haiku 5.5 | 761 | 40763218 | 38696645 | 94.9% | 95.3% |
| Muse Spark 1.3 | 2425 | 68765401 | 63611294 | 92.5% | 93.1% |
| Sonnet 5.5 | 13044 | 414346404 | 391153618 | 94.4% | 95.0% |
