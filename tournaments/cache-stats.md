# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0044-20261016-161517)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| GPT-6.1 Sol | 33 | 840029 | 799232 | 95.1% | 96.5% |
| Haiku 5.5 | 33 | 890204 | 832307 | 93.5% | 93.8% |
| Sonnet 5.5 | 36 | 1657889 | 1515948 | 91.4% | 92.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10398 | 129642801 | 80187776 | 61.9% | 61.9% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1442 | 25534740 | 22478784 | 88.0% | 88.8% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9437 | 285528339 | 265718016 | 93.1% | 93.6% |
| Haiku 5.5 | 33 | 890204 | 832307 | 93.5% | 93.8% |
| Sonnet 5.5 | 9767 | 236355233 | 226151452 | 95.7% | 96.4% |
