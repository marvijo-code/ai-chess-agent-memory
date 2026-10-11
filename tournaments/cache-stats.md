# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0024-20261011-001419)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 217 | 2321924 | 1300992 | 56.0% | 56.0% |
| GPT-6.1 Sol | 153 | 4374160 | 4110080 | 94.0% | 94.3% |
| Sonnet 5.5 | 127 | 2252253 | 2116691 | 94.0% | 95.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 6405 | 71158055 | 35575296 | 50.0% | 49.9% |
| GPT-6.1 Sol | 5135 | 147889982 | 137607424 | 93.0% | 93.5% |
| Sonnet 5.5 | 5371 | 118305466 | 112957599 | 95.5% | 96.1% |
