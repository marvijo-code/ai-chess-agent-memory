# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0045-20261017-034241)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 192 | 10782108 | 8878976 | 82.3% | 82.6% |
| GLM 5.3 Flash | 129 | 4959721 | 4204032 | 84.8% | 85.1% |
| GPT-6.1 Sol | 204 | 8529601 | 8129280 | 95.3% | 95.7% |
| Haiku 5.5 | 204 | 11193404 | 10642468 | 95.1% | 95.5% |
| Sonnet 5.5 | 206 | 9691229 | 9010668 | 93.0% | 93.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 10716 | 145663490 | 93247232 | 64.0% | 64.1% |
| Fable 5.1 | 179 | 3913645 | 3703873 | 94.6% | 95.5% |
| GLM 5.3 Flash | 1774 | 40030773 | 34098624 | 85.2% | 85.7% |
| GPT-6 Astra | 456 | 15632539 | 14922624 | 95.5% | 95.9% |
| GPT-6.1 Sol | 9951 | 307591070 | 286812672 | 93.2% | 93.8% |
| Haiku 5.5 | 528 | 27619196 | 26392740 | 95.6% | 95.9% |
| Sonnet 5.5 | 10372 | 266699197 | 254641979 | 95.5% | 96.2% |
