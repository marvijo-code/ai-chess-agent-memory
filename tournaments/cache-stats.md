# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0008-20261009-055507)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 102 | 890349 | 402432 | 45.2% | 44.9% |
| GPT-6.1 Sol | 95 | 2634402 | 2458624 | 93.3% | 93.7% |
| Sonnet 5.5 | 68 | 1291912 | 1220832 | 94.5% | 95.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2099 | 23382642 | 10703360 | 45.8% | 45.7% |
| GPT-6.1 Sol | 1715 | 50653781 | 47298176 | 93.4% | 93.8% |
| Sonnet 5.5 | 1813 | 41100326 | 39314321 | 95.7% | 96.2% |
