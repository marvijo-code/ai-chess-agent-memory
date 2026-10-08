# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0003-20261008-163034)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 136 | 1453901 | 688128 | 47.3% | 47.3% |
| GPT-6.1 Sol | 73 | 1710129 | 1636736 | 95.7% | 96.2% |
| Sonnet 5.5 | 108 | 2701196 | 2597138 | 96.1% | 96.6% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 699 | 7755563 | 3869440 | 49.9% | 49.9% |
| GPT-6.1 Sol | 535 | 14873473 | 13839488 | 93.0% | 93.4% |
| Sonnet 5.5 | 671 | 15481456 | 14855101 | 96.0% | 96.4% |
