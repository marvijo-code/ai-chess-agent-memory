# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0018-20261010-074818)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 286 | 3104276 | 1417216 | 45.7% | 45.5% |
| GPT-6.1 Sol | 224 | 6815091 | 6385792 | 93.7% | 94.3% |
| Sonnet 5.5 | 226 | 4926819 | 4709528 | 95.6% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4788 | 52631712 | 25099392 | 47.7% | 47.6% |
| GPT-6.1 Sol | 3893 | 112180308 | 104160128 | 92.9% | 93.3% |
| Sonnet 5.5 | 4123 | 90697177 | 86610276 | 95.5% | 96.1% |
