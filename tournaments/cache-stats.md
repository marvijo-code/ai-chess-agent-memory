# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0009-20261009-081556)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 131 | 1211635 | 567936 | 46.9% | 46.7% |
| GPT-6.1 Sol | 213 | 7812296 | 7274880 | 93.1% | 93.6% |
| Sonnet 5.5 | 148 | 3404005 | 3249228 | 95.5% | 96.1% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2391 | 26310985 | 11964288 | 45.5% | 45.4% |
| GPT-6.1 Sol | 2045 | 61444754 | 57288320 | 93.2% | 93.7% |
| Sonnet 5.5 | 2115 | 47998163 | 45915747 | 95.7% | 96.2% |
