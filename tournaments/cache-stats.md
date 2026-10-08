# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0005-20261008-214616)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 169 | 1651214 | 686208 | 41.6% | 41.4% |
| GPT-6.1 Sol | 211 | 7044428 | 6639616 | 94.3% | 94.9% |
| Sonnet 5.5 | 209 | 5226189 | 5017795 | 96.0% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1348 | 14911108 | 6861696 | 46.0% | 45.9% |
| GPT-6.1 Sol | 1141 | 34267114 | 32054656 | 93.5% | 94.0% |
| Sonnet 5.5 | 1212 | 27858735 | 26680819 | 95.8% | 96.3% |
