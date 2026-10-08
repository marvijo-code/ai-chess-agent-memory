# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0003-20261008-163034)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 136 | 1453901 | 688128 | 47.3% | 47.3% |
| GPT-6.1 Sol | 96 | 2847595 | 2758784 | 96.9% | 97.2% |
| Sonnet 5.5 | 132 | 3780002 | 3652695 | 96.6% | 96.9% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 699 | 7755563 | 3869440 | 49.9% | 49.9% |
| GPT-6.1 Sol | 558 | 16010939 | 14961536 | 93.4% | 93.8% |
| Sonnet 5.5 | 695 | 16560262 | 15910658 | 96.1% | 96.5% |
