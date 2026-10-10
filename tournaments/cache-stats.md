# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0019-20261010-104326)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 163 | 1655068 | 675712 | 40.8% | 40.6% |
| GPT-6.1 Sol | 128 | 3683069 | 3452416 | 93.7% | 94.1% |
| Sonnet 5.5 | 119 | 2557069 | 2437749 | 95.3% | 96.0% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4963 | 54552334 | 25969792 | 47.6% | 47.5% |
| GPT-6.1 Sol | 4021 | 115863377 | 107612544 | 92.9% | 93.4% |
| Sonnet 5.5 | 4253 | 93625158 | 89409070 | 95.5% | 96.1% |
