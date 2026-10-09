# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0011-20261009-135256)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 178 | 1666349 | 830592 | 49.8% | 49.7% |
| GPT-6.1 Sol | 225 | 6600420 | 6078080 | 92.1% | 92.6% |
| Sonnet 5.5 | 189 | 4261061 | 4070880 | 95.5% | 96.2% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 2844 | 30684993 | 13836160 | 45.1% | 45.0% |
| GPT-6.1 Sol | 2562 | 76371325 | 71046272 | 93.0% | 93.5% |
| Sonnet 5.5 | 2593 | 57792215 | 55228737 | 95.6% | 96.1% |
