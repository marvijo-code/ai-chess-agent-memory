# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0007-20261009-031124)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 168 | 2087768 | 900736 | 43.1% | 43.0% |
| GPT-6.1 Sol | 122 | 3244168 | 2986880 | 92.1% | 92.8% |
| Sonnet 5.5 | 117 | 2263795 | 2140306 | 94.5% | 95.3% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1872 | 21167302 | 9734912 | 46.0% | 45.9% |
| GPT-6.1 Sol | 1496 | 43510867 | 40586240 | 93.3% | 93.7% |
| Sonnet 5.5 | 1659 | 38063997 | 36433917 | 95.7% | 96.2% |
