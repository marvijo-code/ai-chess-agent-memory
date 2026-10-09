# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0013-20261009-191602)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 80 | 1136285 | 582528 | 51.3% | 51.2% |
| GPT-6.1 Sol | 34 | 811417 | 719232 | 88.6% | 88.8% |
| Sonnet 5.5 | 50 | 1159181 | 1108727 | 95.6% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 3105 | 33487031 | 15303680 | 45.7% | 45.6% |
| GPT-6.1 Sol | 2784 | 82092814 | 76268288 | 92.9% | 93.4% |
| Sonnet 5.5 | 2876 | 64340449 | 61492654 | 95.6% | 96.2% |
