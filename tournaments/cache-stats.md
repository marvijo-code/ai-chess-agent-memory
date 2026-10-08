# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0005-20261008-214616)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 22 | 137941 | 48128 | 34.9% | 33.8% |
| GPT-6.1 Sol | 32 | 654207 | 621184 | 95.0% | 95.5% |
| Sonnet 5.5 | 31 | 496834 | 462727 | 93.1% | 94.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 1201 | 13397835 | 6223616 | 46.5% | 46.4% |
| GPT-6.1 Sol | 962 | 27876893 | 26036224 | 93.4% | 93.8% |
| Sonnet 5.5 | 1034 | 23129380 | 22125751 | 95.7% | 96.2% |
