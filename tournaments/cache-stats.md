# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0018-20261010-074818)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 99 | 1033091 | 473856 | 45.9% | 45.8% |
| GPT-6.1 Sol | 68 | 1575322 | 1440768 | 91.5% | 92.4% |
| Sonnet 5.5 | 93 | 2099896 | 2012588 | 95.8% | 96.4% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 4601 | 50560527 | 24156032 | 47.8% | 47.7% |
| GPT-6.1 Sol | 3737 | 106940539 | 99215104 | 92.8% | 93.3% |
| Sonnet 5.5 | 3990 | 87870254 | 83913336 | 95.5% | 96.1% |
