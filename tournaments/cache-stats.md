# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0039-20261013-051801)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 84 | 1494318 | 1344512 | 90.0% | 90.5% |
| GLM 5.3 Flash | 37 | 527244 | 481280 | 91.3% | 92.4% |
| GPT-6.1 Sol | 53 | 1772867 | 1643264 | 92.7% | 93.5% |
| Sonnet 5.5 | 86 | 2389457 | 2288652 | 95.8% | 96.8% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 9608 | 114090606 | 66065024 | 57.9% | 57.9% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 845 | 13582167 | 12025536 | 88.5% | 89.3% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 8509 | 257514825 | 239922816 | 93.2% | 93.7% |
| Sonnet 5.5 | 8721 | 205062798 | 196193592 | 95.7% | 96.4% |
