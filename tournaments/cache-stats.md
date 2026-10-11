# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0031-20261011-172532)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 245 | 3192235 | 1879552 | 58.9% | 58.7% |
| GPT-6.1 Sol | 139 | 3721969 | 3345664 | 89.9% | 90.9% |
| Sonnet 5.5 | 185 | 5051264 | 4848392 | 96.0% | 96.7% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 8315 | 93127016 | 48036864 | 51.6% | 51.5% |
| GPT-6.1 Sol | 6610 | 192238629 | 178902016 | 93.1% | 93.5% |
| Sonnet 5.5 | 6719 | 147655077 | 140913532 | 95.4% | 96.1% |
