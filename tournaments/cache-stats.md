# Input cache hit rate

Hit rate = cached input tokens / all input tokens of the move requests, read from every provider response (claude cache_read_input_tokens, codex cached_input_tokens, OpenAI-compatible prompt_tokens_details.cached_tokens). Warm = without each game's first 3 moves of the player.

## Current tournament (aichess-0027-20261011-075651)

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 108 | 952932 | 457216 | 48.0% | 47.7% |
| GPT-6.1 Sol | 133 | 4355098 | 4034048 | 92.6% | 93.0% |
| Sonnet 5.5 | 136 | 3210878 | 3079351 | 95.9% | 96.5% |

## All tournaments

| Player | Requests | Input tokens | Cached | Hit rate | Warm hit rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| DeepSeek V4.1 Flash | 7152 | 79738394 | 40267264 | 50.5% | 50.4% |
| GPT-6.1 Sol | 5677 | 164508833 | 153157248 | 93.1% | 93.6% |
| Sonnet 5.5 | 5963 | 131643442 | 125704549 | 95.5% | 96.1% |
