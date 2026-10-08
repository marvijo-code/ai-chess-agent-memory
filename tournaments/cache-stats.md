# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0005-20261008-214616)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 169 | 1651214 | 686208 | 41.6% | 41.4% |
| GPT-6.1 Sol | 194 | 6253446 | 5858944 | 93.7% | 94.4% |
| Sonnet 5.5 | 192 | 4560460 | 4366927 | 95.8% | 96.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1348 | 14911108 | 6861696 | 46.0% | 45.9% |
| GPT-6.1 Sol | 1124 | 33476132 | 31273984 | 93.4% | 93.8% |
| Sonnet 5.5 | 1195 | 27193006 | 26029951 | 95.7% | 96.2% |
