# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0012-20261009-164703)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 125 | 1029761 | 573952 | 55.7% | 56.0% |
| GPT-6.1 Sol | 149 | 3773674 | 3470336 | 92.0% | 92.7% |
| Sonnet 5.5 | 187 | 4336894 | 4150062 | 95.7% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2969 | 31714754 | 14410112 | 45.4% | 45.3% |
| GPT-6.1 Sol | 2711 | 80144999 | 74516608 | 93.0% | 93.4% |
| Sonnet 5.5 | 2780 | 62129109 | 59378799 | 95.6% | 96.2% |
